import random
import math

charSpeed = 4

detectBoxWidth = 6
detectBoxheight = 24

def chooseChars(charList, charNum):
	chars = []
	charList = charList + []
	while charNum > 0:
		pick = random.randint(0, len(charList) - 1)
		chars.append(charList[pick])
		charList.pop(pick)
		charNum -= 1
	return chars

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

class HealthBox:
	def __init__(self, xOffset, yOffset, width, height):
		self.xOffset = xOffset
		self.yOffset = yOffset
		self.height = height
		self.width = width


class DetectBox:

	def __init__(self, xOffset, yOffset, width, height):
		self.xOffset = xOffset
		self.yOffset = yOffset
		self.width = width
		self.height = height

class QuickAttack:
	type = "normal"
	colour = (175, 175, 175)
	damage = 25
	rotate = 0
	graphic = "circle"
	def __init__(self, x, y, pokeSize, size, ttl):
		self.x = x - (size - pokeSize) / 2
		self.y = y - (size - pokeSize) / 2
		self.size = size
		self.pokeSize = pokeSize
		self.startingSize = size
		self.ttl = ttl
		self.startingTtl = ttl
		self.sizeOffset = 0

	def move(self, speed = 1):
		self.ttl -= 1
		self.size -= 8
		self.x += 4
		self.y += 4


class BraveBird:
	type = "flying"
	colour = (185, 224, 239)
	damage = 55
	rotate = 0
	graphic = "image"

	image = "bravebird"
	def __init__(self, x, y, pokeSize, size, xVel, yVel, ttl):
		self.x = x - (size - pokeSize) / 2 + xVel * 4
		self.y = y - (size - pokeSize) / 2 + yVel * 4
		self.size = size
		self.pokeSize = pokeSize
		self.startingSize = size
		self.ttl = ttl
		self.sizeOffset = 0
		self.rotate = math.atan2(xVel, yVel) * 180/3.14 + 180



	def move(self, speed = 1):
		self.ttl -= 1
		self.size -= 3
		self.x += 2
		self.y += 2



class IronHead:
	type = "steel"
	colour = (185, 224, 239)
	damage = 45
	rotate = 0
	graphic = "image"

	image = "ironhead"
	def __init__(self, x, y, pokeSize, size, xVel, yVel, ttl):
		self.x = x - (size - pokeSize) / 2
		self.y = y - (size - pokeSize) / 2
		self.size = size
		self.pokeSize = pokeSize
		self.startingSize = size
		self.ttl = ttl
		self.sizeOffset = 0
		self.rotate = math.atan2(xVel, yVel) * 180/3.14
		self.ttl = ttl



	def move(self, speed = 1):
		self.ttl -= 1
		self.size -= 3
		self.x += 2
		self.y += 2


class ZenHeadbutt:
	type = "psychic"
	colour = (185, 224, 239)
	damage = 30
	rotate = 0
	graphic = "image"

	image = "zenheadbutt"
	def __init__(self, x, y, pokeSize, size, xVel, yVel, ttl):
		self.x = x - (size - pokeSize) / 2
		self.y = y - (size - pokeSize) / 2
		self.size = size
		self.pokeSize = pokeSize
		self.startingSize = size
		self.ttl = ttl
		self.sizeOffset = 0
		self.rotate = math.atan2(xVel, yVel) * 180/3.14
		self.ttl = ttl



	def move(self, speed = 1):
		self.ttl -= 1
		self.size -= 3
		self.x += 2
		self.y += 2


class Waterfall:
	type = "water"
	colour = (185, 224, 239)
	damage = 35
	rotate = 0
	graphic = "image"

	image = "waterfall"
	def __init__(self, x, y, pokeSize, size, xVel, yVel, ttl):
		self.x = x - (size - pokeSize) / 2
		self.y = y - (size - pokeSize) / 2
		self.size = size
		self.pokeSize = pokeSize
		self.startingSize = size
		self.ttl = ttl
		self.sizeOffset = 0
		self.rotate = math.atan2(xVel, yVel) * 180/3.14
		self.ttl = ttl



	def move(self, speed = 1):
		self.ttl -= 1
		self.size -= 3
		self.x += 2
		self.y += 2


class CloseCombat:
	type = "fighting"
	colour = (185, 224, 239)
	damage = 35
	rotate = 0
	graphic = "image"

	image = "fist"
	def __init__(self, x, y, pokeSize, size, ttl):
		self.x = x - (size - pokeSize) / 2
		self.y = y - (size - pokeSize) / 2
		self.size = 0
		self.pokeSize = pokeSize
		self.startingSize = size
		self.sizeOffset = 0
		self.ttl = ttl



	def move(self, speed = 1):
		self.ttl -= 1
		if self.ttl >= 35:
			self.size += 10

		if self.ttl <= 20 and self.size >= 3:
			self.size -= 3
			self.x += 1.5
			self.y += 1.5


class DarkPulse:
	type = "dark"
	colour = (185, 224, 239)
	damage = 30
	rotate = 0
	graphic = "image"
	rotate = 0

	image = "dark"
	def __init__(self, x, y, pokeSize, size, ttl):
		self.x = x - (size - pokeSize) / 2
		self.y = y - (size - pokeSize) / 2
		self.size = size
		self.pokeSize = pokeSize
		self.startingSize = size
		self.ttl = ttl
		self.sizeOffset = 0



	def move(self, speed = 1):
		self.ttl -= 1
		self.size += 5
		self.x -= 1.5
		self.y -= 1.5



