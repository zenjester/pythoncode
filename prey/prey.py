from tkinter import *
from sys import getfilesystemencoding
import time
import random
import math

height = 600
width = 800


canvas = Canvas(highlightthickness=0, height=height, width=width)
canvas.master.title("Life")
if getfilesystemencoding() == 'utf-8': 
   canvas.master.call('console', 'hide')
canvas.pack()

canvas2 = Canvas(highlightthickness=0, height=200, width=width)
canvas2.master.title("Life")
if getfilesystemencoding() == 'utf-8': 
   canvas2.master.call('console', 'hide')
canvas2.pack()

canvas2.create_line(0, 0, width, 0)

canvas2.position1 = 0 

beingList = []
size = 7
x = size * 2
positionList = [(-x, x),(0, x),(x, x),(x, 0),(x, -x),(0, -x),(-x,-x),(-x,0)]


def calc_distance(x, y, x1, y1):
   return math.sqrt(((x-x1)**2) + ((y-y1)**2))

class prey():
   def __init__(self, x = 400, y = 300, speed = 1, fertility = 1000, lifespan = 3000, sight = 150, size = size):
      self.type = 'Prey'
      self.lifespan = lifespan
      self.size = size
      self.x = x
      self.y = y
      self.speed = speed
      self.sight = sight
      self.min = 10
      self.xspeed, self.yspeed, self.direction = 1, 1, 1
      self.fertility = fertility
      #print(self.speed)
      if self.speed == 1.1:
         self.color = 'purple'
      elif self.speed <= .9:
         self.color = 'green'
      elif self.speed >= 1.2:
         self.color = 'magenta'
      elif self.speed == 1:
         self.color = 'blue'
      self.shape = canvas.create_rectangle(self.x, self.y, self.x + self.size, self.y + self.size, outline = self.color)
      self.collided = 1
      self.coords = [self.x, self.y]###
      self.count = 1
      beingList.append(self)
   def predator_direction(self):
      minimum = 900000
      counter = 0
      for being in beingList:
         if being.type == 'Predator':
            counter = 1
            distance = calc_distance(self.x, self.y, being.x, being.y)
            if distance < minimum:
               minimum = distance
               if self.x - being.x == 0:
                  direction = 'vertical'
               else:
                  direction = ((self.y-being.y)/ (self.x-being.x))
               x = being.coords
               self.min = minimum
               self.direction = direction
         elif (being.type == 'Prey' and (being != self)): #collisons
            if (math.fabs(self.x - being.x) < (self.size)) and (math.fabs(self.y - being.y)< (self.size)):
               self.collision = being
               #print('smash')
               return 'Collision', self.x-being.x, self.y-being.y

      if counter == 0:
         return False
      self.direction = direction
      self.distance = distance
      if counter == 0:
         return False
      return direction, x, minimum
   
   def move(self):
      direction = self.predator_direction()
      if direction == False:
         return False
      predator_coords = direction[1]
      if (self.x <= 0) or (self.x >= (width-self.size)) or (self.y <= 0) or (self.y >= (height-self.size)): 
         if self.x <= 0: self.xspeed = self.speed
         elif self.x >= (width-self.size): self.xspeed = -self.speed
         if self.y <= 0: self.yspeed = self.speed
         elif self.y >= (height-self.size): self.yspeed = -self.speed
      #print(predator_coords)
      elif direction[0] == 'Collision':
         self.x += direction[1]
         self.y += direction[2]


      elif direction[2]< self.sight or self.count == 1:         #prey will drift if there is no close threat
         if direction[0] == 'vertical':  #exception for vertical
            self.xspeed = 0
            self.yspeed = self.speed
            if self.y < predator_coords[1]:
               self.yspeed = -self.yspeed
         elif direction[0] == 0:    #exception for horizontal
            self.xspeed = self.speed
            if self.x < predator_coords[0]:
               self.xspeed = -self.speed
            self.yspeed = 0
         else:                      #calculates speed along x and y
            self.yspeed = math.sqrt(((self.speed)**2)/(((1/direction[0])**2)+1))
            if self.y < predator_coords[1]:
               self.yspeed = -self.yspeed
            self.xspeed = self.yspeed/direction[0]

      self.x += self.xspeed
      self.y += self.yspeed
      self.coords = [self.x, self.y]

      if self.min < self.size:
         self.destroy()
         for being in beingList:    #When a predator eats a prey, it's health is replenished
            if being.type == 'Predator' and [being.x, being.y] == predator_coords:
               being.lifespan = 1100
               break
      else:     
         canvas.coords(self.shape, self.x, self.y, self.x + self.size, self.y + self.size)
         self.count = 0
         self.lifespan -= 1
         self.replicate()
         self.die()
   def replicate(self):
      if random.randint(0,self.fertility) == 1:
         mutation = self.mutate()
         pos = random.randint(0,7) 
         position = positionList[pos]
         new = prey(x = self.x + position[0], y = self.y + position[1], speed = self.speed + mutation[0], sight = self.sight + mutation[1])
   def destroy(self):
      canvas.delete(self.shape)
      beingList.remove(self)
   def mutate(self):
      x = random.randint(1,10)
      y = random.randint(1,10)
      if x == 2:
         speed = .1
      elif x == 1:
         speed = -.1
      else:
         speed = 0
      if y == 1:
         vision = -10
      elif y == 2:
         vision = 10
      else:
         vision = 0
      return speed,vision
   def die(self):
      if random.randint(1, self.lifespan) == 1:
         self.destroy()
      

      
