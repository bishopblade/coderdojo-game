import turtle, random, math

boundary = {'r':200, 'l':-200, 't':200, 'b':-200}
level = 1
levelMultiplier = 0.5

class Point(object):
  """2D Math-Vector class. contains x, y used to positioning and 2D Math"""
  def __init__(self, a_x, a_y):
    self.x = a_x
    self.y = a_y
  def clone(self):
    return Point(self.x, self.y)
  def add(self, other):
    global boundary
    #print (boundary)
    self.x += other.x
    if (self.x > boundary['r']):
        self.x = boundary['r']
    elif (self.x < boundary['l']):
        self.x = boundary['l']
        
    self.y += other.y
    if (self.y > boundary['t']):
        self.y = boundary['t']
    elif (self.y < boundary['b']):
        self.y = boundary['b']

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
  def getXY(self):
      return {'x':self.position.x, 'y':self.position.y}
  def setPosition(self, position):
      self.position = position
  def getPosition(self):
      return Point(self.position.x, self.position.y)
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

enemies = []
def setEnemies():
    global enemies;
    num = int(10 * level * levelMultiplier)
    numEnemies = len(enemies);
    for e in enemies:
        randomPoint = Point(random.randrange(-200, 200), random.randrange(-200, 200))
        e.setPosition(randomPoint)
    for e in range(num - numEnemies):
        randomPoint = Point(random.randrange(-200, 200), random.randrange(-200, 200))
        en = Entity("red", 5, randomPoint, 10)
        enemies.append(en)

    
# initialize the environment and data
t = turtle.Turtle()
t.shape('turtle')
window = turtle.Screen()
window.setup(450,450)
window.reset()
t.speed(-1)
t.hideturtle()

levelMoves = 0
winningLevelMoves = 10
score = 0
status = 1 # Alive
losePosition = Point(7, 7)

randomPoint = Point(random.randrange(-200, 200), random.randrange(-200, 200))
p = Entity("green", 5, randomPoint, 15)

setEnemies()


# main draw functions
currently_drawing = False
drawing_object = p;
def moveObject(o):
    o.draw(t)

def drawBase():
    t.penup()

    # Border
    t.color('black')
    t.goto(-200, 200)
    t.pendown()
    t.goto(200, 200)
    t.goto(200, -200)
    t.goto(-200, -200)
    t.goto(-200, 200)
    t.penup()

    # Score
    t.goto(-200, 200)
    t.pendown()
    t.write('SCORE: ', move=True)
    t.write(score)
    t.penup()
    
    # Level
    t.goto(160, 200)
    t.pendown()
    t.write('LEVEL: ', move=True)
    t.write(level)
    t.penup()


    # Info
    t.goto(0, 200)
    t.pendown()
    s = ' '.join(['Make', str(winningLevelMoves), 'moves to complete level'])        
    t.write(s, align='center')
    t.penup()
    
    # End of game?
    if status is 0:
        t.penup()
        t.goto(0,0)
        t.pendown()
        t.write('GAME OVER', align='center', font=('Arial',20, 'bold'))
        t.penup()

    # End of level?
    elif levelMoves is 0 and level > 1:
        t.penup()
        t.goto(0,0)
        t.pendown()
        s = ' '.join(['LEVEL', str(level-1), 'COMPLETE'])        
        t.write(s, align='center', font=('Arial',20, 'bold'))
        t.penup()
        setEnemies()
        

    
def drawEverything():
    global currently_drawing, drawing_object
    if not currently_drawing and status:
        currently_drawing = True
        t.clear()
        drawBase()            
        moveObject(p);
        moveEnemy(enemies, p)
        currently_drawing = False

# all of the input functions
def moveLeftRight(o, diff):
  sign = abs(diff)/diff
  o.simpleMove(Point(sign * o.speed,0))
  drawEverything()
def moveUpDown(o, diff):
  sign = abs(diff)/diff
  o.simpleMove(Point(0, sign * o.speed))
  drawEverything()
  
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
  #print(p.direction)
  drawEverything()

    
# Do enemy update
def moveEnemy(enemies, p):
    global score, status, level, levelMoves
    position = p.getPosition()
    #print (position)
    for e in enemies:
        diff = position.difference(e.getPosition())
        if(abs(diff.x) > abs(diff.y)):
            moveLeftRight(e, diff.x)
        else:
            moveUpDown(e, diff.y)
            
        #e.setTarget(position)
        #e.moveAtTarget(1.5)    
        moveObject(e)

        # Is it Over?
        newdiff = position.difference(e.getPosition())
        if(abs(newdiff.x) < losePosition.x and abs(newdiff.y) < losePosition.y):
            print ('OVER!!!')
            print ('Score =', score)
            status = 0;
            drawBase()

    if(status > 0):
        levelMoves += 1
        score += level
        #print (score)
        
    if levelMoves >= winningLevelMoves:
        level += 1
        levelMoves = 0
     
    
# Main loop
window.onkey(moveLeft, "Left")
window.onkey(moveRight, "Right")
window.onkey(moveUp, "Up")
window.onkey(moveDown, "Down")
window.onclick(mouseClick)

window.listen()
drawEverything()
