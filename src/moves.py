import math
import random
import pygame.draw
from src import physics
from src.debug import showHitboxes
from src.globals import g
from src.sprite_loader import INSTANCE as sprites


class MoveText:
    ttl = 60
    alpha = 0

    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text

    def tick(self):
        self.ttl -= 1
        self.y -= 0.50

        if self.ttl >= 50 and self.alpha < 230:
            self.alpha += 20
        elif self.ttl <= 20 and self.alpha > 15:
            self.alpha -= 10


class Move(physics.PhysicsObject):
    type = "bird"
    colour = (255, 0, 255)
    damage = 0
    graphic = "circle"
    usingTime = 0
    acceleration = 1
    linearAcceleration = 0
    growth = 1
    linearGrowth = 0

    image: str

    def __init__(self, poke):
        self.x = poke.x + poke.size / 2
        self.y = poke.y + poke.size / 2
        super().__init__(self.x, self.y, self.size, self.size, True)
        self.ttl = 0
        self.rotate = 0
        self.rotSpeed = 0
        self.poke = poke

    def update(self):
        self.move()

    def move(self):
        self.x += self.xVel
        self.y += self.yVel

        self.xVel += self.linearAcceleration
        self.yVel += self.linearAcceleration

        self.xVel *= self.acceleration
        self.yVel *= self.acceleration

        self.size += self.linearGrowth
        self.size *= self.growth

        if self.size < 1:
            self.size = 1

        self.resize(self.size, self.size)
        self.rotate += self.rotSpeed

        self.ttl -= 1
        if self.ttl == 0:
            physics.allObjects.remove(self)

    def draw(self):
        if showHitboxes:
            pygame.draw.rect(g.window, self.colour, self.getCollider())
        if self.graphic == "image":
            moveImage = sprites.moves.get(self.image)
            if moveImage is None:
                raise Exception(f"Move image is <None>! {self.image}")
            moveImage = pygame.transform.scale(moveImage, (self.size, self.size))
            if moveImage is None:
                print("Move image is <None>! "+self.image)

            rotatedImage = pygame.transform.rotate(moveImage, self.rotate)

            new_rect = rotatedImage.get_rect(center=moveImage.get_rect(center=(self.x + self.size/2, self.y + self.size/2)).center)
            g.window.blit(rotatedImage, new_rect)
        elif self.graphic == "rect":
            pygame.draw.rect(g.window, self.colour, self.getCollider())
        elif self.graphic == "circle":
            pygame.draw.circle(g.window, self.colour, self.getCollider().center, self.size/2)

    @staticmethod
    def use(poke):
        pass


class QuickAttack(Move):
    type = "normal"
    colour = (175, 175, 175)
    damage = 25
    graphic = "circle"
    usingTime = 120

    def __init__(self, poke):
        self.size = poke.size + 25
        super().__init__(poke)
        self.ttl = 15
        self.xVel = poke.xVel * -4
        self.yVel = poke.yVel * -4
        self.linearGrowth = -8

    @staticmethod
    def use(poke):
        if poke.usingMoveTimer == 120:
            poke.moveText = MoveText(poke.x, poke.y, poke.usingMove)
        if poke.usingMoveTimer == 120:
            poke.previousSpeed = poke.speed
            poke.speed *= 4
        elif poke.usingMoveTimer == 1:
            poke.speed = poke.previousSpeed
        QuickAttack(poke)
        poke.usingMoveTimer -= 1
        if poke.usingMoveTimer == 0:
            poke.usingMove = ""


