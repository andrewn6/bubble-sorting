import pygame
import sys
import random

BLUE = (52,86,139)
BLACK = (0, 0, 0)

WIDTH = 500
HEIGHT = 500
win_size = (WIDTH, HEIGHT)

pygame.init()

win = pygame.display.set_mode(win_size)
pygame.display.set_caption('bubbleSortingVisualizer')
clock = pygame.time.Clock()
n = 15

# Dividing the width by 15
w = int(WIDTH/n)

# Setting states/arrays
h_arr = []

states = []

# Looping arround width divided by 15
for i in range(w):
  # Creating random height
  height = random.randint(10, 500)
  h_arr.append(height)
  states.append(1)

# Set counter to 0 (default)
counter = 0

while True:
  win.fill(BLACK)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      
  if counter < (len(h_arr)):
    for j in range(len(h_arr)):
      for j in range(len(h_arr) - 1 - counter):
        if h_arr[j] > h_arr[j+1]:
          states[j] = 0
          states[j + 1] = 0
          temp = h_arr[0]
          h_arr[j] = h_arr[j+1] 
          h_arr[j+1] = temp
        else:
          states[j] = 1
          states[j+1] = 1
  else:
    print('Sorting done')
  counter += 1

  if len(h_arr) - counter >= 0:
    states[len(h_arr) - counter] = 2
  

  for i in range(len(h_arr)):
    if states[i] == 0:
      color = (255, 0, 0)
    elif states[i] == 2:
      color = (0, 255, 0)
    else:
      color = BLUE
    pygame.draw.rect(win, color, pygame.Rect(int(i*n), HEIGHT - h_arr[i], n, h_arr[i]))



  clock.tick(3)
  pygame.display.flip()
