import pygame
import random
import time

print "Welcome to Master"
print "Use the arrow keys to move"

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "Point at coordinates " + str(x) + ", " + str(y)
    