class predator():
   def __init__(self, x = 500, y = 500, speed = 1.1, fertility = 800, lifespan = 1100, sight = 200, size= size):
      self.type = 'Predator'
      self.speed = speed
      self.sight = sight
      self.size = size
      self.x = x
      self.y = y
      self.coords = [self.x,self.y]
      self.shape = canvas.create_rectangle(self.x, self.y, self.x + self.size, self.y + self.size, outline = 'red')
      self.xspeed, self.yspeed, self.direction = 1, 1, 1
      beingList.append(self)
      self.fertility = fertility
      self.lifespan = lifespan
      self.count = 1
   def prey_direction(self):
      minimum = 9000
      counter = 0
      for being in beingList:
         if being.type == 'Prey':
            counter = 1
            distance = calc_distance(self.x, self.y, being.x, being.y)
            if distance < minimum:
               minimum = distance
               if self.x - being.x == 0:
                  direction = 'vertical'
               else:
                  direction = ((self.y-being.y)/ (self.x-being.x))
               
               x = being.coords
               self.prey = being.coords
               self.direction = direction
         elif (being.type == 'Predator' and (being != self)): #collisons
               if (math.fabs(self.x - being.x) < (self.size)) and (math.fabs(self.y - being.y)< (self.size)):
                  self.collision = being
                  #print('smash')
                  return 'Collision', (self.x -being.x), (self.y +self.size -being.y)
               
            
      if counter == 0:
         return False
      return direction, x, minimum
   def move(self):
      direction = self.prey_direction()
      if direction == False:
         return False
      prey_coords = direction[1]
      if (self.x <= 0) or (self.x >= (width-self.size)) or (self.y <= 0) or (self.y >= (height-self.size)): 
         if self.x <= 0: self.xspeed = self.speed
         elif self.x >= (width-self.size): self.xspeed = -self.speed
         if self.y <= 0: self.yspeed = self.speed
         elif self.y >= (height-self.size): self.yspeed = -self.speed

      elif direction[0] == 'Collision':
         self.x += direction[1]
         self.y += direction[2]


      elif self.count == 1 or direction[2] <self.sight:
         if direction[0] == 'vertical':   #exception for vertical
            self.xspeed = 0
            if self.y > prey_coords[1]:
               self.yspeed = -self.speed
            else:
               self.yspeed = self.speed
         elif direction[0] == 0:    #exception for horizontal
            self.xspeed = self.speed
            if self.x > prey_coords[0]:
               self.xspeed = -self.speed
            self.yspeed = 0
         else:                      #calculates speed along x and y
            self.yspeed = math.sqrt(((self.speed)**2)/(((1/direction[0])**2)+1))
            if self.y > prey_coords[1]:
               self.yspeed = -self.yspeed
            self.xspeed = self.yspeed/direction[0]


      self.x += self.xspeed
      self.y += self.yspeed
      self.coords = [self.x, self.y]
      canvas.coords(self.shape, self.x, self.y, self.x + self.size, self.y + self.size)
      self.lifespan -=1
      self.count = 0
      self.replicate()
      self.die()
      
      
   def replicate(self):
      if random.randint(0,self.fertility) == 1:
         mutation = self.mutate()
         pos = random.randint(0,7)
         position = positionList[pos]
         if self.x < 30:
            position = (40,0)
         elif self.x > 970:
            position = (-40,0)
         elif self.y <30:
            position = (0, 40)
         elif self.y > 870:
            position = (-40,0)
         new = predator(x = self.x + position[0], y = self.y + position[1], speed = self.speed + mutation[0], sight = self.sight + mutation[1])
   def die(self):
      if random.randint(1, self.lifespan) == 1 or self.lifespan == 0:
         self.destroy()
   def destroy(self):
      canvas.delete(self.shape)
      beingList.remove(self)
   def mutate(self):
      x = random.randint(1,30)
      y = random.randint(1,30)
      if x == 2:
         speed = .1
      elif x == 1:
         speed = -.1
      else:
         speed = 0
      if y == 1:
         vision = -10
      elif y == 2:
         vision = 10
      else:
         vision = 0
      return speed,vision

   
   