class BraveBird(Move):
    type = "flying"
    colour = (185, 224, 239)
    damage = 55
    graphic = "image"
    usingTime = 90

    image = "bravebird"
    def __init__(self, poke):
        self.size = poke.size + 80
        super().__init__(poke)
        self.x += poke.xVel * -4
        self.y += poke.yVel * -4
        self.rotate = math.atan2(poke.xVel, poke.yVel) * 180/3.14 + 180
        self.ttl = 25
        self.xVel = 2
        self.yVel = 2
        self.linearGrowth = -3

    @staticmethod
    def use(poke):
        if poke.usingMoveTimer == 90:
            poke.moveText = MoveText(poke.x, poke.y, poke.usingMove)
        if poke.usingMoveTimer == 90:
            poke.previousSpeed = poke.speed
            poke.speed *= 3
        elif poke.usingMoveTimer == 1:
            poke.speed = poke.previousSpeed
        BraveBird(poke)
        poke.usingMoveTimer -= 1
        if poke.usingMoveTimer == 0:
            poke.usingMove = ""


class IronHead(Move):
    type = "steel"
    colour = (185, 224, 239)
    damage = 45
    graphic = "image"
    usingTime = 30

    image = "ironhead"
    def __init__(self, poke):
        self.size = poke.size + 45
        super().__init__(poke)
        self.rotate = math.atan2(poke.xVel, poke.yVel) * 180/3.14
        self.ttl = 2
        self.xVel = poke.xVel
        self.yVel = poke.yVel
        self.linearGrowth = -3

    @staticmethod
    def use(poke):
        if poke.usingMoveTimer == 30:
            poke.moveText = MoveText(poke.x, poke.y, poke.usingMove)
        if poke.usingMoveTimer == 30:
            poke.previousSpeed = poke.speed
            poke.speed *= 3
        elif poke.usingMoveTimer == 1:
            poke.speed = poke.previousSpeed
        IronHead(poke)
        poke.usingMoveTimer -= 1
        if poke.usingMoveTimer == 0:
            poke.usingMove = ""


class ZenHeadbutt(Move):
    type = "psychic"
    colour = (185, 224, 239)
    damage = 30
    graphic = "image"
    usingTime = 60

    image = "zenheadbutt"
    def __init__(self, poke):
        self.size = poke.size + 45
        super().__init__(poke)
        self.rotate = math.atan2(poke.xVel, poke.yVel) * 180/3.14
        self.ttl = 4
        self.xVel = poke.xVel * 2
        self.yVel = poke.yVel * 2
        self.linearGrowth = -3

    @staticmethod
    def use(poke):
        if poke.usingMoveTimer == 60:
            poke.moveText = MoveText(poke.x, poke.y, poke.usingMove)
        if poke.usingMoveTimer == 60:
            poke.previousSpeed = poke.speed
            poke.speed *= 3
        elif poke.usingMoveTimer == 1:
            poke.speed = poke.previousSpeed
        ZenHeadbutt(poke)
        poke.usingMoveTimer -= 1
        if poke.usingMoveTimer == 0:
            poke.usingMove = ""

class Waterfall(Move):
    type = "water"
    colour = (185, 224, 239)
    damage = 35
    graphic = "image"
    usingTime = 60

    image = "waterfall"
    def __init__(self, poke):
        self.size = poke.size + 45
        super().__init__(poke)
        self.rotate = math.atan2(poke.xVel, poke.yVel) * 180/3.14
        self.ttl = 4
        self.xVel = poke.xVel * 2
        self.yVel = poke.yVel * 2
        self.linearGrowth = -3

    @staticmethod
    def use(poke):
        if poke.usingMoveTimer == 60:
            poke.moveText = MoveText(poke.x, poke.y, poke.usingMove)
        if poke.usingMoveTimer == 50:
            poke.previousSpeed = poke.speed
            poke.speed *= 2
        elif poke.usingMoveTimer == 1:
            poke.speed = poke.previousSpeed
        Waterfall(poke)
        poke.usingMoveTimer -= 1
        if poke.usingMoveTimer == 0:
            poke.usingMove = ""


