import random
import pygame.transform
from math import sqrt
from pygame import Rect
from src.moves import Moves, Move
from src import physics
from src.constants import WINDOW_HEIGHT, WINDOW_WIDTH
from src.globals import g
from src.debug import showCollisionBoxes

charSpeed = 0.8

def chooseChars(charList, charNum):
	chars = []
	charList = charList + []
	while charNum > 0:
		pick = random.randint(0, len(charList) - 1)
		chars.append(charList[pick])
		charList.pop(pick)
		charNum -= 1
	return chars

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


class Poke(physics.PhysicsObject):
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
	moveText = ""
	damageIndicators = []

	def __init__(self, x, y, image = "", moveset = [], name = "", size = 60, health = 300):
		super().__init__(x, y, size, size)
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
			if self.xVel != 0 or self.yVel != 0: #update velocity based on speed
				speed = sqrt(self.xVel**2 + self.yVel**2)
				direction = (self.xVel/speed, self.yVel/speed)
				self.xVel = direction[0] * self.speed
				self.yVel = direction[1] * self.speed
			super().update()

			if self.iFrames > 0:
				self.iFrames -= 1
			
			if self.x > WINDOW_WIDTH or self.x < 0:
				print(self.name, "had a woopsie on the x axis")
				self.x = WINDOW_WIDTH//2
			if self.y > WINDOW_HEIGHT or self.y < 0:
				print(self.name, "had a woopsie on the y axis")
				self.y = WINDOW_HEIGHT//2
		
			self.useMove()
	
	def draw(self):
		if self.alive:
			if showCollisionBoxes:
				pygame.draw.rect(g.window, (200, 0, 0, 50), self.getCollider())
			rectImage = Rect((self.x-60, self.y-85, self.size, self.size))
			g.window.blit(pygame.transform.flip(self.image, self.xVel > 0, False), rectImage)

			healthRectRed = pygame.Rect(self.x + self.size / 2 - 25, self.y + 10, 50, 10)
			healthPercentWidth = (self.health / 300) * 50
			healthRectGreen = pygame.Rect(self.x + self.size / 2 - 25, self.y + 10, healthPercentWidth, 10)

			pygame.draw.rect(g.window, (175,0,0), healthRectRed)
			pygame.draw.rect(g.window, (0,175,0), healthRectGreen)

	def restart(self):
		self.health = self.maxHealth
		self.velStart()
		self.alive = True
		self.checksCollision = True
		self.setMoveTimer()
		self.usingMoveTimer = 0
		self.usingMove = ""
		self.iFrames = 0
		self.speed = charSpeed
		self.x = self.startingX
		self.y = self.startingY

	def setMoveTimer(self):
		return 130 + random.randint(1,200)

	def velStart(self):
		self.xVel = round(random.uniform(-1,1)) * self.speed
		self.yVel = round(1 - abs(self.xVel), 3) * random.choice([-1,1]) * self.speed
	
	def collide(self, other, direction):
		if isinstance(other, Move):
			if self.iFrames == 0 and other.poke != self:
				self.takeDamage(other.damage)
				self.iFrames = 180
			return
		if self.usingMove == "U Turn":
			self.xVel *= -1
			self.yVel *= -1
		elif random.random() < 2/3:
			if direction == "top":
				self.y -= other.getCollider().clip(self.getCollider()).height
				self.yVel *= -1
				if self.xVel < 0:
					self.xVel = round(1 - abs(self.yVel), 3) * -self.speed
				else:
					self.xVel = round(1 - abs(self.yVel), 3) * self.speed
			if direction == "bottom":
				self.y += other.getCollider().clip(self.getCollider()).height
				self.yVel *= -1
				if self.xVel < 0:
					self.xVel = round(1 - abs(self.yVel), 3) * -self.speed
				else:
					self.xVel = round(1 - abs(self.yVel), 3) * self.speed
			elif direction == "left":
				self.x += other.getCollider().clip(self.getCollider()).width
				self.xVel *= -1
				if self.yVel < 0:
					self.yVel = round(1 - abs(self.xVel), 3) * -self.speed
				else:
					self.yVel = round(1 - abs(self.xVel), 3) * self.speed
			elif direction == "right":
				self.x -= other.getCollider().clip(self.getCollider()).width
				self.xVel *= -1
				if self.yVel < 0:
					self.yVel = round(1 - abs(self.xVel), 3) * -self.speed
				else:
					self.yVel = round(1 - abs(self.xVel), 3) * self.speed
		else:
			self.velStart()

	def takeDamage(self, damage):
		self.health -= damage
		self.damageIndicators.append(DamageIndicator(self.x, self.y, damage))

		if self.health <= 0:
			self.alive = False
			self.checksCollision = False

	def useMove(self):
		if self.moveTimer <= 0:
			self.moveTimer = self.setMoveTimer()
			self.velStart()
			self.usingMove = random.choice(self.moveset)
			
		else:
			self.moveTimer -= 1

		if self.usingMove != "":
			move = Moves.list.get(self.usingMove)
			if self.usingMoveTimer <= 0:
				self.usingMoveTimer = move.usingTime
			move.use(self)