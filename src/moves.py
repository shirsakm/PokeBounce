import math, random

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


class QuickAttack:
	type = "normal"
	colour = (175, 175, 175)
	damage = 25
	rotate = 0
	graphic = "circle"
	usingTime = 120

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
		
	@staticmethod
	def use(poke):
		if poke.usingMoveTimer == 120:
			poke.moveText = MoveText(poke.x, poke.y, poke.usingMove)
		ttl = 15
		if poke.usingMoveTimer == 120:
			poke.previousSpeed = poke.speed
			poke.speed = 16
		elif poke.usingMoveTimer == 1:
			poke.speed = poke.previousSpeed
		poke.activeHitboxList.append(QuickAttack(poke.x, poke.y, poke.size, poke.size + 25, ttl))
		poke.usingMoveTimer -= 1
		if poke.usingMoveTimer == 0:
			poke.usingMove = ""
        

class BraveBird:
	type = "flying"
	colour = (185, 224, 239)
	damage = 55
	rotate = 0
	graphic = "image"
	usingTime = 90

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

	@staticmethod
	def use(poke):
		if poke.usingMoveTimer == 90:
			poke.moveText = MoveText(poke.x, poke.y, poke.usingMove)
		ttl = 25
		if poke.usingMoveTimer == 90:
			poke.previousSpeed = poke.speed
			poke.speed = 12
		elif poke.usingMoveTimer == 1:
			poke.speed = poke.previousSpeed
		poke.activeHitboxList.append(BraveBird(poke.x, poke.y, poke.size, poke.size + 80, poke.xVel, poke.yVel, ttl))
		poke.usingMoveTimer -= 1
		if poke.usingMoveTimer == 0:
			poke.usingMove = ""


class IronHead:
	type = "steel"
	colour = (185, 224, 239)
	damage = 45
	rotate = 0
	graphic = "image"
	usingTime = 30

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
	
	@staticmethod
	def use(poke):
		if poke.usingMoveTimer == 30:
			poke.moveText = MoveText(poke.x, poke.y, poke.usingMove)
		ttl = 2
		if poke.usingMoveTimer == 30:
			poke.previousSpeed = poke.speed
			poke.speed = 12
		elif poke.usingMoveTimer == 1:
			poke.speed = poke.previousSpeed
		poke.activeHitboxList.append(IronHead(poke.x, poke.y, poke.size, poke.size + 45, poke.xVel, poke.yVel, ttl))
		poke.usingMoveTimer -= 1
		if poke.usingMoveTimer == 0:
			poke.usingMove = ""



class ZenHeadbutt:
	type = "psychic"
	colour = (185, 224, 239)
	damage = 30
	rotate = 0
	graphic = "image"
	usingTime = 60

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

	@staticmethod
	def use(poke):
		if poke.usingMoveTimer == 60:
			poke.moveText = MoveText(poke.x, poke.y, poke.usingMove)
		ttl = 4
		if poke.usingMoveTimer == 60:
			poke.previousSpeed = poke.speed
			poke.speed = 11
		elif poke.usingMoveTimer == 1:
			poke.speed = poke.previousSpeed
		poke.activeHitboxList.append(ZenHeadbutt(poke.x, poke.y, poke.size, poke.size + 45, poke.xVel, poke.yVel, ttl))
		poke.usingMoveTimer -= 1
		if poke.usingMoveTimer == 0:
			poke.usingMove = ""

class Waterfall:
	type = "water"
	colour = (185, 224, 239)
	damage = 35
	rotate = 0
	graphic = "image"
	usingTime = 60

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

	@staticmethod
	def use(poke):
		if poke.usingMoveTimer == 60:
			poke.moveText = MoveText(poke.x, poke.y, poke.usingMove)
		ttl = 10
		if poke.usingMoveTimer == 50:
			poke.previousSpeed = poke.speed
			poke.speed = 8
		elif poke.usingMoveTimer == 1:
			poke.speed = poke.previousSpeed
		poke.activeHitboxList.append(Waterfall(poke.x, poke.y, poke.size, poke.size + 45, poke.xVel, poke.yVel, ttl))
		poke.usingMoveTimer -= 1
		if poke.usingMoveTimer == 0:
			poke.usingMove = ""


