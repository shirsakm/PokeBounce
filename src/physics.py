from pygame import Rect, draw
from src.globals import g

class PhysicsObject:
    collider: Rect
    x: float
    y: float
    height: float
    width: float
    xVel: float = 0
    yVel: float = 0
    centered: bool = True
    checksCollision: bool = False

    def __init__(self, x, y, width, height, centered=True):
        self.centered = centered
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        if self.centered:
            self.x += self.width / 2
            self.y += self.height / 2
        allObjects.append(self)
    
    def update(self):
        self.x += self.xVel
        self.y += self.yVel
    
    def draw(self):
        pass
    
    def getCollider(self):
        return Rect(self.x, self.y, self.width, self.height)
    
    def collide(self, other, direction):
        pass

class Wall(PhysicsObject):
    wallGrowth = 0.01
    maxSize = 300
    color = (20,10,20)
    def __init__(self, direction):
        self.direction = direction
        match self.direction:
            case "left":
                super().__init__(0, 0, 50, 800, False)
            case "right":
                super().__init__(1400, 0, 50, 800, False)
            case "top":
                super().__init__(0, 0, 1450, 50, False)
            case "bottom":
                super().__init__(0, 750, 1450, 50, False)
        self.wallModifier = 0
    
    def update(self):
        if self.wallModifier < self.maxSize:
            self.wallModifier += self.wallGrowth
            match self.direction:
                case "left":
                    self.width += self.wallGrowth
                case "right":
                    self.x -= self.wallGrowth
                    self.width += self.wallGrowth
                case "top":
                    self.height += self.wallGrowth
                case "bottom":
                    self.y -= self.wallGrowth
                    self.height += self.wallGrowth
    
    def draw(self):
        draw.rect(g.window, self.color, self.getCollider())


allObjects: list[PhysicsObject] = []

def physicsUpdate():
    for obj in allObjects:
        obj.update()
    rects = [obj.getCollider() for obj in allObjects]
    for obj in [obj for obj in allObjects if obj.checksCollision]:
        for ind in obj.getCollider().collidelistall(rects):
            other = list(filter(lambda x: x.getCollider() == rects[ind], allObjects))[0]
            if other is obj: continue
            diffX = obj.x - other.x
            diffY = obj.y - other.y
            direction = ""
            if abs(diffX) < abs(diffY):
                if diffX > 0:
                    direction = "left"
                else:
                    direction = "right"
            else:
                if diffY > 0:
                    direction = "bottom"
                else:
                    direction = "top"
            obj.collide(other, direction)
    for obj in allObjects:
        obj.draw()