import pygame
import random
import time

class Point(pygame.sprite.Sprite):
    def __init__(self, x, y, screen):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.screen = screen
    def __str__(self):
        return "Point at coordinates " + str(x) + ", " + str(y)
    def move(self, x, y):
        self.x = x
        self.y = y
    def display(self):
        self.shape = pygame.draw.point(self.x, self.y)
        self.screen.blit(self.shape)
    
