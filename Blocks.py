import pygame
from pygame.draw import rect

ORANGE_RICKY = "OrangeRicky"
BLUE_RICKY = "BlueRicky"
CLEVELANDZ = "ClevelandZ"
RHODE_ISLAND_Z = "RhodeIslandZ"
TEWEE = "Teewee"
SMASH_BOY = "SmashBoy"
HERO = "Hero"

class Block ():
    def __init__(self, type: str, positionX: float =  0.0, positionY: float =  0.0,
                size: float = 20, color: tuple = (255, 255, 255), gradient: int = 50) -> None:
        self.type = type
        self.size = size
        self.positionX = positionX
        self.positionY = positionY
        self.anchor = pygame.Rect(self.positionX, self.positionY, self.size, self.size)
        self.rotate = 'default'
        self.color = color
        self.gradient = gradient
    
    def Build(self) -> None:
        if self.type == HERO:
            var = self.hero_set_sprite()
            varX = var[0]
            varY = var[1]
        elif self.type == ORANGE_RICKY:
            var = self.orangeR_set_sprite()
            varX = var[0]
            varY = var[1]
        elif self.type == BLUE_RICKY:
            var = self.blueR_set_sprite()
            varX = var[0]
            varY = var[1]
        elif self.type == CLEVELANDZ:
            var = self.cleveZ_set_sprite()
            varX = var[0]
            varY = var[1]
        elif self.type == RHODE_ISLAND_Z:
            var = self.rhodeZ_set_sprite()
            varX = var[0]
            varY = var[1]
        elif self.type == TEWEE:
            var = self.tewee_set_sprite()
            varX = var[0]
            varY = var[1]
        elif self.type == SMASH_BOY:
            var = self.smashB_set_sprite()
            varX = var[0]
            varY = var[1]
        else:
            return

        self.primary = pygame.Rect(self.anchor.x + varX[0], self.anchor.y + varY[0], self.size, self.size)
        self.secondary = pygame.Rect(self.anchor.x + varX[1], self.anchor.y + varY[1], self.size, self.size)
        self.tertiary = pygame.Rect(self.anchor.x + varX[2], self.anchor.y + varY[2], self.size, self.size)

    def hero_set_sprite(self):
        if self.rotate == 'first' or self.rotate == 'third':
            varX = self.size, 2*self.size, 3*self.size
            varY = 0, 0, 0
        else:
            varX = 0, 0, 0
            varY = self.size, 2*self.size, 3*self.size
        return varX, varY

    def orangeR_set_sprite(self):
        if self.rotate == 'default':
            varX = -self.size, self.size, self.size
            varY = 0, 0, -self.size
        elif self.rotate == 'first': 
            varX = 0, 0, self.size
            varY = -self.size, self.size, self.size
        elif self.rotate == 'second':
            varX = self.size, -self.size, -self.size
            varY = 0, 0, self.size
        else:
            varX = 0, 0, -self.size
            varY = self.size, -self.size, -self.size
        return varX, varY
        
    def blueR_set_sprite(self):
        if self.rotate == 'default':
            varX = -self.size, self.size, self.size
            varY = 0, 0, self.size
        elif self.rotate == 'first': 
            varX = 0, 0, -self.size
            varY = self.size, -self.size, self.size
        elif self.rotate == 'second':
            varX = self.size, -self.size, -self.size
            varY = 0, 0, -self.size
        else:
            varX = 0, 0, self.size
            varY = -self.size, self.size, -self.size
        return varX, varY

    def cleveZ_set_sprite(self):
        if self.rotate == 'default' or self.rotate == 'second':
            varX = -self.size, 0, self.size
            varY = 0, self.size, self.size
        else:
            varX = 0, -self.size, -self.size
            varY = -self.size, 0, self.size
        return varX, varY

    def rhodeZ_set_sprite(self):
        if self.rotate == 'default' or self.rotate == 'second':
            varX = self.size, 0, -self.size
            varY = 0, self.size, self.size
        else:
            varX = 0, self.size, self.size
            varY = -self.size, 0, self.size
        return varX, varY

    def tewee_set_sprite(self):
        if self.rotate == 'default':
            varX = -self.size, self.size, 0
            varY = 0, 0, self.size
        elif self.rotate == 'first': 
            varX = 0, 0, -self.size
            varY = self.size, -self.size, 0
        elif self.rotate == 'second':
            varX = self.size, -self.size, 0
            varY = 0, 0, -self.size
        else:
            varX = 0, 0, self.size
            varY = self.size, -self.size, 0
        return varX, varY

    def smashB_set_sprite(self):
        varX = - self.size, -self.size, 0
        varY = 0, self.size, self.size
        return varX, varY
    
    def Move(self, x: float, y: float) -> None:
        self.anchor.x += x
        self.anchor.y += y
        self.Build()

    def Rotate(self) -> None:
        if self.rotate == 'default':
            self.rotate = 'first'
        elif self.rotate == 'first':
            self.rotate = 'second'
        elif self.rotate == 'second':
            self.rotate = 'third'
        elif self.rotate == 'third':
            self.rotate = 'default'
        
    def Draw(self, window) -> None:
        self.Build()
        for i in (self.anchor, self.primary, self.secondary, self.tertiary):
            pygame.draw.rect(window, self.color, i)
