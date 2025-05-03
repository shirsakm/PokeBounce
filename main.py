import pygame, sys, random, math
from pygame.locals import *
import requests
import datetime

from poke import Poke, chooseChars



url = "http://127.0.0.1:5000"

pygame.init()

showHitboxes = False
showCollisionBoxes = False

 
# Colours
BACKGROUND = (240, 240, 240)
 
# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 1450
WINDOW_HEIGHT = 800
 
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.Surface.convert_alpha(WINDOW)

SURFACE = pygame.Surface((WINDOW_WIDTH,WINDOW_HEIGHT), pygame.SRCALPHA)
pygame.display.set_caption('Auto Arena')
 
fontStart = pygame.freetype.SysFont('vcr osd mono', 50)
font = pygame.freetype.SysFont('vcr osd mono', 25)


arena_img = pygame.image.load('arena.png').convert_alpha()
arena_img = pygame.transform.scale(arena_img, (WINDOW_WIDTH, WINDOW_HEIGHT))

# Pokemon Sprites
pika_img = pygame.image.load('pikachu.png').convert_alpha()
pika_img = pygame.transform.scale(pika_img, (204, 168))

staraptor_img = pygame.image.load('staraptor.png').convert_alpha()
staraptor_img = pygame.transform.scale(staraptor_img, (204, 168))

infernape_img = pygame.image.load('infernape.png').convert_alpha()
infernape_img = pygame.transform.scale(infernape_img, (204, 168))

umbreon_img = pygame.image.load('umbreon.png').convert_alpha()
umbreon_img = pygame.transform.scale(umbreon_img, (204, 168))

mamoswine_img = pygame.image.load('mamoswine.png').convert_alpha()
mamoswine_img = pygame.transform.scale(mamoswine_img, (204, 168))

kingdra_img = pygame.image.load('kingdra.png').convert_alpha()
kingdra_img = pygame.transform.scale(kingdra_img, (204, 168))

decidueye_img = pygame.image.load('decidueye.png').convert_alpha()
decidueye_img = pygame.transform.scale(decidueye_img, (204, 168))

scizor_img = pygame.image.load('scizor.png').convert_alpha()
scizor_img = pygame.transform.scale(scizor_img, (204, 168))

nidoking_img = pygame.image.load('nidoking.png').convert_alpha()
nidoking_img = pygame.transform.scale(nidoking_img, (204, 168))

wigglytuff_img = pygame.image.load('wigglytuff.png').convert_alpha()
wigglytuff_img = pygame.transform.scale(wigglytuff_img, (204, 168))

smeargle_img = pygame.image.load('smeargle.png').convert_alpha()
smeargle_img = pygame.transform.scale(smeargle_img, (204, 168))

marowak_img = pygame.image.load('marowak-alola.png').convert_alpha()
marowak_img = pygame.transform.scale(marowak_img, (204, 168))

porygonz_img = pygame.image.load('porygon-z.png').convert_alpha()
porygonz_img = pygame.transform.scale(porygonz_img, (204, 168))

clodsire_img = pygame.image.load('clodsire.png').convert_alpha()
clodsire_img = pygame.transform.scale(clodsire_img, (204, 168))

tyranitar_img = pygame.image.load('tyranitar.png').convert_alpha()
tyranitar_img = pygame.transform.scale(tyranitar_img, (204, 168))

metagross_img = pygame.image.load('metagross.png').convert_alpha()
metagross_img = pygame.transform.scale(metagross_img, (204, 168))

# Move Sprites

shadowball_img = pygame.image.load('shadowball.png').convert_alpha()
shadowball_img = pygame.transform.scale(shadowball_img, (55, 40))

fire1_img = pygame.image.load('fire000.png').convert_alpha()
fire1_img = pygame.transform.scale(fire1_img, (100, 100))

fire2_img = pygame.image.load('fire001.png').convert_alpha()
fire2_img = pygame.transform.scale(fire2_img, (100, 100))

fire3_img = pygame.image.load('fire002.png').convert_alpha()
fire3_img = pygame.transform.scale(fire2_img, (100, 100))

fire4_img = pygame.image.load('fire003.png').convert_alpha()
fire4_img = pygame.transform.scale(fire2_img, (100, 100))

fire5_img = pygame.image.load('fire004.png').convert_alpha()
fire5_img = pygame.transform.scale(fire2_img, (100, 100))

