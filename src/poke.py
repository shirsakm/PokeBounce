import random
import pygame.transform
from math import sqrt
from pygame import Rect
from src.moves import MOVES, Move
from src import physics
from src.constants import WINDOW_HEIGHT, WINDOW_WIDTH
from src.globals import g
from src.config import config
from src.sprite_loader import INSTANCE as sprites

charSpeed = 2


class DamageIndicator:
    ttl = 120
    alpha = 0

    def __init__(self, x: float, y: float, damage: int):
        self.x = x
        self.y = y
        self.damage = "-" + str(damage)

    def move(self) -> None:
        self.y -= 0.25
        self.ttl -= 1

        if self.ttl >= 100 and self.alpha < 230:
            self.alpha += 10
        elif self.ttl <= 40 and self.alpha > 25:
            self.alpha -= 5


class Poke(physics.PhysicsObject):
    drawPriority = 1
    alive = False
    iFrames = 0
    usingMove = ""
    usingMoveTimer = 0
    boltShift = 0
    boltShiftCooldown = 0
    deathShrink = 20
    dragonPulseColour = 0
    hyperBeamColour = 0
    ironTailRotation = 0
    moveText = None
    damageIndicators = []
    checksCollision = True

    def __init__(
        self,
        x: float,
        y: float,
        image: pygame.Surface,
        moveset=[],
        name="",
        size=60,
        health=300,
    ):
        super().__init__(x, y, size, size)
        physics.allObjects.remove(self)
        self.prevBeam = None
        self.startingX = x
        self.startingY = y
        self.size = size
        self.maxHealth = health
        self.health = 0
        self.name = name
        self.moveset = moveset
        self.image = image
        self.healthBox = Rect(x + self.size / 2 - 25, y + 10, 50, 10)
        self.speed = charSpeed
        self.moveTimer = self.setMoveTimer()
        self.checksCollision = False

    def update(self):
        if self.alive:
            if self.xVel != 0 or self.yVel != 0:  # update velocity based on speed
                speed = sqrt(self.xVel**2 + self.yVel**2)
                direction = (self.xVel / speed, self.yVel / speed)
                self.xVel = direction[0] * self.speed
                self.yVel = direction[1] * self.speed
            super().update()

            if self.iFrames > 0:
                self.iFrames -= 1

            if self.x > WINDOW_WIDTH or self.x < 0:
                print(self.name, "had a woopsie on the x axis")
                self.x = WINDOW_WIDTH // 2
            if self.y > WINDOW_HEIGHT or self.y < 0:
                print(self.name, "had a woopsie on the y axis")
                self.y = WINDOW_HEIGHT // 2

            self.useMove()

    def draw(self):
        if self.alive:
            if config["Debug"]["showCollisionBoxes"]:
                pygame.draw.rect(g.window, (200, 0, 0, 50), self.getCollider())
            rectImage = Rect((self.x - 60, self.y - 85, self.size, self.size))
            g.window.blit(pygame.transform.flip(self.image, self.xVel > 0, False), rectImage)

            healthRectRed = pygame.Rect(self.x + self.size / 2 - 25, self.y + 10, 50, 10)
            healthPercentWidth = (self.health / 300) * 50
            healthRectGreen = pygame.Rect(self.x + self.size / 2 - 25, self.y + 10, healthPercentWidth, 10)

            pygame.draw.rect(g.window, (175, 0, 0), healthRectRed)
            pygame.draw.rect(g.window, (0, 175, 0), healthRectGreen)

    def revive(self):
        self.health = self.maxHealth
        self.velStart()
        self.alive = True
        physics.allObjects.append(self)
        self.checksCollision = True
        self.setMoveTimer()
        self.usingMoveTimer = 0
        self.usingMove = ""
        self.iFrames = 0
        self.speed = charSpeed
        self.x = self.startingX
        self.y = self.startingY

    def setMoveTimer(self):
        return 130 + random.randint(1, 200)

    def velStart(self):
        self.xVel = round(random.uniform(-1, 1)) * self.speed
        self.yVel = round(1 - abs(self.xVel), 3) * random.choice([-1, 1]) * self.speed

    def collide(self, other):
        if isinstance(other, Move):
            if self.iFrames == 0 and other.poke != self:
                self.takeDamage(other.damage)
                self.iFrames = 180
            return

        if self.usingMove == "U Turn":
            self.xVel *= -1
            self.yVel *= -1
            return
        if random.randint(0, 2) == 0:
            self.velStart()
            return
        contact = self.getCollider().clip(other.getCollider())
        diffX = self.getCollider().centerx - contact.centerx
        diffY = self.getCollider().centery - contact.centery

        speed = sqrt(self.xVel**2 + self.yVel**2)
        if speed == 0:
            return  # TODO this normally...
        direction = (self.xVel / speed, self.yVel / speed)
        if abs(diffX) < abs(diffY):  # used to be a 1/3 chance to random bounce, let's add it back in later
            if diffY > 0:  # collider above
                self.y += contact.height
                self.yVel = abs(self.yVel)
                if self.xVel < 0:
                    self.xVel = -speed * round(1 - abs(direction[1]), 3)
                else:
                    self.xVel = speed * round(1 - abs(direction[1]), 3)
            else:  # collider below
                self.y -= contact.height
                self.yVel = -abs(self.yVel)
                if self.xVel < 0:
                    self.xVel = -speed * round(1 - abs(direction[1]), 3)
                else:
                    self.xVel = speed * round(1 - abs(direction[1]), 3)
        else:
            if diffX > 0:  # collider to the left
                self.x += contact.width
                self.xVel = abs(self.xVel)
                if self.yVel < 0:
                    self.yVel = -speed * round(1 - abs(direction[0]), 3)
                else:
                    self.yVel = speed * round(1 - abs(direction[0]), 3)
            else:  # collider to the right
                self.x -= contact.width
                self.xVel = -abs(self.xVel)
                if self.yVel < 0:
                    self.yVel = -speed * round(1 - abs(direction[0]), 3)
                else:
                    self.yVel = speed * round(1 - abs(direction[0]), 3)

    def takeDamage(self, damage):
        self.health -= damage
        self.damageIndicators.append(DamageIndicator(self.x, self.y, damage))

        if self.health <= 0:
            self.kill()

    def kill(self):
        self.alive = False
        physics.allObjects.remove(self)

    def useMove(self):
        if self.moveTimer <= 0:
            self.moveTimer = self.setMoveTimer()
            self.velStart()
            self.usingMove = random.choice(self.moveset)

        else:
            self.moveTimer -= 1

        if self.usingMove != "":
            move = MOVES.get(self.usingMove)
            if move is None:
                raise ValueError(f"Move {self.usingMove} not found in MOVES dictionary.")
            if self.usingMoveTimer <= 0:
                self.usingMoveTimer = move.usingTime
            move.use(self)


