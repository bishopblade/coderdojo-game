from tkinter import *
from tkinter import ttk
import random
import turtle
import time
x = 4
y = 5
width = 20
height = 10
icon = '@'

# how to draw the game
def drawGame():
  global height
  global width
  for row in range(0, height):
    line = ""
    for col in range(0, width):
      if y == row and x == col:
        line += icon
      else:
        line += '.'
    print(line)
  print('\n')

def moveLeft():
  global x
  x -= 1
  drawGame()
def moveRight():
  global x
  x += 1
  drawGame()
def moveUp():
  global y
  y -= 1
  drawGame()
def moveDown():
  global y
  y += 1
  drawGame()
  
# the turtle library for the key input methods only
import turtle
window = turtle.Screen()
window.onkey(moveLeft, "left")
window.onkey(moveRight, "right")
window.onkey(moveUp, "up")
window.onkey(moveDown, "down")
window.listen()

# show the game
print("move with the arrow keys")
drawGame()

'''import turtle, random, math

class Point(object):
  """2D Math-Vector class. contains x, y used to positioning and 2D Math"""
  def __init__(self, a_x, a_y):
    self.x = a_x
    self.y = a_y
  def clone(self):
    return Point(self.x, self.y)
  def add(self, other):
    self.x += other.x
    self.y += other.y
  def sum(self, other):
    return Point(self.x+other.x, self.y+other.y)
  def difference(self, other):
    return Point(self.x-other.x, self.y-other.y)
  def magnitude(self):
    return math.sqrt(self.x*self.x+self.y*self.y)
  def normal(self):
    d = self.magnitude()
    return Point(self.x / d, self.y / d)
  def product(self, scalar):
    return Point(self.x*scalar, self.y*scalar)
  def __str__(self):
    return "("+str(self.x)+","+str(self.y)+")"
  def draw(self, t, radius):
    t.penup()
    t.goto(self.x,self.y-radius)
    t.pendown()
    t.circle(radius)
    t.penup()

class Entity(object):
  """color, radius, position, speed, direction, target, velocity"""
  def __init__(self, color, radius, position, speed):
    self.color = color
    self.radius = radius
    self.position = position
    self.speed = speed
    self.velocity = Point(0,0)
    self.direction = Point(0,1)
    self.target = Point(0,0)
  def setTarget(self, target):
    self.target = target
    delta = target.difference(self.position)
    self.direction = delta.normal()
  def moveAtTarget(self, time):
    delta = self.target.difference(self.position)
    dist = delta.magnitude()
    if dist < self.radius:
      self.velocity = Point(0,0)
    else:
      self.velocity.add(self.direction.product(time*self.speed))
      m = self.velocity.magnitude()
      if m >= self.speed:
        self.velocity = self.velocity.normal().product(self.speed)
      self.position.add(self.velocity.product(time))
  def simpleMove(self, dir):
    self.direction = dir.normal()
    self.position.add(dir)
  def draw(self, t):
    t.color(self.color)
    self.position.draw(t, self.radius)
    t.goto(self.position.x,self.position.y)
    t.pendown()
    end = self.position.sum(self.direction.product(self.speed))
    t.goto(end.x, end.y)
    t.penup()

# initialize the environment and data
t = turtle.Turtle()
t.shape('turtle')
window = turtle.Screen()
window.setup(400,400)
window.reset()
t.speed(-1)
t.hideturtle()
randomPoint = Point(random.randrange(-200, 200), random.randrange(-200, 200))
p = Entity("green", 5, randomPoint, 10)

# main draw function
currently_drawing = False
def drawEverything():
  global currently_drawing
  if not currently_drawing:
    currently_drawing = True
    t.clear()
    p.draw(t)
    t.penup()
    currently_drawing = False

# all of the input functions
def moveLeft():
  p.simpleMove(Point(-p.speed,0))
  drawEverything()
def moveRight():
  p.simpleMove(Point(p.speed,0))
  drawEverything()
def moveUp():
  p.simpleMove(Point(0,p.speed))
  drawEverything()
def moveDown():
  p.simpleMove(Point(0,-p.speed))
  drawEverything()
def mouseClick(x, y):
  p.setTarget(Point(x,y))
  p.moveAtTarget(1)
  print(p.direction)
  drawEverything()

window.onkey(moveLeft, "left")
window.onkey(moveRight, "right")
window.onkey(moveUp, "up")
window.onkey(moveDown, "down")
window.onclick(mouseClick)
window.listen()
drawEverything()
'''
print ("Hi")
