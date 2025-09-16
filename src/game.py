import pygame, sys, random
import pygame.freetype
from pygame.locals import *
try:
    import requests  # type: ignore
    _requests_available = True
except Exception:
    print("[web] 'requests' module not available, disabling API features.")
    _requests_available = False

from src.config import config
from src.constants import WINDOW_HEIGHT, WINDOW_WIDTH, BACKGROUND, API, startTimer
from src.globals import g
from src.sprite_loader import INSTANCE as sprites
from src.resource_path import resource_path
from src.moves import MOVES
from src import physics, poke


class Game:
    def __init__(self):
        try:
            self.fontStart = pygame.freetype.Font(
                resource_path("assets/font/PixeloidSans.ttf"), 50
            )
            self.font = pygame.freetype.Font(
                resource_path("assets/font/PixeloidSans.ttf"), 25
            )
            self.use_freetype = True
        except Exception as e:
            print(f"Failed to load custom font, using default: {e}")
            # Fallback to regular pygame font for web compatibility
            self.fontStart = pygame.font.Font(None, 50)
            self.font = pygame.font.Font(None, 25)
            self.use_freetype = False
            
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
        self.walls = [
            physics.Wall("right"),
            physics.Wall("left"),
            physics.Wall("top"),
            physics.Wall("bottom"),
        ]
        self.charList = []

    def render_text(self, font, text, color):
        """Helper method to render text with either freetype or regular pygame font"""
        if self.use_freetype:
            return font.render(text, color)
        else:
            # Regular pygame font - only RGB, no alpha
            rgb_color = color[:3] if len(color) > 3 else color
            return font.render(text, True, rgb_color), None

    def moveTest(self):
        sprite = sprites.get_battler("smeargle")
        charList = []
        posList = [(x, y) for x in range(100, WINDOW_WIDTH - 99, 150) for y in range(100, WINDOW_HEIGHT - 99, 150)]
        moveNames = list(MOVES.keys())
        for i in range(len(MOVES)):
            charList.append(
                poke.Poke(
                    posList[i][0],
                    posList[i][1],
                    sprite,
                    [moveNames[i]],
                    moveNames[i] + " Test",
                )
            )
        return charList

    def newGame(self):
        if config["Debug"]["overrideBattlers"]:
            battlerOverride = config["Debug"]["battlerOverride"]
            try:
                self.charList = [poke.allPokemon[i.lower()] for i in battlerOverride]
            except KeyError:
                print("Invalid battler override settings.")
                exit(1)
        elif config["Debug"]["testMoves"]:
            self.charList = self.moveTest()
        else:
            self.charList = poke.chooseChars(list(poke.allPokemon.values()), random.randint(3, 10))

        for wall in self.walls:
            wall.reset()

        for char in self.charList:
            char.revive()

        self.id = random.randint(10000, 99999)

        if API and _requests_available:
            try:
                requests.post(
                    self.url + "/setfighters",
                    json={"fighters": [char.name for char in self.charList]},
                )
                requests.post(self.url + "/setgameid", json={"id": self.id})
            except Exception as e:
                print(f"[web] Failed to send API init data: {e}")

        self.gambling = True
        if API and _requests_available:
            try:
                requests.post(
                    self.url + "/setgambling", json={"openGambling": self.gambling}
                )
            except Exception as e:
                print(f"[web] Failed to set gambling flag: {e}")
        self.initialized = True

    def displayResult(self):
        if self.result == "draw":
            text_surf2, text_rect2 = self.render_text(self.fontStart, "DRAW!", (0, 0, 0))
            g.window.blit(text_surf2, (WINDOW_WIDTH / 2 - 450, WINDOW_HEIGHT / 2 - 75))
        elif self.result == "win":
            text_surf2, text_rect2 = self.render_text(
                self.fontStart, self.winner.upper() + " WINS!", (0, 0, 0)
            )
            g.window.blit(text_surf2, (WINDOW_WIDTH / 2 - 450, WINDOW_HEIGHT / 2 - 75))

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
                charrectImage = pygame.Rect((char.x - 60, char.y - 85, char.size, char.size))

                g.window.blit(pygame.transform.flip(char.image, False, False), charrectImage)
            text_surf2, text_rect2 = self.render_text(
                self.fontStart, 
                "Place Your Bets. Starting in " + str(self.startCountdown // 60),
                (0, 0, 0)
            )
            g.window.blit(text_surf2, (WINDOW_WIDTH / 2 - 450, WINDOW_HEIGHT / 2 - 75))

        elif self.endScreenCountdown != 0:
            self.endScreenCountdown -= 1
            self.displayResult()

        elif self.endScreenCountdown == 0 and self.result != "":
            self.gameStart = False

            self.startCountdown = startTimer

            self.initialized = False

            self.gameOver = False
            self.gameOverCountdown = 30

            self.wallModifier = 0

            self.result = ""
            self.winner = ""

        else:
            if self.gambling:
                self.gambling = False
                if API and _requests_available:
                    try:
                        requests.post(
                            self.url + "/setgambling", json={"openGambling": self.gambling}
                        )
                    except Exception as e:
                        print(f"[web] Failed to update gambling flag: {e}")

            physics.physicsUpdate()
            self.alivelist = [poke for poke in self.charList if poke.alive]

            if len(self.alivelist) <= 1 and self.gameOverCountdown == 30:
                self.gameOver = True
            for char in self.charList:
                if char.moveText:
                    if char.moveText.ttl > 0:
                        text_surf2, text_rect2 = self.render_text(
                            self.font, char.moveText.text, (0, 0, 0, char.moveText.alpha)
                        )
                        g.window.blit(
                            text_surf2, (char.moveText.x - 48, char.moveText.y - 8)
                        )
                        text_surf2, text_rect2 = self.render_text(
                            self.font, char.moveText.text, (255, 255, 255, char.moveText.alpha)
                        )
                        g.window.blit(text_surf2, (char.moveText.x - 50, char.moveText.y - 10))
                    char.moveText.tick()
                newDamageIndictators = []
                for indic in char.damageIndicators:
                    indic.move()
                    text_surf2, text_rect2 = self.render_text(
                        self.font, indic.damage, (255, 0, 0, indic.alpha)
                    )
                    g.window.blit(text_surf2, (indic.x, indic.y + 10))
                    if indic.ttl >= 0:
                        newDamageIndictators.append(indic)
                char.damageIndicators = newDamageIndictators

            if self.gameOver:
                self.gameOverCountdown -= 1

            if self.gameOverCountdown == 0:
                if len(self.alivelist) == 0:
                    self.result = "draw"
                    if API and _requests_available:
                        try:
                            requests.post(
                                self.url + "/setwinner", json={"winner": "Nobody"}
                            )
                        except Exception as e:
                            print(f"[web] Failed to post winner (draw): {e}")
                elif len(self.alivelist) == 1:
                    self.result = "win"
                    self.winner = self.alivelist[0].name
                    self.alivelist[0].kill()
                    if API and _requests_available:
                        try:
                            requests.post(
                                self.url + "/setwinner", json={"winner": self.winner}
                            )
                        except Exception as e:
                            print(f"[web] Failed to post winner: {e}")