class Sandstorm:
	type = "rock"
	colour = (185, 224, 239)
	damage = 15
	rotate = 0
	graphic = "image"
	rotate = 0

	image = "sandstorm"
	def __init__(self, x, y, pokeSize, size, ttl):
		self.x = x - (size - pokeSize) / 2
		self.y = y - (size - pokeSize) / 2
		self.size = size
		self.pokeSize = pokeSize
		self.startingSize = size
		self.ttl = ttl
		self.sizeOffset = 0



	def move(self, speed = 1):
		self.ttl -= 1
		if self.ttl > 270:
			self.size += 5
			self.x -= 2.5
			self.y -= 2.5
		else:
			self.size += 0.1
			self.x -= 0.05
			self.y -= 0.05


class Earthquake:
	type = "ground"
	colour = (185, 224, 239)
	damage = 60
	rotate = 0
	graphic = "image"
	rotate = 0

	image = "earthquake"
	def __init__(self, x, y, pokeSize, size, ttl):
		self.x = x - (size - pokeSize) / 2
		self.y = y - (size - pokeSize) / 2
		self.size = size
		self.pokeSize = pokeSize
		self.startingSize = size
		self.ttl = ttl
		self.sizeOffset = 0



	def move(self, speed = 1):
		self.ttl -= 1
		self.size += 5
		self.x -= 1.5
		self.y -= 1.5
		self.damage -= 1


class DazzlingGleam:
	type = "fairy"
	colour = (185, 224, 239)
	damage = 30
	rotate = 0
	graphic = "image"
	rotate = 0

	image = "dazzling"
	def __init__(self, x, y, pokeSize, size, ttl):
		self.x = x - (size - pokeSize) / 2
		self.y = y - (size - pokeSize) / 2
		self.size = size
		self.pokeSize = pokeSize
		self.startingSize = size
		self.ttl = ttl
		self.sizeOffset = 0
		self.ttl = ttl



	def move(self, speed = 1):
		self.ttl -= 1
		self.size += 4.5
		self.x -= 1.5
		self.y -= 1.5
		self.rotate += 4


class IronTail:
	type = "steel"
	colour = (185, 224, 239)
	damage = 30
	rotate = 0
	graphic = "image"

	image = "irontail"

	def __init__(self, x, y, pokeSize, size, ttl, rotate):
		self.x = x - (size - pokeSize) / 2
		self.y = y - (size - pokeSize) / 2
		self.size = size
		self.pokeSize = pokeSize
		self.startingSize = size
		self.ttl = ttl
		self.sizeOffset = 0
		self.ttl = ttl
		self.rotate = rotate



	def move(self, speed = 1):
		self.ttl -= 1


class UTurn:
	type = "bug"
	colour = (30, 175, 30)
	damage = 15
	rotate = 0
	graphic = "circle"
	def __init__(self, x, y, pokeSize, size, ttl):
		self.x = x - (size - pokeSize) / 2
		self.y = y - (size - pokeSize) / 2
		self.size = size
		self.pokeSize = pokeSize
		self.startingSize = size
		self.ttl = ttl
		self.startingTtl = ttl
		self.sizeOffset = 0

	def move(self, speed = 1):
		self.ttl -= 1
		self.size -= 4
		self.x += 2
		self.y += 2

class Bolt:
	type = "electric"
	graphic = "rect"
	damage = 40
	boltRects = []
	colour = (251, 225, 13, 10)

	def __init__(self, x, y, xVel, yVel, pokeSize, size, ttl = 60, isFirst = False):
		if isFirst:
			self.x = x + pokeSize // 2 - size//2
			self.y = y + pokeSize // 2 - size//2
		else:
			self.x = x 
			self.y = y
		self.xVel = xVel
		self.yVel = yVel
		self.size = size
		self.ttl = ttl

	def move(self):
		self.ttl -= 1
		self.colour = (251, 225, 13, 1)
		if self.ttl < 25:
			self.size -= 2

class DragonPulse:
	type = "dragon"
	graphic = "circle"
	damage = 40
	boltRects = []
	colours = [(251, 20, 250), (129, 10, 250)]

	def __init__(self, x, y, xVel, yVel, pokeSize, size, ttl = 60, isFirst = False, colourPick = 0):
		if isFirst:
			self.x = x + pokeSize // 2 - size//2
			self.y = y + pokeSize // 2 - size//2
		else:
			self.x = x 
			self.y = y
		self.xVel = xVel
		self.yVel = yVel
		self.size = size
		self.ttl = ttl
		self.colour = self.colours[colourPick]

	def move(self):
		self.ttl -= 1
		if self.ttl < 25:
			self.size -= 2


class HyperBeam:
	type = "normal"
	graphic = "circle"
	damage = 50
	boltRects = []
	colours = [(255, 183, 0), (255, 221, 0)]

	def __init__(self, x, y, xVel, yVel, pokeSize, size, ttl = 60, isFirst = False, colourPick = 0):
		if isFirst:
			self.x = x + pokeSize // 2 - size//2
			self.y = y + pokeSize // 2 - size//2
		else:
			self.x = x 
			self.y = y
		self.xVel = xVel
		self.yVel = yVel
		self.size = size
		self.ttl = ttl
		self.colour = self.colours[colourPick]

	def move(self):
		self.ttl -= 1
		if self.ttl < 25:
			self.size -= 2