class CloseCombat:
	type = "fighting"
	colour = (185, 224, 239)
	damage = 35
	rotate = 0
	graphic = "image"
	usingTime = 45

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

	@staticmethod
	def use(poke):
		if poke.usingMoveTimer == 45:
			poke.moveText = MoveText(poke.x, poke.y, poke.usingMove)
		ttl = 45
		if poke.usingMoveTimer % 5 == 0:
			xOffset = random.randint(-80, 80)
			yOffset = random.randint(-80, 80)
			poke.activeHitboxList.append(CloseCombat(poke.x + xOffset + poke.xVel * 70, poke.y + yOffset + poke.yVel * 70, poke.size, poke.size + 15, ttl))
		poke.usingMoveTimer -= 1
		if poke.usingMoveTimer == 0:
			poke.usingMove = ""


class DarkPulse:
	type = "dark"
	colour = (185, 224, 239)
	damage = 30
	rotate = 0
	graphic = "image"
	rotate = 0
	usingTime = 60

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
	
	@staticmethod
	def use(poke):
		if poke.usingMoveTimer == 60:
			poke.moveText = MoveText(poke.x, poke.y, poke.usingMove)
			poke.previousSpeed = poke.speed
			poke.speed = 0.25
		ttl = 45
		if poke.usingMoveTimer % 20 == 0:
			poke.activeHitboxList.append(DarkPulse(poke.x, poke.y, poke.size, 25, ttl))

		elif poke.usingMoveTimer == 1:
			poke.speed = poke.previousSpeed
		poke.usingMoveTimer -= 1
		if poke.usingMoveTimer == 0:
			poke.usingMove = ""



class Sandstorm:
	type = "rock"
	colour = (185, 224, 239)
	damage = 15
	rotate = 0
	graphic = "image"
	rotate = 0
	usingTime = 20

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

	@staticmethod
	def use(poke):
		if poke.usingMoveTimer == 20:
			poke.moveText = MoveText(poke.x, poke.y, poke.usingMove)
			poke.previousSpeed = poke.speed
			poke.speed = 0.25
			ttl = 300
			poke.activeHitboxList.append(Sandstorm(poke.x, poke.y, poke.size, 25, ttl))
		

		elif poke.usingMoveTimer == 1:
			poke.speed = poke.previousSpeed
		poke.usingMoveTimer -= 1
		if poke.usingMoveTimer == 0:
			poke.usingMove = ""


class Earthquake:
	type = "ground"
	colour = (185, 224, 239)
	damage = 60
	rotate = 0
	graphic = "image"
	rotate = 0
	usingTime = 60

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
	
	@staticmethod
	def use(poke):
		if poke.usingMoveTimer == 60:
			poke.moveText = MoveText(poke.x, poke.y, poke.usingMove)
			poke.previousSpeed = poke.speed
			poke.speed = 0.1
		ttl = 60
		if poke.usingMoveTimer % 20 == 0:
			poke.activeHitboxList.append(Earthquake(poke.x, poke.y, poke.size, 25, ttl))

		elif poke.usingMoveTimer == 1:
			poke.speed = poke.previousSpeed
		poke.usingMoveTimer -= 1
		if poke.usingMoveTimer == 0:
			poke.usingMove = ""


class DazzlingGleam:
	type = "fairy"
	colour = (185, 224, 239)
	damage = 30
	rotate = 0
	graphic = "image"
	rotate = 0
	usingTime = 90

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

	@staticmethod
	def use(poke):
		if poke.usingMoveTimer == 60:
			poke.moveText = MoveText(poke.x, poke.y, poke.usingMove)
			poke.previousSpeed = poke.speed
			poke.speed = 0.25
		ttl = 60
		if poke.usingMoveTimer == 60:
			poke.activeHitboxList.append(DazzlingGleam(poke.x, poke.y, poke.size, 30, ttl))

		elif poke.usingMoveTimer == 1:
			poke.speed = poke.previousSpeed
		poke.usingMoveTimer -= 1
		if poke.usingMoveTimer == 0:
			poke.usingMove = ""

class IronTail:
	type = "steel"
	colour = (185, 224, 239)
	damage = 30
	rotate = 0
	graphic = "image"

	image = "irontail"
	usingTime = 90

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

	@staticmethod
	def use(poke):
		if poke.usingMoveTimer == 90:
			poke.moveText = MoveText(poke.x, poke.y, poke.usingMove)
			poke.ironTailRotation = 0
			poke.iFrames = 60
		ttl = 2
		poke.activeHitboxList.append(IronTail(poke.x, poke.y, poke.size, poke.size + 110, ttl, poke.ironTailRotation))
		poke.ironTailRotation += 20
		
		poke.usingMoveTimer -= 1
		if poke.usingMoveTimer == 0:
			poke.usingMove = ""