fire6_img = pygame.image.load('fire005.png').convert_alpha()
fire6_img = pygame.transform.scale(fire2_img, (100, 100))

fire7_img = pygame.image.load('fire006.png').convert_alpha()
fire7_img = pygame.transform.scale(fire2_img, (100, 100))

fire8_img = pygame.image.load('fire007.png').convert_alpha()
fire8_img = pygame.transform.scale(fire2_img, (100, 100))

bubble_img = pygame.image.load('bubble.png').convert_alpha()
bubble_img = pygame.transform.scale(bubble_img, (100, 100))

leaf_img = pygame.image.load('leaf.png').convert_alpha()
leaf_img = pygame.transform.scale(leaf_img, (100, 100))

bravebird_img = pygame.image.load('bravebird.png').convert_alpha()
bravebird_img = pygame.transform.scale(bravebird_img, (100, 100))

stone_img = pygame.image.load('stone.png').convert_alpha()
stone_img = pygame.transform.scale(stone_img, (100, 100))

poison_img = pygame.image.load('poison.png').convert_alpha()
poison_img = pygame.transform.scale(poison_img, (100, 100))

dark_img = pygame.image.load('dark.png').convert_alpha()
dark_img = pygame.transform.scale(dark_img, (100, 100))

dazzling_img = pygame.image.load('dazzling.png').convert_alpha()
dazzling_img = pygame.transform.scale(dazzling_img, (100, 100))

irontail_img = pygame.image.load('irontail.png').convert_alpha()
irontail_img = pygame.transform.scale(irontail_img, (100, 100))

ironhead_img = pygame.image.load('ironhead.png').convert_alpha()
ironhead_img = pygame.transform.scale(ironhead_img, (100, 100))

fist_img = pygame.image.load('fist.png').convert_alpha()
fist_img = pygame.transform.scale(fist_img, (100, 100))

bone_img = pygame.image.load('bone.png').convert_alpha()
bone_img = pygame.transform.scale(bone_img, (100, 100))

earthquake_img = pygame.image.load('earthquake.png').convert_alpha()
earthquake_img = pygame.transform.scale(earthquake_img, (100, 100))

waterfall_img = pygame.image.load('waterfall.png').convert_alpha()
waterfall_img = pygame.transform.scale(waterfall_img, (100, 100))

sandstorm_img = pygame.image.load('sandstorm.png').convert_alpha()
sandstorm_img = pygame.transform.scale(sandstorm_img, (100, 100))

zenheadbutt_img = pygame.image.load('zenheadbutt.png').convert_alpha()
zenheadbutt_img = pygame.transform.scale(zenheadbutt_img, (100, 100))


moveDict = {
  "shadowball" : shadowball_img,
  "fire1" : fire1_img,
  "fire2" : fire2_img,
  "fire3" : fire3_img,
  "fire4" : fire4_img,
  "fire5" : fire5_img,
  "fire6" : fire6_img,
  "fire7" : fire7_img,
  "fire8" : fire8_img,
  "bubble" : bubble_img,
  "leaf" : leaf_img,
  "bravebird" : bravebird_img,
  "stone" : stone_img,
  "poison" : poison_img,
  "dark" : dark_img,
  "dazzling" : dazzling_img,
  "irontail" : irontail_img,
  "ironhead" : ironhead_img,
  "fist" : fist_img,
  "bone" : bone_img,
  "earthquake" : earthquake_img,
  "waterfall" : waterfall_img,
  "sandstorm" : sandstorm_img,
  "zenheadbutt" : zenheadbutt_img,
}


maxHealth = 300

pikachu1 = Poke(75, 450, pika_img, 80, ["Thunderbolt", "Quick Attack", "Iron Tail"], "Pikachu", maxHealth)
# pikachu1 = Poke(600, 400, pika_img, 80, ["Thunderbolt"], "Pikachu", maxHealth)

staraptor1 = Poke(600, 450, staraptor_img, 80, ["Quick Attack", "Brave Bird", "Close Combat"], "Staraptor", maxHealth)

infernape1 = Poke(600, 75, infernape_img, 80, ["Flamethrower", "Stone Edge", "Close Combat"], "Infernape", maxHealth)
# infernape1 = Poke(800, 400, infernape_img, 80, ["Close Combat"], "Infernape", maxHealth)

