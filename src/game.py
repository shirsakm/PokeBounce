import pygame
import sys
import random
import pygame.freetype
import pygame.locals
import requests
from pygame.locals import QUIT
from src.debug import overrideBattlers, battlerOverride
from src.constants import WINDOW_HEIGHT, WINDOW_WIDTH, BACKGROUND, API, startTimer
from src.globals import g
from src.poke import chooseChars
from src.sprite_loader import INSTANCE as sprites
from src.sets import Sets
from src import physics


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
        self.walls = [physics.Wall("right"), physics.Wall("left"), physics.Wall("top"), physics.Wall("bottom")]

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

        if API:
            requests.post(self.url + "/setfighters", json={"fighters": [char.name for char in self.charList]})
        if API:
            requests.post(self.url + "/setgameid", json={"id": self.id})

        self.gambling = True
        if API:
            requests.post(self.url + "/setgambling", json={"openGambling": self.gambling})
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
                charrectImage = pygame.Rect((char.x-60, char.y-85, char.size, char.size))

                g.window.blit(pygame.transform.flip(char.image, False, False), charrectImage)
            text_surf2, text_rect2 = self.fontStart.render(
                "Place Your Bets. Starting in " + str(self.startCountdown//60),
                (0, 0, 0)
            )
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
                if API:
                    requests.post(self.url + "/setgambling", json={"openGambling": self.gambling})

            physics.physicsUpdate()
            self.alivelist = [poke for poke in self.charList if poke.alive]

            if len(self.alivelist) <= 1 and self.gameOverCountdown == 30:
                self.gameOver = True
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
                    if API:
                        requests.post(self.url + "/setwinner", json={"winner": "Nobody"})
                if len(self.alivelist) == 1:
                    self.result = "win"
                    self.winner = self.alivelist[0].name
                    if API:
                        requests.post(self.url + "/setwinner", json = {"winner" : self.winner})
                self.endScreenCountdown = 240
