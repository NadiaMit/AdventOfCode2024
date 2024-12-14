import os
import re
import sys
import time
from functools import reduce
from operator import mul

from PIL import Image

sys.path.insert(1, sys.path[0].replace("days", "helpers"))
import helpers as helpers

# get daily input
day = helpers.get_current_day(__file__)
isTest = sys.argv[-1] == "test"
input = helpers.read_input(day, test=isTest)

# start timer for whole day puzzle after reading the input
start_time = time.time()

# code for both parts
HEIGHT = 103
WIDTH = 101

class Robot:
  def __init__(self, p, v):
    self.position = p
    self.velocity = v
  
  def move(self):
    # get new positions for the robot
    new_x = self.position[0] + self.velocity[0]
    new_y = self.position[1] + self.velocity[1]
    
    # if out of bounds, jump to the other side
    new_x %= WIDTH
    new_y %= HEIGHT
    
    # update the position
    self.position = (new_x, new_y)

def print_robots(robots, second):
  unique_robots = set([robot.position for robot in robots])
  grid = []

  for y in range(HEIGHT):
    row = []
    for x in range(WIDTH):
      if (x, y) in unique_robots:
        row.append((255, 255, 255))
      else:
        row.append((0, 0, 0))
    grid.append(row)

  image = Image.new("RGB", (WIDTH, HEIGHT))
  pixels = [pixel for row in grid for pixel in row]
  image.putdata(pixels)

  image.save(f"./robots/{second}.jpg", "JPEG")

robots = []
pattern = re.compile(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)")
for line in input:
  match = pattern.match(line)
  px, py, vx, vy = map(int, match.groups())
  robots.append(Robot((px, py), (vx, vy)))

tree_pos = 7709
for i in range(10000):
  for robot in robots:
    robot.move()
  if i+1 == tree_pos:
    print_robots(robots, i+1)

x_bound = WIDTH // 2
y_bound = HEIGHT // 2

quadrants = [0,0,0,0]
for robot in robots:
  x,y = robot.position
  # check if in quadrant 1
  if x < x_bound and y < y_bound:
    quadrants[0] += 1
  # check if in quadrant 2
  elif x > x_bound and y < y_bound:
    quadrants[1] += 1
  # check if in quadrant 3
  elif x < x_bound and y > y_bound:
    quadrants[2] += 1
  # check if in quadrant 4
  elif x > x_bound and y > y_bound:
    quadrants[3] += 1

result_part_1 = reduce(mul, quadrants)
result_part_2 = tree_pos

# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") #230435667
print(f"Part 2: {result_part_2}") #7709
print(f"Duration: {time.time() - start_time} seconds")