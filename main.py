import pygame
import random
import time
pygame.init()

print "Welcome to Dot's Adventure"
print "Use the arrow keys to move"
screen = pygame.display.set_mode([640, 260])

coins = 50
coins_won = random.randint(0,10)
coins_lost = random.randint(0,3)

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, screen):
        Sprite.__init__(self)
        self.x = x
        self.y = y
        self.screen = screen
        self.color = pygame.color.Color
    def __str__(self):
        return "Point at coordinates " + str(x) + ", " + str(y)
    def move(self, x, y):
        self.x = x
        self.y = y
    def display(self):
        self.shape = pygame.draw.point(self.x, self.y)
        self.screen.blit(self.shape)
        self.screen.update()
    def difference (self, other):
        return (self.x-other.x, self.y-other.y)