class UTurn:
	type = "bug"
	colour = (30, 175, 30)
	damage = 15
	rotate = 0
	graphic = "circle"
	usingTime = 120
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

	@staticmethod
	def use(poke):
		if poke.usingMoveTimer == 120:
			poke.moveText = MoveText(poke.x, poke.y, poke.usingMove)
		ttl = 20
		if poke.usingMoveTimer == 120:
			poke.iFrames = 120
			poke.previousSpeed = poke.speed
			poke.speed = -12
		elif poke.usingMoveTimer == 1:
			poke.speed = poke.previousSpeed
		poke.activeHitboxList.append(UTurn(poke.x, poke.y, poke.size, poke.size + 25, ttl))
		poke.usingMoveTimer -= 1
		if poke.usingMoveTimer == 0:
			poke.usingMove = ""

class Bolt:
	type = "electric"
	graphic = "rect"
	damage = 40
	boltRects = []
	colour = (251, 225, 13, 10)

	usingTime = 60

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

	@staticmethod
	def use(poke):
		
		if poke.usingMoveTimer == 60:
			poke.moveText = MoveText(poke.x, poke.y, poke.usingMove)
		speed = 40
		size = 40
		ttl = 90 - (60 - poke.usingMoveTimer)
		if poke.boltShift == 0 and poke.boltShiftCooldown == 0:
			poke.boltShift = random.choice([0,0,0,0,4])

		if poke.usingMoveTimer == 60:
			bolt = Bolt(poke.x, poke.y, poke.xVel, poke.yVel, poke.size, size, ttl, True)
			poke.activeHitboxList.append(bolt)
			poke.xVelUnshift = poke.xVel
			poke.yVelUnshift = poke.yVel
		elif poke.usingMoveTimer > 0:
			lastHitbox = poke.activeHitboxList[-1]
			if poke.boltShift == 0:
				boltX = lastHitbox.x + lastHitbox.xVel * speed
				boltY = lastHitbox.y + lastHitbox.yVel * speed
				poke.xVelUnshift = lastHitbox.xVel
				poke.yVelUnshift = lastHitbox.yVel
			
			elif poke.boltShift == 1:
				boltX = lastHitbox.x + poke.xVelUnshift * speed
				boltY = lastHitbox.y + poke.yVelUnshift * speed
				poke.boltShiftCooldown = 10

			else:
				boltX = lastHitbox.x + lastHitbox.yVel * speed
				boltY = lastHitbox.y + lastHitbox.xVel * speed

			bolt = Bolt(boltX, boltY, lastHitbox.xVel, lastHitbox.yVel, poke.size, size, ttl)
			poke.activeHitboxList.append(bolt)
		poke.usingMoveTimer -= 1
		if poke.usingMoveTimer == 0:
			poke.usingMove = ""
		if poke.boltShift:
			poke.boltShift -= 1
		if poke.boltShiftCooldown:
			poke.boltShiftCooldown -= 1

class DragonPulse:
	type = "dragon"
	graphic = "circle"
	damage = 40
	boltRects = []
	colours = [(251, 20, 250), (129, 10, 250)]
	usingTime = 60

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

	@staticmethod
	def use(poke):
		if poke.usingMoveTimer == 60:
			poke.moveText = MoveText(poke.x, poke.y, poke.usingMove)
		speed = 25
		size = 40 + (60 - poke.usingMoveTimer)
		ttl = 90 - (60 - poke.usingMoveTimer)
		poke.dragonPulseColour = (poke.dragonPulseColour + 1) % 2

		if poke.usingMoveTimer == 60:
			bolt = DragonPulse(poke.x, poke.y, poke.xVel, poke.yVel, poke.size, size, ttl, True, poke.dragonPulseColour)
			poke.activeHitboxList.append(bolt)
			poke.xVelUnshift = poke.xVel
			poke.yVelUnshift = poke.yVel
		elif poke.usingMoveTimer > 0:
			lastHitbox = poke.activeHitboxList[-1]
			boltX = lastHitbox.x + lastHitbox.xVel * speed
			boltY = lastHitbox.y + lastHitbox.yVel * speed
			bolt = DragonPulse(boltX, boltY, lastHitbox.xVel, lastHitbox.yVel, poke.size, size, ttl, False, poke.dragonPulseColour)
			poke.activeHitboxList.append(bolt)
		poke.usingMoveTimer -= 1
		if poke.usingMoveTimer == 0:
			poke.usingMove = ""


