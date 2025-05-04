import pygame
import sys
import random
import pygame.freetype
import pygame.locals
import requests
from pygame.locals import QUIT
from src.debug import showHitboxes, showCollisionBoxes, overrideBattlers, battlerOverride
from src.constants import WINDOW_HEIGHT, WINDOW_WIDTH, BACKGROUND, API, startTimer
from src.globals import g
from src.poke import chooseChars
from src.sprite_loader import INSTANCE as sprites
from src.sets import Sets


class Game:
    def __init__(self):
        self.fontStart = pygame.freetype.SysFont('vcr osd mono', 50)
        self.font = pygame.freetype.SysFont('vcr osd mono', 25)
        self.url = "http://127.0.0.1:5000"
        self.gameStart = False
        self.startCountdown = startTimer
        self.initialized = False
        self.gameOver = False
        self.winner = ""
        self.result = ""
        self.endScreenCountdown = 0
        self.gameOverCountdown = 30
        self.gambling = False
        self.id = 0
        self.timer = 0
        self.wallModifier = 0
        self.wallGrowth = 0.01
        self.wallMaxSize = 300
        self.walls = []

    def newGame(self):
        self.charList = []
        for char in Sets.sets.keys():
            self.charList.append(Sets.get(char))

        if overrideBattlers:
            self.charList = []
            for set_id in battlerOverride:
                self.charList.append(Sets.get(set_id))
        else:
            self.charList = chooseChars(self.charList, random.randint(3, 10))

        print([char.name for char in self.charList])

        self.id = random.randint(10000, 99999)

        if API: requests.post(self.url + "/setfighters", json={"fighters": [char.name for char in self.charList]})
        if API: requests.post(self.url + "/setgameid", json={"id": self.id})

        self.gambling = True
        if API: requests.post(self.url + "/setgambling", json={"openGambling": self.gambling})
        self.initialized = True

    def displayResult(self):
        if self.result == "draw":
            text_surf2, text_rect2 = self.fontStart.render("DRAW!", (0, 0, 0))
            g.window.blit(text_surf2, (WINDOW_WIDTH/2 - 450, WINDOW_HEIGHT/2 - 75))
        elif self.result == "win":
            text_surf2, text_rect2 = self.fontStart.render(self.winner.upper() + " WINS!", (0, 0, 0))
            g.window.blit(text_surf2, (WINDOW_WIDTH/2 - 450, WINDOW_HEIGHT/2 - 75))

    def render(self):
        # Render elements of the game
        g.window.fill(BACKGROUND)

        bgrect = pygame.Rect(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)

        g.window.blit(sprites.get_arena(), bgrect)

        wallleft = pygame.Rect((0, 0, 50 + self.wallModifier, 800))
        wallright = pygame.Rect((1400 - self.wallModifier, 0, 51 + self.wallModifier, 800))
        walltop = pygame.Rect((0, 0, 1450, 50 + self.wallModifier))
        walldown = pygame.Rect((0, 750 - self.wallModifier, 1450, 51 + self.wallModifier))

        self.walls = [wallleft, wallright, walltop, walldown]

        for wall in self.walls:
            pygame.draw.rect(g.window, (20, 10, 20), wall)

    # The main game loop
    def update(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        self.render()

        if self.startCountdown != 0:
            self.startCountdown -= 1

            if not self.initialized:
                self.newGame()

            for char in self.charList:
                charrect = pygame.Rect((char.x, char.y, char.size, char.size))
                charrectImage = pygame.Rect((char.x-60, char.y-85, char.size, char.size))

                g.window.blit(pygame.transform.flip(char.image, False, False), charrectImage)
            text_surf2, text_rect2 = self.fontStart.render("Place Your Bets. Starting in " + str(self.startCountdown//60), (0, 0, 0))
            g.window.blit(text_surf2, (WINDOW_WIDTH/2 - 450, WINDOW_HEIGHT/2 - 75))

        elif self.endScreenCountdown != 0:
            self.endScreenCountdown -= 1
            self.displayResult()

        elif self.endScreenCountdown == 0 and self.result != "":
            self.gameStart = False

            self.startCountdown = startTimer

            self.gameInitialized = False

            self.gameOver = False
            self.gameOverCountdown = 30

            self.wallModifier = 0

            self.result = ""
            self.winner = ""

            for char in self.charList:
                char.restart()

        else:
            if self.gambling:
                self.gambling = False
                if API: requests.post(self.url + "/setgambling", json={"openGambling": self.gambling})

            if self.wallModifier < self.wallMaxSize:
                self.wallModifier += self.wallGrowth

            self.alivelist = []
            for char in self.charList:
                char.move(char.speed)
                if char.alive:
                    self.alivelist.append(char.name)

                    if char.x > WINDOW_WIDTH or char.x < 0:
                        print(char.name, "had a woopsie on the x axis")
                        char.x = WINDOW_WIDTH//2
                    if char.y > WINDOW_HEIGHT or char.y < 0:
                        print(char.name, "had a woopsie on the y axis")
                        char.y = WINDOW_HEIGHT//2

                    charrect = pygame.Rect((char.x, char.y, char.size, char.size))
                    charrectImage = pygame.Rect((char.x-60, char.y-85, char.size, char.size))

                    if char.xVel < 0:
                        g.window.blit(pygame.transform.flip(char.image, False, False), charrectImage)
                    elif char.xVel > 0:
                        g.window.blit(pygame.transform.flip(char.image, True, False), charrectImage)

                    otherChars = []
                    for nestedChar in self.charList:
                        if nestedChar.alive:
                            if nestedChar != char:
                                otherChars.append(pygame.Rect((nestedChar.x, nestedChar.y, nestedChar.size, nestedChar.size)))

                    obstacleList = self.walls + otherChars

                    charLeftBox = pygame.Rect(
                        (
                            char.x + char.leftDetectBox.xOffset,
                            char.y + char.leftDetectBox.yOffset,
                            char.leftDetectBox.width,
                            char.leftDetectBox.height
                        )
                    )
                    charRightBox = pygame.Rect(
                        (
                            char.x + char.rightDetectBox.xOffset,
                            char.y + char.rightDetectBox.yOffset,
                            char.rightDetectBox.width,
                            char.rightDetectBox.height
                        )
                    )
                    charUpBox = pygame.Rect(
                        (
                            char.x + char.upDetectBox.xOffset,
                            char.y + char.upDetectBox.yOffset,
                            char.upDetectBox.width,
                            char.upDetectBox.height
                        )
                    )
                    charDownBox = pygame.Rect(
                        (
                            char.x + char.downDetectBox.xOffset,
                            char.y + char.downDetectBox.yOffset,
                            char.downDetectBox.width,
                            char.downDetectBox.height
                        )
                    )

                    if showCollisionBoxes:
                        pygame.draw.rect(g.window, (255, 0, 0), charLeftBox)
                        pygame.draw.rect(g.window, (255, 0, 0), charRightBox)
                        pygame.draw.rect(g.window, (255, 0, 0), charUpBox)
                        pygame.draw.rect(g.window, (255, 0, 0), charDownBox)

                    if charLeftBox.collidelist(obstacleList) != -1:
                        char.collideLeft()
                    if charRightBox.collidelist(obstacleList) != -1:
                        char.collideRight()
                    if charUpBox.collidelist(obstacleList) != -1:
                        char.collideTop()
                    if charDownBox.collidelist(obstacleList) != -1:
                        char.collideBottom()

                    char.useMove()

                    healthRectRed = pygame.Rect(
                        (
                            char.healthBox.xOffset + char.x,
                            char.y - char.healthBox.yOffset,
                            char.healthBox.width,
                            char.healthBox.height
                        )
                    )

                    healthPercentWidth = (char.health / 300) * char.healthBox.width

                    healthRectGreen = pygame.Rect((char.healthBox.xOffset + char.x,
                        char.y - char.healthBox.yOffset, healthPercentWidth,
                        char.healthBox.height))
                    pygame.draw.rect(g.window, (175, 0, 0), healthRectRed)
                    pygame.draw.rect(g.window, (0, 175, 0), healthRectGreen)

            if len(self.alivelist) <= 1 and self.gameOverCountdown == 30:
                self.gameOver = True

            moveRects = []
            for char in self.charList:
                stillAliveHitboxes = []
                for move in char.activeHitboxList:
                    move.move()
                    moveRects.append([pygame.Rect((move.x, move.y, move.size, move.size)), move])
                    if move.ttl > 0:
                        stillAliveHitboxes.append(move)

                char.activeHitboxList = stillAliveHitboxes

                for char in self.charList:
                    otherCharsHitboxes = []
                    otherCharsValues = []
                    for nestedChar in self.charList:
                        if nestedChar != char:
                            for hitbox in nestedChar.activeHitboxList:
                                otherCharsHitboxes.append(pygame.Rect((hitbox.x, hitbox.y, hitbox.size, hitbox.size)))
                                otherCharsValues.append(hitbox)
                    if char.iFrames == 0:
                        charrect = pygame.Rect((char.x, char.y, char.size, char.size))
                        if charrect.collidelist(otherCharsHitboxes) != -1:
                            char.iFrames = 180
                            char.takeDamage(otherCharsValues[charrect.collidelist(otherCharsHitboxes)].damage)

            for moveRect in moveRects:
                if showHitboxes:
                    pygame.draw.rect(g.window, moveRect[1].colour, moveRect[0])
                if moveRect[1].graphic == "image":
                    moveImage = sprites.moves.get(moveRect[1].image)
                    if moveImage is None:
                        raise Exception("Move image is <None>! "+moveRect[1].image)
                    moveImage = pygame.transform.scale(moveImage, (moveRect[1].size, moveRect[1].size))
                    if moveImage is None:
                        print("Move image is <None>! "+moveRect[1].image)

                    rotatedImage = pygame.transform.rotate(moveImage, moveRect[1].rotate)

                    new_rect = rotatedImage.get_rect(
                        center = moveImage.get_rect(
                            center=(
                                moveRect[1].x + moveRect[1].size/2,
                                moveRect[1].y + moveRect[1].size/2
                            )
                        ).center
                    )

                    g.window.blit(rotatedImage, new_rect)
                elif moveRect[1].graphic == "rect":
                    pygame.draw.rect(g.window, moveRect[1].colour, moveRect[0])

                elif moveRect[1].graphic == "circle":
                    pygame.draw.circle(g.window, moveRect[1].colour, moveRect[0].center, moveRect[1].size/2)

            for char in self.charList:
                if char.moveText:
                    if char.moveText.ttl > 0:
                        text_surf2, text_rect2 = self.font.render(char.moveText.text, (0, 0, 0, char.moveText.alpha))
                        g.window.blit(text_surf2, (char.moveText.x - 48, char.moveText.y - 8))
                        text_surf2, text_rect2 = self.font.render(char.moveText.text, (255, 255, 255, char.moveText.alpha))
                        g.window.blit(text_surf2, (char.moveText.x - 50, char.moveText.y - 10))
                    char.moveText.tick()
                newDamageIndictators = []
                for indic in char.damageIndicators:
                    indic.move()
                    text_surf2, text_rect2 = self.font.render(indic.damage, (255, 0, 0, indic.alpha))
                    g.window.blit(text_surf2, (indic.x, indic.y + 10))
                    if indic.ttl >= 0:
                        newDamageIndictators.append(indic)
                char.damageIndicators = newDamageIndictators

            if self.gameOver:
                self.gameOverCountdown -= 1

            if self.gameOverCountdown == 0:
                if len(self.alivelist) == 0:
                    self.result = "draw"
                    if API: requests.post(self.url + "/setwinner", json={"winner": "Nobody"})
                if len(self.alivelist) == 1:
                    self.result = "win"
                    self.winner = self.alivelist[0]
                    if API: requests.post(self.url + "/setwinner", json={"winner": self.winner})
                self.endScreenCountdown = 240