umbreon1 = Poke(75, 75, umbreon_img, 80, ["Quick Attack", "Dark Pulse", "Shadow Ball"], "Umbreon", maxHealth)

mamoswine1 = Poke(700, 500, mamoswine_img, 80, ["Ice Beam", "Stone Edge", "Iron Head"], "Mamoswine", maxHealth)

nidoking1 = Poke(1000, 200, nidoking_img, 80, ["Bubble Beam", "Stone Edge", "Poison Sting"], "Nidoking", maxHealth)

scizor1 = Poke(1000, 400, scizor_img, 80, ["U Turn", "Iron Head", "Close Combat"], "Scizor", maxHealth)

wigglytuff1 = Poke(1200, 300, wigglytuff_img, 80, ["Dazzling Gleam", "Flamethrower", "Thunderbolt"], "Wigglytuff", maxHealth)

decidueye1 = Poke(1200, 150, decidueye_img, 80, ["Razor Leaf", "Brave Bird", "Shadow Ball"], "Decidueye", maxHealth)

kingdra1 = Poke(1200, 650, kingdra_img, 80, ["Dragon Pulse", "Ice Beam", "Bubble Beam"], "Kingdra", maxHealth)

smeargle1 = Poke(700, 100, smeargle_img, 80, ["Thunderbolt", "Quick Attack", "Flamethrower", "Shadow Ball", "Razor Leaf", "Bubble Beam", "U Turn", "Ice Beam", "Dragon Pulse", "Brave Bird", "Stone Edge", "Dazzling Gleam", "Close Combat", "Poison Sting", "Dark Pulse", "Iron Tail", "Iron Head", "Earthquake", "Sandstorm", "Waterfall", "Zen Headbutt", "Bonemerang", "Hyper Beam"], "Smeargle", maxHealth)

marowak1 = Poke(700, 650, marowak_img, 80, ["Bonemerang", "Flamethrower", "Shadow Ball"], "Marowak", maxHealth)

clodsire1 = Poke(300, 650, clodsire_img, 80, ["Earthquake", "Poison Sting", "Waterfall"], "Quagsire", maxHealth)

porygonz1 = Poke(1000, 650, porygonz_img, 80, ["Hyper Beam", "Thunderbolt", "Ice Beam"], "Porygon-Z", maxHealth)

tyranitar1 = Poke(850, 500, tyranitar_img, 80, ["Sandstorm", "Dark Pulse", "Stone Edge"], "Tyranitar", maxHealth)

metagross1 = Poke(850, 100, metagross_img, 80, ["Earthquake", "Zen Headbutt", "Iron Head"], "Metagross", maxHealth)




allChars = [
  pikachu1,
  umbreon1,
  staraptor1,
  infernape1,
  mamoswine1,
  kingdra1,
  wigglytuff1,
  decidueye1,
  scizor1,
  nidoking1,
  smeargle1,
  marowak1,
  clodsire1,
  porygonz1,
  tyranitar1,
  metagross1
]

startTimer = 300

charList = allChars

gameStart = False

startCountdown = startTimer

charsChosen = False

gameOver = False
gameOverCountdown = 30

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

  WINDOW.blit(arena_img, bgrect)

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
      charList = chooseChars(allChars, random.randint(3,10))
      # charList = [pikachu1, staraptor1]
      charsChosen = True

      gameId = random.randint(10000, 99999)

      fighterList = []
      for char in charList:
      	fighterList.append(char.name)

      requests.post(url + "/setfighters", json = {"fighters" : fighterList})
      requests.post(url + "/setgameid", json = {"id" : gameId})

      gambling = True
      requests.post(url + "/setgambling", json = {"openGambling" : gambling})

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
        requests.post(url + "/setgambling", json = {"openGambling" : gambling})

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

        healthPercentWidth = (char.health / maxHealth) * char.healthBox.width

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
        moveImage = moveDict[moveRect[1].image]

        moveImage = pygame.transform.scale(moveImage, (moveRect[1].size, moveRect[1].size))
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
        requests.post(url + "/setwinner", json = {"winner" : "Nobody"})
      if len(alivelist) == 1:
        result = "win"
        winner = alivelist[0]
        requests.post(url + "/setwinner", json = {"winner" : winner})
      endScreenCountdown = 240
      







  pygame.display.flip()
  fpsClock.tick(FPS)