class HyperBeam:
	type = "normal"
	graphic = "circle"
	damage = 50
	boltRects = []
	colours = [(255, 183, 0), (255, 221, 0)]

	usingTime = 60

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

	@staticmethod
	def use(poke):
		
		if poke.usingMoveTimer == 60:
			poke.moveText = MoveText(poke.x, poke.y, poke.usingMove)
		speed = 25
		size = 40 + ((60 - poke.usingMoveTimer) * 2)
		ttl = 90 - (60 - poke.usingMoveTimer)
		poke.dragonPulseColour = (poke.dragonPulseColour + 1) % 2

		if poke.usingMoveTimer == 60:
			bolt = HyperBeam(poke.x, poke.y, poke.xVel, poke.yVel, poke.size, size, ttl, True, poke.dragonPulseColour)
			poke.activeHitboxList.append(bolt)
			poke.xVelUnshift = poke.xVel
			poke.yVelUnshift = poke.yVel
			poke.previousSpeed = poke.speed
			poke.speed = 0
		elif poke.usingMoveTimer > 0:
			lastHitbox = poke.activeHitboxList[-1]
			boltX = lastHitbox.x + lastHitbox.xVel * speed
			boltY = lastHitbox.y + lastHitbox.yVel * speed
			bolt = HyperBeam(boltX, boltY, lastHitbox.xVel, lastHitbox.yVel, poke.size, size, ttl, False, poke.dragonPulseColour)
			poke.activeHitboxList.append(bolt)
		poke.usingMoveTimer -= 1
		if poke.usingMoveTimer == 0:
			poke.moveTimer = 300
			poke.speed = poke.previousSpeed
			poke.usingMove = ""


class IceBeam:
	type = "ice"
	graphic = "rect"
	damage = 40
	boltRects = []
	colour = (125, 205, 236)

	usingTime = 60

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

	@staticmethod
	def use(poke):
		if poke.usingMoveTimer == 60:
			poke.moveText = MoveText(poke.x, poke.y, poke.usingMove)
		speed = 40
		size = 40
		ttl = 90  - (60 - poke.usingMoveTimer)
		if poke.boltShift == 0 and poke.boltShiftCooldown == 0:
			poke.boltShift = random.choice([0,0,0,0,0,3,-3])

		if poke.usingMoveTimer == 60:
			bolt = IceBeam(poke.x, poke.y, poke.xVel, poke.yVel, poke.size, size, ttl, True)
			poke.activeHitboxList.append(bolt)
			poke.xVelUnshift = poke.xVel
			poke.yVelUnshift = poke.yVel
		elif poke.usingMoveTimer > 0:
			lastHitbox = poke.activeHitboxList[-1]
			if poke.boltShift == 0:
				boltX = lastHitbox.x + lastHitbox.xVel * speed
				boltY = lastHitbox.y + lastHitbox.yVel * speed
				poke.xVelUnshift = lastHitbox.xVel
				poke.yVelUnshift = lastHitbox.yVel
			
			elif poke.boltShift == 1:
				boltX = lastHitbox.x + poke.xVelUnshift * speed
				boltY = lastHitbox.y + poke.yVelUnshift * speed
				poke.boltShiftCooldown = 5

			else:
				boltX = lastHitbox.x + lastHitbox.yVel * speed
				boltY = lastHitbox.y + lastHitbox.xVel * speed

			bolt = IceBeam(boltX, boltY, lastHitbox.xVel, lastHitbox.yVel, poke.size, size, ttl)
			poke.activeHitboxList.append(bolt)
		poke.usingMoveTimer -= 1
		if poke.usingMoveTimer == 0:
			poke.usingMove = ""
		if poke.boltShift > 0:
			poke.boltShift -= 1
		elif poke.boltShift < 0:
			poke.boltShift += 1
		if poke.boltShiftCooldown:
			poke.boltShiftCooldown -= 1



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

	usingTime = 30

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

	@staticmethod
	def use(poke):
		if poke.usingMoveTimer == 30:
			poke.moveText = MoveText(poke.x, poke.y, poke.usingMove)
		poke.usingMoveTimer -= 1
		if poke.usingMoveTimer == 29:
			ball = ShadowBall(poke.x, poke.y, poke.xVel, poke.yVel, poke.size, 12)
			poke.activeHitboxList.append(ball)
		if poke.usingMoveTimer == 0:
			poke.usingMove = ""


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

	usingTime = 30

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

	@staticmethod
	def use(poke):
		if poke.usingMoveTimer == 30:
			poke.moveText = MoveText(poke.x, poke.y, poke.usingMove)
		poke.usingMoveTimer -= 1
		if poke.usingMoveTimer == 29:
			ball = StoneEdge(poke.x, poke.y, poke.xVel, poke.yVel, poke.size, 14)
			poke.activeHitboxList.append(ball)
			ball = StoneEdge(poke.x, poke.y, poke.xVel, poke.yVel, poke.size, 14)
			poke.activeHitboxList.append(ball)
			ball = StoneEdge(poke.x, poke.y, poke.xVel, poke.yVel, poke.size, 14)
			poke.activeHitboxList.append(ball)
			ball = StoneEdge(poke.x, poke.y, poke.xVel, poke.yVel, poke.size, 14)
			poke.activeHitboxList.append(ball)
			ball = StoneEdge(poke.x, poke.y, poke.xVel, poke.yVel, poke.size, 14)
			poke.activeHitboxList.append(ball)
		if poke.usingMoveTimer == 0:
			poke.usingMove = ""


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

	usingTime = 30

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
	
	@staticmethod
	def use(poke):
		if poke.usingMoveTimer == 30:
			poke.moveText = MoveText(poke.x, poke.y, poke.usingMove)
		poke.usingMoveTimer -= 1
		if poke.usingMoveTimer % 5 == 0:
			ball = PoisonSting(poke.x, poke.y, poke.xVel, poke.yVel, poke.size, 14)
			poke.activeHitboxList.append(ball)
		if poke.usingMoveTimer == 0:
			poke.usingMove = ""