class CloseCombat(Move):
    type = "fighting"
    colour = (185, 224, 239)
    damage = 35
    graphic = "image"
    usingTime = 45

    image = "fist"
    def __init__(self, poke):
        self.size = poke.size + 15
        super().__init__(poke)
        self.x = poke.x + random.randint(-80, 80) + poke.xVel * 70
        self.y = poke.y + random.randint(-80, 80) + poke.yVel * 70
        self.ttl = 45
        self.linearGrowth = 5

    def move(self):
        super().move()
        if self.size <= 3:
            self.size = 3
            self.linearGrowth = 0
        if self.ttl == 20:
            self.linearGrowth = -1.5
            self.xVel = 1.5
            self.yVel = 1.5

    @staticmethod
    def use(poke):
        if poke.usingMoveTimer == 45:
            poke.moveText = MoveText(poke.x, poke.y, poke.usingMove)
        if poke.usingMoveTimer % 5 == 0:
            CloseCombat(poke)
        poke.usingMoveTimer -= 1
        if poke.usingMoveTimer == 0:
            poke.usingMove = ""


class DarkPulse(Move):
    type = "dark"
    colour = (185, 224, 239)
    damage = 30
    graphic = "image"
    usingTime = 60

    image = "dark"
    def __init__(self, poke):
        self.size = 25
        super().__init__(poke)
        self.ttl = 45
        self.linearGrowth = 2.5

    @staticmethod
    def use(poke):
        if poke.usingMoveTimer == 60:
            poke.moveText = MoveText(poke.x, poke.y, poke.usingMove)
            poke.previousSpeed = poke.speed
            poke.speed *= 0.05
        if poke.usingMoveTimer % 20 == 0:
            DarkPulse(poke)

        elif poke.usingMoveTimer == 1:
            poke.speed = poke.previousSpeed
        poke.usingMoveTimer -= 1
        if poke.usingMoveTimer == 0:
            poke.usingMove = ""



class Sandstorm(Move):
    type = "rock"
    colour = (185, 224, 239)
    damage = 15
    graphic = "image"
    usingTime = 20

    image = "sandstorm"
    def __init__(self, poke):
        self.size = 25
        super().__init__(poke)
        self.ttl = 200

    @staticmethod
    def use(poke):
        if poke.usingMoveTimer == 20:
            poke.moveText = MoveText(poke.x, poke.y, poke.usingMove)
            poke.previousSpeed = poke.speed
            poke.speed *= 0.05
            Sandstorm(poke)
        elif poke.usingMoveTimer == 1:
            poke.speed = poke.previousSpeed
        poke.usingMoveTimer -= 1
        if poke.usingMoveTimer == 0:
            poke.usingMove = ""


class Earthquake(Move):
    type = "ground"
    colour = (185, 224, 239)
    damage = 60
    graphic = "image"
    usingTime = 60

    image = "earthquake"
    def __init__(self, poke):
        self.size = 25
        super().__init__(poke)
        self.ttl = 60
        self.linearGrowth = 2.5

    def move(self, speed=1):
        super().move()
        self.damage -= 1

    @staticmethod
    def use(poke):
        if poke.usingMoveTimer == 60:
            poke.moveText = MoveText(poke.x, poke.y, poke.usingMove)
            poke.previousSpeed = poke.speed
            poke.speed *= 0.01
        if poke.usingMoveTimer % 20 == 0:
            Earthquake(poke)

        elif poke.usingMoveTimer == 1:
            poke.speed = poke.previousSpeed
        poke.usingMoveTimer -= 1
        if poke.usingMoveTimer == 0:
            poke.usingMove = ""


