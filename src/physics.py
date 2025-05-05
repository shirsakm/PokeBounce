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
    drawPriority: int = 0

    def __init__(self, x, y, width, height, centered=True):
        self.centered = centered
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        if self.centered:
            self.x -= self.width / 2
            self.y -= self.height / 2
        allObjects.append(self)

    def update(self):
        self.x += self.xVel
        self.y += self.yVel
    
    def resize(self, width, height):
        if self.centered:
            self.x -= (width - self.width) / 2
            self.y -= (height - self.height) / 2
        self.width = width
        self.height = height
    
    def draw(self):
        pass

    def getCollider(self):
        return Rect(self.x, self.y, self.width, self.height)

    def collide(self, other):
        pass


class Wall(PhysicsObject):
    wallGrowth = 0.01
    maxSize = 300
    color = (20, 10, 20)
    drawPriority = 2
    
    def __init__(self, direction):
        self.direction = direction
    
    def reset(self):
        match self.direction:
            case "left":
                super().__init__(0, 0, 50, 800, False)
            case "right":
                super().__init__(1400, 0, 51, 800, False)
            case "top":
                super().__init__(0, 0, 1450, 50, False)
            case "bottom":
                super().__init__(0, 750, 1450, 51, False)
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
    priorities = [0,1,2]
    for pri in priorities:
        for obj in filter(lambda o: o.drawPriority == pri, allObjects):
            obj.draw()

    frameObjList = allObjects.copy()
    for obj in frameObjList:
        obj.update()
    rects = [obj.getCollider() for obj in frameObjList]
    for obj in [obj for obj in frameObjList if obj.checksCollision]:
        for ind in obj.getCollider().collidelistall(rects):
            other = frameObjList[ind]
            if other is obj: continue
            obj.collide(other)