class Flame:
	type = "fire"
	ttl = 90
	spread = 0.1
	growth = 1.02
	speedDecay = 0.98
	damage = 20
	colour = (255, 102, 0, 30)
	graphic = "image"

	usingTime = 60

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

	@staticmethod
	def use(poke):
		if poke.usingMoveTimer == 60:
			poke.moveText = MoveText(poke.x, poke.y, poke.usingMove)
		poke.usingMoveTimer -= 1
		if poke.usingMoveTimer % 5 == 0:
			flame = Flame(poke.x, poke.y, poke.xVel, poke.yVel, poke.size, 16)
			poke.activeHitboxList.append(flame)
		if poke.usingMoveTimer == 0:
			poke.usingMove = ""

class Bubble:
	type = "water"
	ttl = 120
	spread = 0.15
	growth = 1.01
	speedDecay = 0.97
	damage = 20
	colour = (20, 50, 250, 30)
	graphic = "image"

	usingTime = 45

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

	@staticmethod
	def use(poke):
		if poke.usingMoveTimer == 45:
			poke.moveText = MoveText(poke.x, poke.y, poke.usingMove)
		poke.usingMoveTimer -= 1
		if poke.usingMoveTimer % 5 == 0:
			bubble = Bubble(poke.x, poke.y, poke.xVel, poke.yVel, poke.size, 20)
			poke.activeHitboxList.append(bubble)
		if poke.usingMoveTimer == 0:
			poke.usingMove = ""

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

	usingTime = 45

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

	@staticmethod
	def use(poke):
		if poke.usingMoveTimer == 45:
			poke.moveText = MoveText(poke.x, poke.y, poke.usingMove)
		poke.usingMoveTimer -= 1
		if poke.usingMoveTimer % 7 == 0:
			razorLeaf = RazorLeaf(poke.x, poke.y, poke.xVel, poke.yVel, poke.size, 20)
			poke.activeHitboxList.append(razorLeaf)
		if poke.usingMoveTimer == 0:
			poke.usingMove = ""



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

	usingTime = 120

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

	@staticmethod
	def use(poke):
		if poke.usingMoveTimer == 120:
			poke.moveText = MoveText(poke.x, poke.y, poke.usingMove)
		poke.usingMoveTimer -= 1
		if poke.usingMoveTimer == 119:
			ball = Bonemerang(poke.x, poke.y, poke.xVel, poke.yVel, poke.size, 10)
			poke.activeHitboxList.append(ball)
		if poke.usingMoveTimer == 0:
			poke.usingMove = ""

class Moves:
	list = {
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