def chooseChars(charList: list[Poke], charNum: int) -> list[Poke]:
    chars = []
    charList = charList + []
    while charNum > 0:
        pick = random.randint(0, len(charList) - 1)
        chars.append(charList[pick])
        charList.pop(pick)
        charNum -= 1
    return chars


allPokemon = {
    "pikachu": Poke(
        75,
        450,
        sprites.get_battler("pikachu"),
        ["Thunderbolt", "Quick Attack", "Iron Tail"],
        "Pikachu",
    ),
    "staraptor": Poke(
        600,
        450,
        sprites.get_battler("staraptor"),
        ["Quick Attack", "Brave Bird", "Close Combat"],
        "Staraptor",
    ),
    "infernape": Poke(
        600,
        75,
        sprites.get_battler("infernape"),
        ["Flamethrower", "Stone Edge", "Close Combat"],
        "Infernape",
    ),
    "umbreon": Poke(
        75,
        75,
        sprites.get_battler("umbreon"),
        ["Quick Attack", "Dark Pulse", "Shadow Ball"],
        "Umbreon",
    ),
    "mamoswine": Poke(
        700,
        500,
        sprites.get_battler("mamoswine"),
        ["Ice Beam", "Stone Edge", "Iron Head"],
        "Mamoswine",
    ),
    "nidoking": Poke(
        1000,
        200,
        sprites.get_battler("nidoking"),
        ["Bubble Beam", "Stone Edge", "Poison Sting"],
        "Nidoking",
    ),
    "scizor": Poke(
        1000,
        400,
        sprites.get_battler("scizor"),
        ["U Turn", "Iron Head", "Close Combat"],
        "Scizor",
    ),
    "wigglytuff": Poke(
        1200,
        300,
        sprites.get_battler("wigglytuff"),
        ["Dazzling Gleam", "Flamethrower", "Thunderbolt"],
        "Wigglytuff",
    ),
    "decidueye": Poke(
        1200,
        150,
        sprites.get_battler("decidueye"),
        ["Razor Leaf", "Brave Bird", "Shadow Ball"],
        "Decidueye",
    ),
    "kingdra": Poke(
        1200,
        650,
        sprites.get_battler("kingdra"),
        ["Dragon Pulse", "Ice Beam", "Bubble Beam"],
        "Kingdra",
    ),
    "smeargle": Poke(
        700,
        100,
        sprites.get_battler("smeargle"),
        [
            "Thunderbolt",
            "Quick Attack",
            "Flamethrower",
            "Shadow Ball",
            "Razor Leaf",
            "Bubble Beam",
            "U Turn",
            "Ice Beam",
            "Dragon Pulse",
            "Brave Bird",
            "Stone Edge",
            "Dazzling Gleam",
            "Close Combat",
            "Poison Sting",
            "Dark Pulse",
            "Iron Tail",
            "Iron Head",
            "Earthquake",
            "Sandstorm",
            "Waterfall",
            "Zen Headbutt",
            "Bonemerang",
            "Hyper Beam",
        ],
        "Smeargle",
    ),
    "marowak": Poke(
        700,
        650,
        sprites.get_battler("marowak"),
        ["Bonemerang", "Flamethrower", "Shadow Ball"],
        "Marowak",
    ),
    "quagsire": Poke(
        300,
        650,
        sprites.get_battler("quagsire"),
        ["Earthquake", "Poison Sting", "Waterfall"],
        "Quagsire",
    ),
    "porygonz": Poke(
        1000,
        650,
        sprites.get_battler("porygonz"),
        ["Hyper Beam", "Thunderbolt", "Ice Beam"],
        "Porygon-Z",
    ),
    "tyranitar": Poke(
        850,
        500,
        sprites.get_battler("tyranitar"),
        ["Sandstorm", "Dark Pulse", "Stone Edge"],
        "Tyranitar",
    ),
    "metagross": Poke(
        850,
        100,
        sprites.get_battler("metagross"),
        ["Earthquake", "Zen Headbutt", "Iron Head"],
        "Metagross",
    ),
}

allPokemon["kangaskhan"] = Poke(
    300,
    100,
    sprites.get_battler("kangaskhan", 0.75, offset_y=10),
    ["Earthquake", "Iron Tail", "Hyper Beam"],
    "Kangaskhan",
)

allPokemon["muk"] = Poke(
    300,
    500,
    sprites.get_battler("muk"),
    ["Poison Sting", "Earthquake", "Sandstorm"],
    "Muk",
)

allPokemon["greninja"] = Poke(
    300,
    300,
    sprites.get_battler("greninja", offset_y=-7),
    ["Waterfall", "Ice Beam", "Dark Pulse"],
    "Greninja",
)