class DazzlingGleam(Move):
    type = "fairy"
    colour = (185, 224, 239)
    damage = 30
    graphic = "image"
    usingTime = 90

    image = "dazzling"
    def __init__(self, poke):
        self.size = 30
        super().__init__(poke)
        self.ttl = 60
        self.rotate = 0
        self.rotSpeed = 4
        self.linearGrowth = 2

    @staticmethod
    def use(poke):
        if poke.usingMoveTimer == 60:
            poke.moveText = MoveText(poke.x, poke.y, poke.usingMove)
            poke.previousSpeed = poke.speed
            poke.speed *= 0.05
        if poke.usingMoveTimer == 60:
            DazzlingGleam(poke)

        elif poke.usingMoveTimer == 1:
            poke.speed = poke.previousSpeed
        poke.usingMoveTimer -= 1
        if poke.usingMoveTimer == 0:
            poke.usingMove = ""

class IronTail(Move):
    type = "steel"
    colour = (185, 224, 239)
    damage = 30
    graphic = "image"

    image = "irontail"
    usingTime = 90

    def __init__(self, poke):
        self.size = poke.size + 110
        super().__init__(poke)
        self.ttl = 2
        self.rotate = poke.ironTailRotation

    @staticmethod
    def use(poke):
        if poke.usingMoveTimer == 90:
            poke.moveText = MoveText(poke.x, poke.y, poke.usingMove)
            poke.ironTailRotation = 0
            poke.iFrames = 60
        IronTail(poke)
        poke.ironTailRotation += 20

        poke.usingMoveTimer -= 1
        if poke.usingMoveTimer == 0:
            poke.usingMove = ""


class UTurn(Move):
    type = "bug"
    colour = (30, 175, 30)
    damage = 15
    graphic = "circle"
    usingTime = 120
    def __init__(self, poke):
        self.size = poke.size + 25
        super().__init__(poke)
        self.ttl = 20
        self.xVel = 2 * poke.xVel
        self.yVel = 2 * poke.yVel
        self.growth = 0.95

    @staticmethod
    def use(poke):
        if poke.usingMoveTimer == 120:
            poke.moveText = MoveText(poke.x, poke.y, poke.usingMove)
        if poke.usingMoveTimer == 120:
            poke.iFrames = 120
            poke.previousSpeed = poke.speed
            poke.speed *= 3
            poke.xVel *= -1
            poke.yVel *= -1
        elif poke.usingMoveTimer == 1:
            poke.speed = poke.previousSpeed
        UTurn(poke)
        poke.usingMoveTimer -= 1
        if poke.usingMoveTimer == 0:
            poke.usingMove = ""

class Bolt(Move):
    type = "electric"
    graphic = "rect"
    damage = 40
    colour = (251, 225, 13, 10)

    usingTime = 60

    def __init__(self, poke):
        self.size = 40
        super().__init__(poke)
        self.ttl = 90 - (60 - poke.usingMoveTimer)

        if poke.usingMoveTimer == 60 or poke.prevBeam is None:
            poke.beamXVel = poke.xVel
            poke.beamYVel = poke.yVel
        else:
            lastHitbox = poke.prevBeam
            self.x = lastHitbox.x + poke.beamXVel * 40
            self.y = lastHitbox.y + poke.beamYVel * 40
        poke.prevBeam = self

    def move(self):
        super().move()
        if self.ttl == 25:
            self.linearGrowth = -2

    @staticmethod
    def use(poke):
        if poke.usingMoveTimer == 60:
            poke.moveText = MoveText(poke.x, poke.y, poke.usingMove)
        poke.usingMoveTimer -= 1
        if poke.usingMoveTimer > 0:
            Bolt(poke)
        if poke.usingMoveTimer == 0:
            poke.usingMove = ""