class IceBeam:
	type = "ice"
	graphic = "rect"
	damage = 40
	boltRects = []
	colour = (125, 205, 236)

	def __init__(self, x, y, xVel, yVel, pokeSize, size, ttl = 60, isFirst = False):
		if isFirst:
			self.x = x + pokeSize // 2 - size//2
			self.y = y + pokeSize // 2 - size//2
		else:
			self.x = x 
			self.y = y
		self.xVel = xVel
		self.yVel = yVel
		self.size = size
		self.ttl = ttl

	def move(self):
		self.ttl -= 1
		if self.ttl < 25:
			self.size -= 2



class ShadowBall:
	type = "ghost"
	ttl = 300
	spread = 0.0
	growth = 1.01
	speedDecay = 1.005
	damage = 55
	colour = (255, 20, 200, 30)
	graphic = "image"
	image = "shadowball"
	rotate = 0



	def __init__(self, x, y, xVel, yVel, pokeSize, speed =2, size = 40):
		self.x = x + pokeSize // 2 - size//2
		self.y = y + pokeSize // 2 - size//2
		self.xVel = xVel
		self.yVel = yVel
		self.size = size
		self.speed = speed


	def move(self):
		self.x += self.xVel * self.speed
		self.y += self.yVel * self.speed

		self.xVel = self.xVel * self.speedDecay
		self.yVel = self.yVel * self.speedDecay

		self.size = self.size * self.growth

		self.rotate += 5

		self.ttl -= 1


class StoneEdge:
	type = "rock"
	ttl = 300
	spread = 0.2
	growth = 1.00
	speedDecay = 1.000
	damage = 40
	colour = (255, 20, 200, 30)
	graphic = "image"
	image = "stone"



	def __init__(self, x, y, xVel, yVel, pokeSize, speed =2, size = 40):
		self.x = x + pokeSize // 2 - size//2
		self.y = y + pokeSize // 2 - size//2
		self.xVel = xVel + round(random.uniform(0 - self.spread, self.spread),3)
		self.yVel = yVel + round(random.uniform(0 - self.spread, self.spread),3)
		self.size = size
		self.speed = speed
		self.rotate = math.atan2(xVel, yVel) * 180/3.14 + 180


	def move(self):
		self.x += self.xVel * self.speed
		self.y += self.yVel * self.speed

		self.xVel = self.xVel * self.speedDecay
		self.yVel = self.yVel * self.speedDecay

		self.size = self.size * self.growth

		self.ttl -= 1


class PoisonSting:
	type = "poison"
	ttl = 300
	spread = 0.1
	growth = 1.00
	speedDecay = 1.000
	damage = 30
	colour = (255, 20, 200, 30)
	graphic = "image"
	image = "poison"



	def __init__(self, x, y, xVel, yVel, pokeSize, speed =2, size = 20):
		self.x = x + pokeSize // 2 - size//2
		self.y = y + pokeSize // 2 - size//2
		self.xVel = xVel + round(random.uniform(0 - self.spread, self.spread),3)
		self.yVel = yVel + round(random.uniform(0 - self.spread, self.spread),3)
		self.size = size
		self.speed = speed
		self.rotate = math.atan2(xVel, yVel) * 180/3.14 + 180


	def move(self):
		self.x += self.xVel * self.speed
		self.y += self.yVel * self.speed

		self.xVel = self.xVel * self.speedDecay
		self.yVel = self.yVel * self.speedDecay

		self.size = self.size * self.growth

		self.ttl -= 1


class Flame:
	type = "fire"
	ttl = 90
	spread = 0.1
	growth = 1.02
	speedDecay = 0.98
	damage = 20
	colour = (255, 102, 0, 30)
	graphic = "image"

	rotate = 0

	imageList = ["fire1", "fire2", "fire3", "fire4", "fire5", "fire6", "fire7", "fire8"]
	image = imageList[0]
	imageCounter = 0
	imagePointer = 0


	def __init__(self, x, y, xVel, yVel, pokeSize, speed =2, size = 20):
		self.x = x + pokeSize // 2 - size//2
		self.y = y + pokeSize // 2 - size//2
		self.xVel = xVel + round(random.uniform(0 - self.spread, self.spread),3)
		self.yVel = yVel + round(random.uniform(0 - self.spread, self.spread),3)
		self.size = size
		self.speed = speed


	def move(self):
		self.x += self.xVel * self.speed
		self.y += self.yVel * self.speed

		self.xVel = self.xVel * self.speedDecay
		self.yVel = self.yVel * self.speedDecay

		self.size = self.size * self.growth

		self.imageCounter += 1
		if self.imageCounter == 5:
			self.imageCounter = 0
			self.imagePointer += 1

		if self.imagePointer == len(self.imageList):
			self.imagePointer = 0
		self.image = self.imageList[self.imagePointer]
		self.ttl -= 1

