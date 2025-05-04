import random
from src.moves import MOVES
import pygame

charSpeed = 4

detectBoxWidth = 6
detectBoxheight = 24

class HealthBox:
    def __init__(self, xOffset: float, yOffset: float, width: int, height: int):
        self.xOffset = xOffset
        self.yOffset = yOffset
        self.height = height
        self.width = width


class DetectBox:
    def __init__(self, xOffset: float, yOffset: float, width: int, height: int):
        self.xOffset = xOffset
        self.yOffset = yOffset
        self.width = width
        self.height = height


class DamageIndicator:
    ttl = 120
    alpha = 0
    def __init__(self, x: float, y: float, damage: int):
        self.x = x
        self.y = y
        self.damage = "-"+str(damage)

    def move(self) -> None:
        self.y -= 0.25
        self.ttl -= 1

        if self.ttl >= 100 and self.alpha < 230:
            self.alpha += 10
        elif self.ttl <= 40 and self.alpha > 25:
            self.alpha -= 5


class Poke:
    xVel = 0
    yVel = 0

    alive = True

    iFrames = 0

    usingMove = ""
    usingMoveTimer = 0

    activeHitboxList = []

    boltShift = 0
    boltShiftCooldown = 0

    deathShrink = 20

    dragonPulseColour = 0
    hyperBeamColour = 0

    ironTailRotation = 0

    moveText = None
    damageIndicators = []

    def __init__(self, x: float, y: float, image: pygame.Surface, moveset = [], name = "",  size = 60, health = 300):
        self.x = x
        self.y = y
        self.startingX = x
        self.startingY = y
        self.size = size
        self.maxHealth = health
        self.health = self.maxHealth

        self.name = name

        self.moveset = moveset

        self.image = image

        self.leftDetectBox = DetectBox(0, detectBoxWidth, detectBoxWidth, size - detectBoxWidth * 2)
        self.rightDetectBox = DetectBox(size - detectBoxWidth, detectBoxWidth, detectBoxWidth, size - detectBoxWidth * 2)
        self.upDetectBox = DetectBox(detectBoxWidth, 0, size - detectBoxWidth * 2, detectBoxWidth)
        self.downDetectBox = DetectBox(detectBoxWidth, size - detectBoxWidth, size - detectBoxWidth * 2, detectBoxWidth)

        self.healthBox = HealthBox(self.size // 2 - 25, 10, 50, 10)

        self.speed = charSpeed

        self.velStart()


        self.moveTimer = self.setMoveTimer()

    def restart(self) -> None:
        self.health = self.maxHealth
        self.velStart()
        self.alive = True
        self.setMoveTimer()
        self.usingMoveTimer = 0
        self.usingMove = ""
        self.iFrames = 0
        self.speed = charSpeed
        self.x = self.startingX
        self.y = self.startingY
        self.activeHitboxList = []


    def setMoveTimer(self) -> int:
        return 130 + random.randint(1, 200)

    def velStart(self) -> None:
        self.xVel = round(random.uniform(-1, 1), 3)
        self.yVel = round(1 - abs(self.xVel), 3) * random.choice([-1, 1])

    def move(self, speed = 2) -> None:
        self.x += self.xVel * speed
        self.y += self.yVel * speed

        if self.iFrames > 0:
            self.iFrames -= 1

    def collideBottom(self) -> None:
        if random.choice(["normal", "normal", "random"]) == "normal":
            self.yVel = self.yVel * -1
            if self.xVel < 0:
                self.xVel = round(1 - abs(self.yVel), 3) * -1
            else:
                self.xVel = round(1 - abs(self.yVel), 3)
        else:
            self.yVel = round(random.uniform(-1, 0), 3)
            self.xVel = round(1 - abs(self.yVel), 3) * random.choice([-1, 1])
        if self.usingMove == "U Turn":
            self.xVel = self.xVel * -1
            self.yVel = self.yVel * -1

    def collideTop(self) -> None:
        if random.choice(["normal", "normal", "random"]) == "normal":
            self.yVel = self.yVel * -1
            if self.xVel < 0:
                self.xVel = round(1 - abs(self.yVel), 3) * -1
            else:
                self.xVel = round(1 - abs(self.yVel), 3)
        else:
            self.yVel = round(random.uniform(0, 1), 3)
            self.xVel = round(1 - abs(self.yVel), 3) * random.choice([-1, 1])
        if self.usingMove == "U Turn":
            self.xVel = self.xVel * -1
            self.yVel = self.yVel * -1

    def collideLeft(self) -> None:
        if random.choice(["normal", "normal", "random"]) == "normal":
            self.xVel = self.xVel * -1
            if self.yVel < 0:
                self.yVel = round(1 - abs(self.xVel), 3) * -1
            else:
                self.yVel = round(1 - abs(self.xVel), 3)
        else:
            self.xVel = round(random.uniform(0, 1), 3)
            self.yVel = round(1 - abs(self.xVel), 3) * random.choice([-1, 1])
        if self.usingMove == "U Turn":
            self.xVel = self.xVel * -1
            self.yVel = self.yVel * -1

    def collideRight(self) -> None:
        if random.choice(["normal", "normal", "random"]) == "normal":
            self.xVel = self.xVel * -1
            if self.yVel < 0:
                self.yVel = round(1 - abs(self.xVel), 3) * -1
            else:
                self.yVel = round(1 - abs(self.xVel), 3)
        else:
            self.xVel = round(random.uniform(-1, 0), 3)
            self.yVel = round(1 - abs(self.xVel), 3) * random.choice([-1, 1])
        if self.usingMove == "U Turn":
            self.xVel = self.xVel * -1
            self.yVel = self.yVel * -1


    def takeDamage(self, damage) -> None:
        self.health -= damage
        self.damageIndicators.append(DamageIndicator(self.x, self.y, damage))

        if self.health <= 0:
            self.alive = False

    def useMove(self) -> None:
        if self.moveTimer <= 0:
            self.moveTimer = self.setMoveTimer()
            self.usingMove = random.choice(self.moveset)

        else:
            self.moveTimer -= 1

        if self.usingMove != "":
            move = MOVES.get(self.usingMove)
            if move is not None:
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