def run():
   y = 1
   counter = 0
   text = canvas.create_text(80, 10, text = "FPS: 0", tag = 'FPS')

   while y == 1 :
      ctime = time.time()
      for being in beingList:
         x = being.move()

      
         if x == False or len(beingList) == 0:
            evaluate()
            y = 2
            break
      canvas.update()
      canvas.delete(text)
      text = canvas.create_text(80, 10, text = "FPS: " + str(int(1/(time.time()-ctime + .0000001))), tag = 'FPS')


      
      if counter % 100 == 0:
         x = evaluate()
         output(x)
         counter = 0
      counter +=1
   canvas.delete('FPS')
   initialize()

def output(evaluation):
   #canvas2.create_line(canvas2.position1, -(evaluation[0]-1)*1000 + 150, canvas2.position1, -((evaluation[0]-1)*1000)+149)  #prey
   #canvas2.create_line(canvas2.position1, -(evaluation[2]-1.19)*1000 + 100, canvas2.position1, -((evaluation[2]-1.19)*1000)+99 , fill = 'red') #predators
   canvas2.create_line(canvas2.position1, -(evaluation[4]) + 100, canvas2.position1, -(evaluation[4])+99)  #prey
   canvas2.create_line(canvas2.position1, -(evaluation[5]) + 100, canvas2.position1, -(evaluation[5])+99, fill = 'red')  #prey

   canvas2.position1+=1
   if evaluation[0] != 1:
      text_file = open("prey.txt", 'a')
      text_file.write(str(evaluation[0]))
      text_file.write("\n")
      text_file.close()
   if str(evaluation[2]) != str(1.1):
      text_file = open("predator.txt", 'a')
      text_file.write(str(evaluation[2]))
      text_file.write("\n")
      text_file.close()
   if evaluation[1] != 150:
      text_file = open("preysight.txt", 'a')
      text_file.write(str(evaluation[1]))
      text_file.write("\n")
      text_file.close()
   if evaluation[3] != 200:
      text_file = open("predatorsight.txt", 'a')
      text_file.write(str(evaluation[3]))
      text_file.write("\n")
      text_file.close()
   if canvas2.position1 == width:
      canvas2.delete(ALL)
      canvas.create_line(0,0,width, 0)
      canvas2.position1 = 0

def evaluate():
   speedcount = 0
   sightcount = 0
   speedcount2 = 0
   sightcount2 = 0
   counter = 0
   counter2 = 0
   for being in beingList:
      if being.type == 'Prey':
         speedcount += being.speed
         sightcount += being.sight
         counter += 1
      elif being.type == 'Predator':
         speedcount2 += being.speed
         sightcount2 += being.sight
         counter2 += 1
#   print('Prey:', counter, '\nPredators:', counter2)
   if counter != 0:  
#      print('Prey Speed', speedcount/counter)
#      print('Prey Sight', sightcount/counter)
      preyspeed = speedcount/counter
      preysight = sightcount/counter
   if counter2 != 0:
#      print('Predator Speed', speedcount2/counter2)
#      print('Predator Sight', sightcount2/counter2)
      predatorspeed = speedcount2/counter2
      predatorsight = sightcount2/counter2
   if counter == 0:
      return[0, 0, predatorspeed, predatorsight]
   elif counter2 == 0:
      return[preyspeed, preysight, 0, 0]
   return [preyspeed, preysight, predatorspeed, predatorsight, counter, counter2]

def average(file):
   total, counter = 0, 0
   file = open(file, 'r')
   for line in file:
      total += float(line)
      counter +=1
   average = total/counter
   return(average)

def return_averages():
   files = ('prey.txt', 'predator.txt', 'preysight.txt', 'predatorsight.txt')
   results = []
   for file in files:
      results.append(average(file))
   return results

def initialize():
   print('start')
   global beingList
   for being in beingList[::-1]:
      being.destroy()
   predatorList, preyList = [], []
   #print(beingList)
   for i in range(20):  #creates 20 prey and predators distributed randomly
      x = random.randrange(100, width-100, 30)
      y = random.randrange(100, height-100, 30)
      if [x, y] not in preyList:
         x = prey(x = random.randrange(100, width-100, 30), y = random.randrange(100, height-100, 30))
      if 2*i & 3 == 0:
         y = predator(x = random.randrange(100,width-100, 30), y = random.randrange(100, height-100, 30))
   canvas2.create_line(canvas2.position1, 0, canvas2.position1, 200)
   run()
   
initialize()


#### 



canvas.after(10,run)

canvas.mainloop()