class DragonPulse(Move):
    type = "dragon"
    graphic = "circle"
    damage = 40
    colours = [(251, 20, 250), (129, 10, 250)]
    usingTime = 60

    def __init__(self, poke):
        self.size = 40 + (60 - poke.usingMoveTimer)
        super().__init__(poke)
        self.ttl = 90 - (60 - poke.usingMoveTimer)
        if poke.usingMoveTimer == 60 or poke.prevBeam is None:
            poke.beamXVel = poke.xVel
            poke.beamYVel = poke.yVel
        else:
            lastHitbox = poke.prevBeam
            self.x = lastHitbox.x + poke.beamXVel * 25
            self.y = lastHitbox.y + poke.beamYVel * 25
        poke.prevBeam = self
        self.colour = self.colours[poke.dragonPulseColour]

    def move(self):
        super().move()
        if self.ttl == 25:
            self.linearGrowth = -2

    @staticmethod
    def use(poke):
        if poke.usingMoveTimer == 60:
            poke.moveText = MoveText(poke.x, poke.y, poke.usingMove)
        poke.dragonPulseColour = (poke.dragonPulseColour + 1) % 2
        if poke.usingMoveTimer > 0:
            DragonPulse(poke)
        poke.usingMoveTimer -= 1
        if poke.usingMoveTimer == 0:
            poke.usingMove = ""


class HyperBeam(Move):
    type = "normal"
    graphic = "circle"
    damage = 50
    colours = [(255, 183, 0), (255, 221, 0)]

    usingTime = 60

    def __init__(self, poke):
        self.size = 40 + ((60 - poke.usingMoveTimer) * 2)
        super().__init__(poke)
        self.ttl = 90 - (60 - poke.usingMoveTimer)
        if poke.usingMoveTimer == 60 or poke.prevBeam is None:
            poke.beamXVel = poke.xVel
            poke.beamYVel = poke.yVel
        else:
            lastHitbox = poke.prevBeam
            self.x = lastHitbox.x + poke.beamXVel * 40
            self.y = lastHitbox.y + poke.beamYVel * 40
        poke.prevBeam = self
        self.colour = self.colours[poke.dragonPulseColour]

    def move(self):
        super().move()
        if self.ttl == 25:
            self.linearGrowth = -2

    @staticmethod
    def use(poke):
        if poke.usingMoveTimer == 60:
            poke.moveText = MoveText(poke.x, poke.y, poke.usingMove)
            poke.previousSpeed = poke.speed
            poke.speed = 0
        if poke.usingMoveTimer > 0:
            HyperBeam(poke)
        poke.dragonPulseColour = (poke.dragonPulseColour + 1) % 2
        poke.usingMoveTimer -= 1
        if poke.usingMoveTimer == 0:
            poke.moveTimer = 300
            poke.speed = poke.previousSpeed
            poke.usingMove = ""


class IceBeam(Move):
    type = "ice"
    graphic = "rect"
    damage = 40
    colour = (125, 205, 236)

    usingTime = 60

    def __init__(self, poke):
        self.size = 40
        super().__init__(poke)
        self.ttl = 90 - (60 - poke.usingMoveTimer)

        if poke.usingMoveTimer == 60 or poke.prevBeam is None:
            poke.beamXVel = poke.xVel
            poke.beamYVel = poke.yVel
        else:
            lastHitbox = poke.prevBeam
            self.x = lastHitbox.x + poke.beamXVel * 25
            self.y = lastHitbox.y + poke.beamYVel * 25
        poke.prevBeam = self

    def move(self):
        super().move()
        if self.ttl == 25:
            self.linearGrowth = -2

    @staticmethod
    def use(poke):
        if poke.usingMoveTimer == 60:
            poke.moveText = MoveText(poke.x, poke.y, poke.usingMove)
        if poke.usingMoveTimer > 0:
            IceBeam(poke)
        poke.usingMoveTimer -= 1
        if poke.usingMoveTimer == 0:
            poke.usingMove = ""



