import pygame, sys, random
from pygame.locals import *
import requests
from src.debug import *
from src.constants import *

# Game Setup
pygame.init()
FPS = 60
fpsClock = pygame.time.Clock()
 
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.Surface.convert_alpha(WINDOW)

pygame.display.set_caption('Auto Arena')
 
fontStart = pygame.freetype.SysFont('vcr osd mono', 50)
font = pygame.freetype.SysFont('vcr osd mono', 25)

from src.poke import chooseChars
from src.sprite_loader import INSTANCE as sprites
from src.sets import Sets

url = "http://127.0.0.1:5000"
 

gameStart = False

startCountdown = startTimer

charsChosen = False

gameOver = False

winner = ""

result = ""
endScreenCountdown = 0

gambling = False

gameId = 0

gametimer = 0

wallModifier = 0
wallGrowth = 0.01
wallMaxSize = 300

# The main function that controls the game

looping = True

# The main game loop
while looping:
    for event in pygame.event.get() :
        if event.type == QUIT :
            pygame.quit()
            sys.exit()
    

    # Render elements of the game
    WINDOW.fill(BACKGROUND)

    bgrect = pygame.Rect(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)

    WINDOW.blit(sprites.get_arena(), bgrect)

    wallleft = pygame.Rect((0, 0, 50 + wallModifier, 800))
    wallright = pygame.Rect((1400 - wallModifier, 0, 50 + wallModifier + 1, 800))
    walltop = pygame.Rect((0, 0, 1450, 50 + wallModifier))
    walldown = pygame.Rect((0, 750 - wallModifier, 1450, 50 + wallModifier + 1))

    walls = [wallleft, wallright, walltop, walldown]

    for wall in walls:
        pygame.draw.rect(WINDOW, (20,10,20), wall)

    if startCountdown != 0:
        startCountdown -= 1

        if not charsChosen:
            charList = []
            for char in Sets.sets.keys():
                charList.append(Sets.get(char))

            if overrideBattlers:
                charList = []
                for set in battlerOverride:
                    charList.append(Sets.get(set))
            else: 
                charList = chooseChars(charList, random.randint(3,10))
                
            charsChosen = True

            gameId = random.randint(10000, 99999)

            fighterList = []
            for char in charList:
                fighterList.append(char.name)

            if API: requests.post(url + "/setfighters", json = {"fighters" : fighterList})
            if API: requests.post(url + "/setgameid", json = {"id" : gameId})

            gambling = True
            if API: requests.post(url + "/setgambling", json = {"openGambling" : gambling})

        for char in charList:
            charrect = pygame.Rect((char.x, char.y, char.size, char.size))
            charrectImage = pygame.Rect((char.x-60, char.y-85, char.size, char.size))

            WINDOW.blit(pygame.transform.flip(char.image, False, False), charrectImage)
            
        text_surf2, text_rect2 = fontStart.render("Place Your Bets. Starting in " + str(startCountdown//60), (0, 0, 0))
        WINDOW.blit(text_surf2, (WINDOW_WIDTH/2 - 450, WINDOW_HEIGHT/2 - 75))

    elif endScreenCountdown != 0:
        if result == "draw":
            text_surf2, text_rect2 = fontStart.render("DRAW!", (0, 0, 0))
            WINDOW.blit(text_surf2, (WINDOW_WIDTH/2 - 450, WINDOW_HEIGHT/2 - 75))
        elif result == "win":
            text_surf2, text_rect2 = fontStart.render(winner.upper() + " WINS!", (0, 0, 0))
            WINDOW.blit(text_surf2, (WINDOW_WIDTH/2 - 450, WINDOW_HEIGHT/2 - 75))
        endScreenCountdown -= 1

    elif endScreenCountdown == 0 and result != "":
        gameStart = False

        startCountdown = startTimer

        charsChosen = False

        gameOver = False
        gameOverCountdown = 30

        wallModifier = 0

        result = ""
        winner = ""

        for char in charList:
            char.restart()

    else:
        if gambling:

                gambling = False
                if API: requests.post(url + "/setgambling", json = {"openGambling" : gambling})

        if wallModifier < wallMaxSize:
                wallModifier += wallGrowth

        alivelist = []
        for char in charList:
            char.move(char.speed)
            if char.alive:
                alivelist.append(char.name)



                if char.x > WINDOW_WIDTH or char.x < 0:
                    print(char.name, "had a woopsie on the x axis")
                    char.x = WINDOW_WIDTH//2
                if char.y > WINDOW_HEIGHT or char.y < 0:
                    print(char.name, "had a woopsie on the y axis")
                    char.y = WINDOW_HEIGHT//2

                charrect = pygame.Rect((char.x, char.y, char.size, char.size))
                charrectImage = pygame.Rect((char.x-60, char.y-85, char.size, char.size))

                if char.xVel < 0:
                    WINDOW.blit(pygame.transform.flip(char.image, False, False), charrectImage)
                elif char.xVel > 0:
                    WINDOW.blit(pygame.transform.flip(char.image, True, False), charrectImage)

                otherChars = []
                for nestedChar in charList:
                    if nestedChar.alive:
                        if nestedChar != char:
                            otherChars.append(pygame.Rect((nestedChar.x, nestedChar.y, nestedChar.size, nestedChar.size)))

                obstacleList = walls + otherChars

                charLeftBox = pygame.Rect((char.x + char.leftDetectBox.xOffset, char.y + char.leftDetectBox.yOffset, char.leftDetectBox.width, char.leftDetectBox.height))
                charRightBox = pygame.Rect((char.x + char.rightDetectBox.xOffset, char.y + char.rightDetectBox.yOffset, char.rightDetectBox.width, char.rightDetectBox.height))
                charUpBox = pygame.Rect((char.x + char.upDetectBox.xOffset, char.y + char.upDetectBox.yOffset, char.upDetectBox.width, char.upDetectBox.height))
                charDownBox = pygame.Rect((char.x + char.downDetectBox.xOffset, char.y + char.downDetectBox.yOffset, char.downDetectBox.width, char.downDetectBox.height))

                if showCollisionBoxes:
                    pygame.draw.rect(WINDOW, (255,0,0), charLeftBox)
                    pygame.draw.rect(WINDOW, (255,0,0), charRightBox)
                    pygame.draw.rect(WINDOW, (255,0,0), charUpBox)
                    pygame.draw.rect(WINDOW, (255,0,0), charDownBox)


                if charLeftBox.collidelist(obstacleList) != -1:
                    char.collideLeft()
                if charRightBox.collidelist(obstacleList) != -1:
                    char.collideRight()
                if charUpBox.collidelist(obstacleList) != -1:
                    char.collideTop()
                if charDownBox.collidelist(obstacleList) != -1:
                    char.collideBottom()

                char.useMove()

                healthRectRed = pygame.Rect((char.healthBox.xOffset + char.x, char.y - char.healthBox.yOffset, char.healthBox.width, char.healthBox.height))

                healthPercentWidth = (char.health / 300) * char.healthBox.width

                healthRectGreen = pygame.Rect((char.healthBox.xOffset + char.x, char.y - char.healthBox.yOffset, healthPercentWidth, char.healthBox.height))
                pygame.draw.rect(WINDOW, (175,0,0), healthRectRed)
                pygame.draw.rect(WINDOW, (0,175,0), healthRectGreen)

        if len(alivelist) <= 1 and gameOverCountdown == 30:
            gameOver = True

        moveRects = []
        for char in charList:
            stillAliveHitboxes = []
            for move in char.activeHitboxList:
                move.move()
                moveRects.append([pygame.Rect((move.x, move.y, move.size, move.size)), move])
                if move.ttl > 0:
                    stillAliveHitboxes.append(move)
                

            char.activeHitboxList = stillAliveHitboxes

            for char in charList:
                otherCharsHitboxes = []
                otherCharsValues = []
                for nestedChar in charList:
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
                pygame.draw.rect(WINDOW, moveRect[1].colour, moveRect[0])
            if moveRect[1].graphic == "image":
                moveImage = sprites.moves.get(moveRect[1].image)
                moveImage = pygame.transform.scale(moveImage,(moveRect[1].size,moveRect[1].size))
                if moveImage is None:
                    print("Move image is <None>! "+moveRect[1].image)
                        
                rotatedImage = pygame.transform.rotate(moveImage, moveRect[1].rotate)

                new_rect = rotatedImage.get_rect(center = moveImage.get_rect(center = (moveRect[1].x + moveRect[1].size/2, moveRect[1].y + moveRect[1].size/2)).center)

                WINDOW.blit(rotatedImage, new_rect)
            elif moveRect[1].graphic == "rect":
                pygame.draw.rect(WINDOW, moveRect[1].colour, moveRect[0])


            elif moveRect[1].graphic == "circle":
                pygame.draw.circle(WINDOW, moveRect[1].colour, moveRect[0].center, moveRect[1].size/2)



        for char in charList:
            if char.moveText:
                if char.moveText.ttl > 0:
                    text_surf2, text_rect2 = font.render(char.moveText.text, (0, 0, 0, char.moveText.alpha))
                    WINDOW.blit(text_surf2, (char.moveText.x - 48, char.moveText.y - 8))
                    text_surf2, text_rect2 = font.render(char.moveText.text, (255, 255, 255, char.moveText.alpha))
                    WINDOW.blit(text_surf2, (char.moveText.x - 50, char.moveText.y - 10))
                char.moveText.tick()
            newDamageIndictators = []
            for indic in char.damageIndicators:
                indic.move()
                text_surf2, text_rect2 = font.render(indic.damage, (255, 0, 0, indic.alpha))
                WINDOW.blit(text_surf2, (indic.x, indic.y + 10))
                if indic.ttl >= 0:
                    newDamageIndictators.append(indic)
            char.damageIndicators = newDamageIndictators

        if gameOver:
            gameOverCountdown -= 1

        if gameOverCountdown == 0:
            if len(alivelist) == 0:
                result = "draw"
                if API: requests.post(url + "/setwinner", json = {"winner" : "Nobody"})
            if len(alivelist) == 1:
                result = "win"
                winner = alivelist[0]
                if API: requests.post(url + "/setwinner", json = {"winner" : winner})
            endScreenCountdown = 240
            
    pygame.display.flip()
    fpsClock.tick(FPS)
