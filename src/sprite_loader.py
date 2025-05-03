import pygame
from pygame.locals import *
from src.constants import *

class Sprites:
    base_dir = "img"
    battler_dir = base_dir+"/battlers"
    move_dir = base_dir+"/moves"

    battlers = {}
    moves = {}
    arena = None
    _WINDOW_WIDTH = None
    _WINDOW_HEIGHT = None


    def __init__(self):
        print("Loading images from '"+self.base_dir+"/*'...")
        print("Arena...")
        self.get_arena()
        print("Battlers...")
        self._load_battlers(battler_sprites)
        print("Moves...")
        self._load_moves(move_sprites)


    def get_battler(self,battler_id):
        if (battler_id not in self.battlers.keys()):
            self.battlers[battler_id] = self._load_battler(battler_id)

        return self.battlers[battler_id]


    def get_move(self,move_id):
        if (move_id not in self.moves.keys()):
            self._load_move(move_id)

        return self.moves[move_id]


    def get_arena(self):
        if (self.arena == None):
            self.arena = self._load_img(Sprites.base_dir+"/arena.png",WINDOW_WIDTH, WINDOW_HEIGHT)

        return self.arena

    def _load_img(self,file_path,x_scale,y_scale):
        img = pygame.image.load(file_path).convert_alpha()
        if (x_scale == None):
            x_scale = img.get_width()
        if (y_scale == None):
            y_scale = img.get_height()
        return pygame.transform.scale(img, (x_scale, y_scale))
    

    def _load_battler(self,battler_id):
        return self._load_img(self.battler_dir+"/"+battler_id+".png",204,168)

    def _load_move(self,move_id):
        scale = 100
        if move_id == "poison":
            scale = 10
        return self._load_img(self.move_dir+"/"+move_id+".png",scale,scale)
    

    def _load_battlers(self,arr):
        for img in arr:
            self.battlers[img] = self._load_battler(img)
    
    def _load_moves(self,arr):
        for img in arr:
            self.moves[img] = self._load_move(img)

INSTANCE = Sprites()