class ShadowBall(Move):
    type = "ghost"
    spread = 0.0
    linearGrowth = 1
    acceleration = 1.005
    damage = 55
    colour = (255, 20, 200, 30)
    graphic = "image"
    image = "shadowball"

    usingTime = 30

    def __init__(self, poke):
        self.size = 40
        super().__init__(poke)
        self.ttl = 300
        self.xVel = poke.xVel * 2 / poke.speed
        self.yVel = poke.yVel * 2 / poke.speed
        self.rotSpeed = 5

    @staticmethod
    def use(poke):
        if poke.usingMoveTimer == 30:
            poke.moveText = MoveText(poke.x, poke.y, poke.usingMove)
        poke.usingMoveTimer -= 1
        if poke.usingMoveTimer == 29:
            ShadowBall(poke)
        if poke.usingMoveTimer == 0:
            poke.usingMove = ""


class StoneEdge(Move):
    type = "rock"
    spread = 0.2
    damage = 40
    colour = (255, 20, 200, 30)
    graphic = "image"
    image = "stone"
    usingTime = 30

    def __init__(self, poke):
        self.size = 40
        self.xVel = (poke.xVel + round(random.uniform(0 - self.spread, self.spread), 3)) * 2 / poke.speed
        self.yVel = (poke.yVel + round(random.uniform(0 - self.spread, self.spread), 3)) * 2 / poke.speed
        super().__init__(poke)
        self.ttl = 300
        self.rotate = math.atan2(self.xVel, self.yVel) * 180/3.14 + 180

    @staticmethod
    def use(poke):
        if poke.usingMoveTimer == 30:
            poke.moveText = MoveText(poke.x, poke.y, poke.usingMove)
        poke.usingMoveTimer -= 1
        if poke.usingMoveTimer == 29:
            [StoneEdge(poke) for _ in range(5)]
        if poke.usingMoveTimer == 0:
            poke.usingMove = ""


class PoisonSting(Move):
    type = "poison"
    spread = 0.1
    damage = 30
    colour = (255, 20, 200, 30)
    graphic = "image"
    image = "poison"

    usingTime = 30

    def __init__(self, poke):
        self.size = 20
        self.xVel = (poke.xVel + round(random.uniform(0 - self.spread, self.spread), 3)) * 2 / poke.speed
        self.yVel = (poke.yVel + round(random.uniform(0 - self.spread, self.spread), 3)) * 2 / poke.speed
        super().__init__(poke)
        self.ttl = 14
        self.rotate = math.atan2(self.xVel, self.yVel) * 180/3.14 + 180

    @staticmethod
    def use(poke):
        if poke.usingMoveTimer == 30:
            poke.moveText = MoveText(poke.x, poke.y, poke.usingMove)
        poke.usingMoveTimer -= 1
        if poke.usingMoveTimer % 5 == 0:
            PoisonSting(poke)
        if poke.usingMoveTimer == 0:
            poke.usingMove = ""


class Flame(Move):
    type = "fire"
    spread = 0.1
    growth = 1.02
    acceleration = 0.98
    damage = 20
    colour = (255, 102, 0, 30)
    graphic = "image"
    usingTime = 60

    imageList = ["fire1", "fire2", "fire3", "fire4", "fire5", "fire6", "fire7", "fire8"]
    image = imageList[0]
    imageCounter = 0
    imagePointer = 0

    def __init__(self, poke):
        self.size = 20
        super().__init__(poke)
        self.xVel = (poke.xVel + round(random.uniform(0 - self.spread, self.spread), 3)) * 2 / poke.speed
        self.yVel = (poke.yVel + round(random.uniform(0 - self.spread, self.spread), 3)) * 2 / poke.speed
        self.ttl = 16

    def move(self):
        super().move()
        self.imageCounter += 1
        if self.imageCounter == 5:
            self.imageCounter = 0
            self.imagePointer += 1

        if self.imagePointer == len(self.imageList):
            self.imagePointer = 0
        self.image = self.imageList[self.imagePointer]

    @staticmethod
    def use(poke):
        if poke.usingMoveTimer == 60:
            poke.moveText = MoveText(poke.x, poke.y, poke.usingMove)
        poke.usingMoveTimer -= 1
        if poke.usingMoveTimer % 5 == 0:
            Flame(poke)
        if poke.usingMoveTimer == 0:
            poke.usingMove = ""