class Bubble:
	type = "water"
	ttl = 120
	spread = 0.15
	growth = 1.01
	speedDecay = 0.97
	damage = 20
	colour = (20, 50, 250, 30)
	graphic = "image"

	image = "bubble"
	rotate = 0


	def __init__(self, x, y, xVel, yVel, pokeSize, speed =2, size = 20):
		self.x = x + pokeSize // 2 - size//2
		self.y = y + pokeSize // 2 - size//2
		self.xVel = xVel + round(random.uniform(0 - self.spread, self.spread),3)
		self.yVel = yVel + round(random.uniform(0 - self.spread, self.spread),3)
		self.size = size
		self.speed = speed


	def move(self):
		self.x += self.xVel * self.speed
		self.y += self.yVel * self.speed

		self.xVel = self.xVel * self.speedDecay
		self.yVel = self.yVel * self.speedDecay

		self.size = self.size * self.growth

		self.ttl -= 1

class RazorLeaf:
	type = "grass"
	ttl = 120
	spread = 0.2
	growth = 1.000
	speedDecay = 1
	damage = 35
	colour = (50, 250, 100)
	graphic = "image"
	rotate = 0

	image = "leaf"

	def __init__(self, x, y, xVel, yVel, pokeSize, speed =2, size = 30):
		self.x = x + pokeSize // 2 - size//2
		self.y = y + pokeSize // 2 - size//2
		self.xVel = xVel + round(random.uniform(0 - self.spread, self.spread),3)
		self.yVel = yVel + round(random.uniform(0 - self.spread, self.spread),3)
		self.size = size
		self.speed = speed


	def move(self):
		self.x += self.xVel * self.speed
		self.y += self.yVel * self.speed

		self.xVel = self.xVel * self.speedDecay
		self.yVel = self.yVel * self.speedDecay

		self.size = self.size * self.growth

		self.rotate += 20

		self.ttl -= 1



class Bonemerang:
	type = "ground"
	ttl = 240
	spread = 0
	growth = 1.000
	speedDecay = 1
	damage = 35
	colour = (50, 250, 100)
	graphic = "image"
	rotate = 0

	image = "bone"

	def __init__(self, x, y, xVel, yVel, pokeSize, speed =2, size = 60):
		self.x = x + pokeSize // 2 - size//2
		self.y = y + pokeSize // 2 - size//2
		self.xVel = xVel 
		self.yVel = yVel 
		self.size = size
		self.speed = speed


	def move(self):
		self.x += self.xVel * self.speed
		self.y += self.yVel * self.speed

		self.xVel = self.xVel * self.speedDecay
		self.yVel = self.yVel * self.speedDecay

		self.size = self.size * self.growth

		self.rotate += 20

		self.ttl -= 1
		self.speed -= 0.1



class DamageIndicator:
	ttl = 120
	alpha = 0
	def __init__(self, x, y, damage):
		self.x = x 
		self.y = y 
		self.damage = "-"+str(damage)

	def move(self):
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

	moveText = ""
	damageIndicators = []

	def __init__(self, x, y, image = "", size = 60, moveset = [], name = "", health = 300):
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

	def restart(self):
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


	def setMoveTimer(self):
		return 130 + random.randint(1,200)

	def velStart(self):
		self.xVel = round(random.uniform(-1,1),3)
		self.yVel = round(1 - abs(self.xVel), 3) * random.choice([-1,1])

	def move(self, speed = 2):
		self.x += self.xVel * speed
		self.y += self.yVel * speed

		if self.iFrames > 0:
			self.iFrames -= 1

	def collideBottom(self):
		if random.choice(["normal","normal","random"]) == "normal":
			self.yVel = self.yVel * -1
			if self.xVel < 0:
				self.xVel = round(1 - abs(self.yVel), 3) * -1
			else:
				self.xVel = round(1 - abs(self.yVel), 3)
		else:
			self.yVel = round(random.uniform(-1,0),3)
			self.xVel = round(1 - abs(self.yVel), 3) * random.choice([-1,1])
		if self.usingMove == "U Turn":
			self.xVel = self.xVel * -1
			self.yVel = self.yVel * -1
			
	def collideTop(self):
		if random.choice(["normal","normal","random"]) == "normal":
			self.yVel = self.yVel * -1
			if self.xVel < 0:
				self.xVel = round(1 - abs(self.yVel), 3) * -1
			else:
				self.xVel = round(1 - abs(self.yVel), 3)
		else:
			self.yVel = round(random.uniform(0,1),3)
			self.xVel = round(1 - abs(self.yVel), 3) * random.choice([-1,1])
		if self.usingMove == "U Turn":
			self.xVel = self.xVel * -1
			self.yVel = self.yVel * -1
			
	def collideLeft(self):
		if random.choice(["normal","normal","random"]) == "normal":
			self.xVel = self.xVel * -1
			if self.yVel < 0:
				self.yVel = round(1 - abs(self.xVel), 3) * -1
			else:
				self.yVel = round(1 - abs(self.xVel), 3)
		else:
			self.xVel = round(random.uniform(0,1),3)
			self.yVel = round(1 - abs(self.xVel), 3) * random.choice([-1,1])
		if self.usingMove == "U Turn":
			self.xVel = self.xVel * -1
			self.yVel = self.yVel * -1
			
	def collideRight(self):
		if random.choice(["normal","normal","random"]) == "normal":
			self.xVel = self.xVel * -1
			if self.yVel < 0:
				self.yVel = round(1 - abs(self.xVel), 3) * -1
			else:
				self.yVel = round(1 - abs(self.xVel), 3)
		else:
			self.xVel = round(random.uniform(-1,0),3)
			self.yVel = round(1 - abs(self.xVel), 3) * random.choice([-1,1])
		if self.usingMove == "U Turn":
			self.xVel = self.xVel * -1
			self.yVel = self.yVel * -1


	def takeDamage(self, damage):
		self.health -= damage
		self.damageIndicators.append(DamageIndicator(self.x, self.y, damage))

		if self.health <= 0:
			self.alive = False

	def useMove(self):
		if self.moveTimer <= 0:
			self.moveTimer = self.setMoveTimer()
			allMoves = ["Thunderbolt", "Quick Attack", "Flamethrower", "Shadow Ball", "Razor Leaf", "Bubble Beam", "U Turn", "Ice Beam", "Dragon Pulse", "Brave Bird", "Stone Edge", "Dazzling Gleam", "Close Combat", "Poison Sting", "Dark Pulse", "Iron Tail", "Iron Head"]
			self.usingMove = random.choice(self.moveset)
			
		else:
			self.moveTimer -= 1

		if self.usingMove == "Flamethrower":
			if self.usingMoveTimer <= 0:
				self.usingMoveTimer = 60
			self.useFlamethrower()

		if self.usingMove == "Bubble Beam":
			if self.usingMoveTimer <= 0:
				self.usingMoveTimer = 45
			self.useBubble()

		if self.usingMove == "Razor Leaf":
			if self.usingMoveTimer <= 0:
				self.usingMoveTimer = 45
			self.useRazorLeaf()

		if self.usingMove == "Thunderbolt":
			if self.usingMoveTimer <= 0:
				self.usingMoveTimer = 60
			self.useThunderbolt()
		if self.usingMove == "Dragon Pulse":
			if self.usingMoveTimer <= 0:
				self.usingMoveTimer = 60
			self.useDragonPulse()

		if self.usingMove == "Hyper Beam":
			if self.usingMoveTimer <= 0:
				self.usingMoveTimer = 60
			self.useHyperBeam()

		if self.usingMove == "Ice Beam":
			if self.usingMoveTimer <= 0:
				self.usingMoveTimer = 60
			self.useIceBeam()

		if self.usingMove == "Quick Attack":
			if self.usingMoveTimer <= 0:
				self.usingMoveTimer = 120
			self.useQuickAttack()

		if self.usingMove == "Brave Bird":
			if self.usingMoveTimer <= 0:
				self.takeDamage(5)
				self.usingMoveTimer = 90
			self.useBraveBird()

		if self.usingMove == "U Turn":
			if self.usingMoveTimer <= 0:
				self.usingMoveTimer = 120
			self.useUTurn()

		if self.usingMove == "Shadow Ball":
			if self.usingMoveTimer <= 0:
				self.usingMoveTimer = 30
			self.useShadowBall()

		if self.usingMove == "Stone Edge":
			if self.usingMoveTimer <= 0:
				self.usingMoveTimer = 30
			self.useStoneEdge()

		if self.usingMove == "Poison Sting":
			if self.usingMoveTimer <= 0:
				self.usingMoveTimer = 30
			self.usePoisonSting()

		if self.usingMove == "Dark Pulse":
			if self.usingMoveTimer <= 0:
				self.usingMoveTimer = 60
			self.useDarkPulse()

		if self.usingMove == "Dazzling Gleam":
			if self.usingMoveTimer <= 0:
				self.usingMoveTimer = 60
			self.useDazzlingGleam()

		if self.usingMove == "Earthquake":
			if self.usingMoveTimer <= 0:
				self.usingMoveTimer = 60
			self.useEarthquake()

		if self.usingMove == "Zen Headbutt":
			if self.usingMoveTimer <= 0:
				self.usingMoveTimer = 60
			self.useZenHeadbutt()

		if self.usingMove == "Iron Tail":
			if self.usingMoveTimer <= 0:
				self.usingMoveTimer = 90
			self.useIronTail()

		if self.usingMove == "Iron Head":
			if self.usingMoveTimer <= 0:
				self.usingMoveTimer = 30
			self.useIronHead()

		if self.usingMove == "Waterfall":
			if self.usingMoveTimer <= 0:
				self.usingMoveTimer = 60
			self.useWaterfall()

		if self.usingMove == "Close Combat":
			if self.usingMoveTimer <= 0:
				self.usingMoveTimer = 45
			self.useCloseCombat()

		if self.usingMove == "Bonemerang":
			if self.usingMoveTimer <= 0:
				self.usingMoveTimer = 120
			self.useBonemerang()

		if self.usingMove == "Sandstorm":
			if self.usingMoveTimer <= 0:
				self.usingMoveTimer = 30
			self.useSandstorm()



	def useBonemerang(self):
		if self.usingMoveTimer == 120:
			self.moveText = MoveText(self.x, self.y, self.usingMove)
		self.usingMoveTimer -= 1
		if self.usingMoveTimer == 119:
			ball = Bonemerang(self.x, self.y, self.xVel, self.yVel, self.size, 10)
			self.activeHitboxList.append(ball)
		if self.usingMoveTimer == 0:
			self.usingMove = ""

	def useShadowBall(self):
		if self.usingMoveTimer == 30:
			self.moveText = MoveText(self.x, self.y, self.usingMove)
		self.usingMoveTimer -= 1
		if self.usingMoveTimer == 29:
			ball = ShadowBall(self.x, self.y, self.xVel, self.yVel, self.size, 12)
			self.activeHitboxList.append(ball)
		if self.usingMoveTimer == 0:
			self.usingMove = ""

	def useStoneEdge(self):
		if self.usingMoveTimer == 30:
			self.moveText = MoveText(self.x, self.y, self.usingMove)
		self.usingMoveTimer -= 1
		if self.usingMoveTimer == 29:
			ball = StoneEdge(self.x, self.y, self.xVel, self.yVel, self.size, 14)
			self.activeHitboxList.append(ball)
			ball = StoneEdge(self.x, self.y, self.xVel, self.yVel, self.size, 14)
			self.activeHitboxList.append(ball)
			ball = StoneEdge(self.x, self.y, self.xVel, self.yVel, self.size, 14)
			self.activeHitboxList.append(ball)
			ball = StoneEdge(self.x, self.y, self.xVel, self.yVel, self.size, 14)
			self.activeHitboxList.append(ball)
			ball = StoneEdge(self.x, self.y, self.xVel, self.yVel, self.size, 14)
			self.activeHitboxList.append(ball)
		if self.usingMoveTimer == 0:
			self.usingMove = ""

	def usePoisonSting(self):
		if self.usingMoveTimer == 30:
			self.moveText = MoveText(self.x, self.y, self.usingMove)
		self.usingMoveTimer -= 1
		if self.usingMoveTimer % 5 == 0:
			ball = PoisonSting(self.x, self.y, self.xVel, self.yVel, self.size, 14)
			self.activeHitboxList.append(ball)
		if self.usingMoveTimer == 0:
			self.usingMove = ""

	def useFlamethrower(self):
		if self.usingMoveTimer == 60:
			self.moveText = MoveText(self.x, self.y, self.usingMove)
		self.usingMoveTimer -= 1
		if self.usingMoveTimer % 5 == 0:
			flame = Flame(self.x, self.y, self.xVel, self.yVel, self.size, 16)
			self.activeHitboxList.append(flame)
		if self.usingMoveTimer == 0:
			self.usingMove = ""

	def useBubble(self):
		if self.usingMoveTimer == 45:
			self.moveText = MoveText(self.x, self.y, self.usingMove)
		self.usingMoveTimer -= 1
		if self.usingMoveTimer % 5 == 0:
			bubble = Bubble(self.x, self.y, self.xVel, self.yVel, self.size, 20)
			self.activeHitboxList.append(bubble)
		if self.usingMoveTimer == 0:
			self.usingMove = ""

	def useRazorLeaf(self):
		if self.usingMoveTimer == 45:
			self.moveText = MoveText(self.x, self.y, self.usingMove)
		self.usingMoveTimer -= 1
		if self.usingMoveTimer % 7 == 0:
			razorLeaf = RazorLeaf(self.x, self.y, self.xVel, self.yVel, self.size, 20)
			self.activeHitboxList.append(razorLeaf)
		if self.usingMoveTimer == 0:
			self.usingMove = ""

	def useThunderbolt(self):
		if self.usingMoveTimer == 60:
			self.moveText = MoveText(self.x, self.y, self.usingMove)
		speed = 40
		size = 40
		ttl = 90 - (60 - self.usingMoveTimer)
		if self.boltShift == 0 and self.boltShiftCooldown == 0:
			self.boltShift = random.choice([0,0,0,0,4])

		if self.usingMoveTimer == 60:
			bolt = Bolt(self.x, self.y, self.xVel, self.yVel, self.size, size, ttl, True)
			self.activeHitboxList.append(bolt)
			self.xVelUnshift = self.xVel
			self.yVelUnshift = self.yVel
		elif self.usingMoveTimer > 0:
			lastHitbox = self.activeHitboxList[-1]
			if self.boltShift == 0:
				boltX = lastHitbox.x + lastHitbox.xVel * speed
				boltY = lastHitbox.y + lastHitbox.yVel * speed
				self.xVelUnshift = lastHitbox.xVel
				self.yVelUnshift = lastHitbox.yVel
			
			elif self.boltShift == 1:
				boltX = lastHitbox.x + self.xVelUnshift * speed
				boltY = lastHitbox.y + self.yVelUnshift * speed
				self.boltShiftCooldown = 10

			else:
				boltX = lastHitbox.x + lastHitbox.yVel * speed
				boltY = lastHitbox.y + lastHitbox.xVel * speed

			bolt = Bolt(boltX, boltY, lastHitbox.xVel, lastHitbox.yVel, self.size, size, ttl)
			self.activeHitboxList.append(bolt)
		self.usingMoveTimer -= 1
		if self.usingMoveTimer == 0:
			self.usingMove = ""
		if self.boltShift:
			self.boltShift -= 1
		if self.boltShiftCooldown:
			self.boltShiftCooldown -= 1


	def useDragonPulse(self):
		if self.usingMoveTimer == 60:
			self.moveText = MoveText(self.x, self.y, self.usingMove)
		speed = 25
		size = 40 + (60 - self.usingMoveTimer)
		ttl = 90 - (60 - self.usingMoveTimer)
		self.dragonPulseColour = (self.dragonPulseColour + 1) % 2

		if self.usingMoveTimer == 60:
			bolt = DragonPulse(self.x, self.y, self.xVel, self.yVel, self.size, size, ttl, True, self.dragonPulseColour)
			self.activeHitboxList.append(bolt)
			self.xVelUnshift = self.xVel
			self.yVelUnshift = self.yVel
		elif self.usingMoveTimer > 0:
			lastHitbox = self.activeHitboxList[-1]
			boltX = lastHitbox.x + lastHitbox.xVel * speed
			boltY = lastHitbox.y + lastHitbox.yVel * speed
			bolt = DragonPulse(boltX, boltY, lastHitbox.xVel, lastHitbox.yVel, self.size, size, ttl, False, self.dragonPulseColour)
			self.activeHitboxList.append(bolt)
		self.usingMoveTimer -= 1
		if self.usingMoveTimer == 0:
			self.usingMove = ""



	def useHyperBeam(self):
		if self.usingMoveTimer == 60:
			self.moveText = MoveText(self.x, self.y, self.usingMove)
		speed = 25
		size = 40 + ((60 - self.usingMoveTimer) * 2)
		ttl = 90 - (60 - self.usingMoveTimer)
		self.dragonPulseColour = (self.dragonPulseColour + 1) % 2

		if self.usingMoveTimer == 60:
			bolt = HyperBeam(self.x, self.y, self.xVel, self.yVel, self.size, size, ttl, True, self.dragonPulseColour)
			self.activeHitboxList.append(bolt)
			self.xVelUnshift = self.xVel
			self.yVelUnshift = self.yVel
			self.previousSpeed = self.speed
			self.speed = 0
		elif self.usingMoveTimer > 0:
			lastHitbox = self.activeHitboxList[-1]
			boltX = lastHitbox.x + lastHitbox.xVel * speed
			boltY = lastHitbox.y + lastHitbox.yVel * speed
			bolt = HyperBeam(boltX, boltY, lastHitbox.xVel, lastHitbox.yVel, self.size, size, ttl, False, self.dragonPulseColour)
			self.activeHitboxList.append(bolt)
		self.usingMoveTimer -= 1
		if self.usingMoveTimer == 0:
			self.moveTimer = 300
			self.speed = self.previousSpeed
			self.usingMove = ""



	def useIceBeam(self):
		if self.usingMoveTimer == 60:
			self.moveText = MoveText(self.x, self.y, self.usingMove)
		speed = 40
		size = 40
		ttl = 90  - (60 - self.usingMoveTimer)
		if self.boltShift == 0 and self.boltShiftCooldown == 0:
			self.boltShift = random.choice([0,0,0,0,0,3,-3])

		if self.usingMoveTimer == 60:
			bolt = IceBeam(self.x, self.y, self.xVel, self.yVel, self.size, size, ttl, True)
			self.activeHitboxList.append(bolt)
			self.xVelUnshift = self.xVel
			self.yVelUnshift = self.yVel
		elif self.usingMoveTimer > 0:
			lastHitbox = self.activeHitboxList[-1]
			if self.boltShift == 0:
				boltX = lastHitbox.x + lastHitbox.xVel * speed
				boltY = lastHitbox.y + lastHitbox.yVel * speed
				self.xVelUnshift = lastHitbox.xVel
				self.yVelUnshift = lastHitbox.yVel
			
			elif self.boltShift == 1:
				boltX = lastHitbox.x + self.xVelUnshift * speed
				boltY = lastHitbox.y + self.yVelUnshift * speed
				self.boltShiftCooldown = 5

			else:
				boltX = lastHitbox.x + lastHitbox.yVel * speed
				boltY = lastHitbox.y + lastHitbox.xVel * speed

			bolt = IceBeam(boltX, boltY, lastHitbox.xVel, lastHitbox.yVel, self.size, size, ttl)
			self.activeHitboxList.append(bolt)
		self.usingMoveTimer -= 1
		if self.usingMoveTimer == 0:
			self.usingMove = ""
		if self.boltShift > 0:
			self.boltShift -= 1
		elif self.boltShift < 0:
			self.boltShift += 1
		if self.boltShiftCooldown:
			self.boltShiftCooldown -= 1


	def useQuickAttack(self):
		if self.usingMoveTimer == 120:
			self.moveText = MoveText(self.x, self.y, self.usingMove)
		ttl = 15
		if self.usingMoveTimer == 120:
			self.previousSpeed = self.speed
			self.speed = 16
		elif self.usingMoveTimer == 1:
			self.speed = self.previousSpeed
		self.activeHitboxList.append(QuickAttack(self.x, self.y, self.size, self.size + 25, ttl))
		self.usingMoveTimer -= 1
		if self.usingMoveTimer == 0:
			self.usingMove = ""

	def useBraveBird(self):
		if self.usingMoveTimer == 90:
			self.moveText = MoveText(self.x, self.y, self.usingMove)
		ttl = 25
		if self.usingMoveTimer == 90:
			self.previousSpeed = self.speed
			self.speed = 12
		elif self.usingMoveTimer == 1:
			self.speed = self.previousSpeed
		self.activeHitboxList.append(BraveBird(self.x, self.y, self.size, self.size + 80, self.xVel, self.yVel, ttl))
		self.usingMoveTimer -= 1
		if self.usingMoveTimer == 0:
			self.usingMove = ""

	def useUTurn(self):
		if self.usingMoveTimer == 120:
			self.moveText = MoveText(self.x, self.y, self.usingMove)
		ttl = 20
		if self.usingMoveTimer == 120:
			self.iFrames = 120
			self.previousSpeed = self.speed
			self.speed = -12
		elif self.usingMoveTimer == 1:
			self.speed = self.previousSpeed
		self.activeHitboxList.append(UTurn(self.x, self.y, self.size, self.size + 25, ttl))
		self.usingMoveTimer -= 1
		if self.usingMoveTimer == 0:
			self.usingMove = ""


	def useDarkPulse(self):
		if self.usingMoveTimer == 60:
			self.moveText = MoveText(self.x, self.y, self.usingMove)
			self.previousSpeed = self.speed
			self.speed = 0.25
		ttl = 45
		if self.usingMoveTimer % 20 == 0:
			self.activeHitboxList.append(DarkPulse(self.x, self.y, self.size, 25, ttl))

		elif self.usingMoveTimer == 1:
			self.speed = self.previousSpeed
		self.usingMoveTimer -= 1
		if self.usingMoveTimer == 0:
			self.usingMove = ""

	def useSandstorm(self):
		if self.usingMoveTimer == 20:
			self.moveText = MoveText(self.x, self.y, self.usingMove)
			self.previousSpeed = self.speed
			self.speed = 0.25
			ttl = 300
			self.activeHitboxList.append(Sandstorm(self.x, self.y, self.size, 25, ttl))
		

		elif self.usingMoveTimer == 1:
			self.speed = self.previousSpeed
		self.usingMoveTimer -= 1
		if self.usingMoveTimer == 0:
			self.usingMove = ""



	def useEarthquake(self):
		if self.usingMoveTimer == 60:
			self.moveText = MoveText(self.x, self.y, self.usingMove)
			self.previousSpeed = self.speed
			self.speed = 0.1
		ttl = 60
		if self.usingMoveTimer % 20 == 0:
			self.activeHitboxList.append(Earthquake(self.x, self.y, self.size, 25, ttl))

		elif self.usingMoveTimer == 1:
			self.speed = self.previousSpeed
		self.usingMoveTimer -= 1
		if self.usingMoveTimer == 0:
			self.usingMove = ""

	def useDazzlingGleam(self):
		if self.usingMoveTimer == 60:
			self.moveText = MoveText(self.x, self.y, self.usingMove)
			self.previousSpeed = self.speed
			self.speed = 0.25
		ttl = 60
		if self.usingMoveTimer == 60:
			self.activeHitboxList.append(DazzlingGleam(self.x, self.y, self.size, 30, ttl))

		elif self.usingMoveTimer == 1:
			self.speed = self.previousSpeed
		self.usingMoveTimer -= 1
		if self.usingMoveTimer == 0:
			self.usingMove = ""
		
	def useIronTail(self):
		if self.usingMoveTimer == 90:
			self.moveText = MoveText(self.x, self.y, self.usingMove)
			self.ironTailRotation = 0
			self.iFrames = 60
		ttl = 2
		self.activeHitboxList.append(IronTail(self.x, self.y, self.size, self.size + 110, ttl, self.ironTailRotation))
		self.ironTailRotation += 20
		
		self.usingMoveTimer -= 1
		if self.usingMoveTimer == 0:
			self.usingMove = ""

	def useIronHead(self):
		if self.usingMoveTimer == 30:
			self.moveText = MoveText(self.x, self.y, self.usingMove)
		ttl = 2
		if self.usingMoveTimer == 30:
			self.previousSpeed = self.speed
			self.speed = 12
		elif self.usingMoveTimer == 1:
			self.speed = self.previousSpeed
		self.activeHitboxList.append(IronHead(self.x, self.y, self.size, self.size + 45, self.xVel, self.yVel, ttl))
		self.usingMoveTimer -= 1
		if self.usingMoveTimer == 0:
			self.usingMove = ""

	def useZenHeadbutt(self):
		if self.usingMoveTimer == 60:
			self.moveText = MoveText(self.x, self.y, self.usingMove)
		ttl = 4
		if self.usingMoveTimer == 60:
			self.previousSpeed = self.speed
			self.speed = 11
		elif self.usingMoveTimer == 1:
			self.speed = self.previousSpeed
		self.activeHitboxList.append(ZenHeadbutt(self.x, self.y, self.size, self.size + 45, self.xVel, self.yVel, ttl))
		self.usingMoveTimer -= 1
		if self.usingMoveTimer == 0:
			self.usingMove = ""


	def useWaterfall(self):
		if self.usingMoveTimer == 60:
			self.moveText = MoveText(self.x, self.y, self.usingMove)
		ttl = 10
		if self.usingMoveTimer == 50:
			self.previousSpeed = self.speed
			self.speed = 8
		elif self.usingMoveTimer == 1:
			self.speed = self.previousSpeed
		self.activeHitboxList.append(Waterfall(self.x, self.y, self.size, self.size + 45, self.xVel, self.yVel, ttl))
		self.usingMoveTimer -= 1
		if self.usingMoveTimer == 0:
			self.usingMove = ""



	def useCloseCombat(self):
		if self.usingMoveTimer == 45:
			self.moveText = MoveText(self.x, self.y, self.usingMove)
		ttl = 45
		if self.usingMoveTimer % 5 == 0:
			xOffset = random.randint(-80, 80)
			yOffset = random.randint(-80, 80)
			self.activeHitboxList.append(CloseCombat(self.x + xOffset + self.xVel * 70, self.y + yOffset + self.yVel * 70, self.size, self.size + 15, ttl))
		self.usingMoveTimer -= 1
		if self.usingMoveTimer == 0:
			self.usingMove = ""


		

	