class Bubble(Move):
    type = "water"
    spread = 0.15
    growth = 1.01
    acceleration = 0.97
    damage = 20
    colour = (20, 50, 250, 30)
    graphic = "image"

    usingTime = 45

    image = "bubble"

    def __init__(self, poke):
        self.size = 20
        super().__init__(poke)
        self.xVel = (poke.xVel + round(random.uniform(0 - self.spread, self.spread), 3)) * 2 / poke.speed
        self.yVel = (poke.yVel + round(random.uniform(0 - self.spread, self.spread), 3)) * 2 / poke.speed
        self.ttl = 120

    @staticmethod
    def use(poke):
        if poke.usingMoveTimer == 45:
            poke.moveText = MoveText(poke.x, poke.y, poke.usingMove)
        poke.usingMoveTimer -= 1
        if poke.usingMoveTimer % 5 == 0:
            Bubble(poke)
        if poke.usingMoveTimer == 0:
            poke.usingMove = ""


class RazorLeaf(Move):
    type = "grass"
    spread = 0.2
    damage = 35
    colour = (50, 250, 100)
    graphic = "image"

    usingTime = 45

    image = "leaf"

    def __init__(self, poke):
        self.size = 30
        super().__init__(poke)
        self.xVel = (poke.xVel + round(random.uniform(0 - self.spread, self.spread), 3)) * 20 / poke.speed
        self.yVel = (poke.yVel + round(random.uniform(0 - self.spread, self.spread), 3)) * 20 / poke.speed
        self.ttl = 120
        self.rotSpeed = 20

    @staticmethod
    def use(poke):
        if poke.usingMoveTimer == 45:
            poke.moveText = MoveText(poke.x, poke.y, poke.usingMove)
        poke.usingMoveTimer -= 1
        if poke.usingMoveTimer % 7 == 0:
            RazorLeaf(poke)
        if poke.usingMoveTimer == 0:
            poke.usingMove = ""


class Bonemerang(Move):
    type = "ground"
    damage = 35
    colour = (50, 250, 100)
    graphic = "image"

    image = "bone"

    usingTime = 120

    def __init__(self, poke):
        self.size = 60
        super().__init__(poke)
        self.ttl = 240
        self.xVel = poke.xVel * 10
        self.yVel = poke.yVel * 10
        self.rotSpeed = 20
        self.linearAcceleration = -0.1

    @staticmethod
    def use(poke):
        if poke.usingMoveTimer == 120:
            poke.moveText = MoveText(poke.x, poke.y, poke.usingMove)
        poke.usingMoveTimer -= 1
        if poke.usingMoveTimer == 119:
            Bonemerang(poke)
        if poke.usingMoveTimer == 0:
            poke.usingMove = ""


MOVES: dict[str, type[Move]] = {
        "Thunderbolt": Bolt,
        "Quick Attack": QuickAttack,
        "Flamethrower": Flame,
        "Shadow Ball": ShadowBall,
        "Razor Leaf": RazorLeaf,
        "Bubble Beam": Bubble,
        "U Turn": UTurn,
        "Ice Beam": IceBeam,
        "Dragon Pulse": DragonPulse,
        "Brave Bird": BraveBird,
        "Stone Edge": StoneEdge,
        "Dazzling Gleam": DazzlingGleam,
        "Close Combat": CloseCombat,
        "Poison Sting": PoisonSting,
        "Dark Pulse": DarkPulse,
        "Iron Tail": IronTail,
        "Iron Head": IronHead,
        "Earthquake": Earthquake,
        "Bonemerang": Bonemerang,
        "Zen Headbutt": ZenHeadbutt,
        "Waterfall": Waterfall,
        "Sandstorm": Sandstorm,
        "Hyper Beam": HyperBeam
    }
