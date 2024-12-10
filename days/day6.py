import sys
import time

sys.path.insert(1, sys.path[0].replace("days", "helpers"))
import helpers as helpers

# get daily input
day = helpers.get_current_day(__file__)
isTest = sys.argv[-1] == "test"
input = helpers.read_input(day, test=isTest)

# start timer for whole day puzzle after reading the input
start_time = time.time()

# code for both parts
area_map = [list(line) for line in input]

def turn_right(direction):
  [x, y] = direction
  # clockwise rotation of 90 degrees
  return [-y, x]

def in_bound(x, y):
  return 0 <= x < len(area_map[0]) and 0 <= y < len(area_map)

def is_loop(obs_x, obs_y, position, direction):
  new_obstacle = (obs_x, obs_y)
  direction = turn_right(direction)
  visited = {(position[0], position[1], direction[0], direction[1])}
  
  while True:
    [x, y] = [position[0] + direction[0], position[1] + direction[1]]
    
    # if we run outside the map, we are not in a loop
    if not in_bound(x, y):
      return False
    
    if area_map[y][x] == '#' or (x, y) == new_obstacle:
      direction = turn_right(direction)
      continue
    
    # if we have visited this position before, we are in a loop
    if (x, y, direction[0], direction[1]) in visited:
      return True
    
    # add the position to the visited set
    visited.add((x, y, direction[0], direction[1]))
    position = [x, y]

# find the guards starting position in the area
position = [0, 0]
direction = [0, -1]
for y in range(len(area_map)):
    start = area_map[y].index('^') if '^' in area_map[y] else -1
    if start != -1:
      position = [start, y]
      break

visited = {(position[0], position[1])}
added = 0
# follow the path of the guard until they leave the map
while True:
  [x, y] = [position[0] + direction[0], position[1] + direction[1]]
  
  # check if next position is outside the map
  if not in_bound(x, y):
    break
  
  # turn right if the next position is a wall
  if area_map[y][x] == '#':
    direction = turn_right(direction)
    continue
  
  if (x, y) not in visited and is_loop(x, y, position, direction):
    added += 1
  
  # go forward
  position = [x, y]
  visited.add((x, y))


result_part_1 = len(visited)
result_part_2 =  added

# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") #4939
print(f"Part 2: {result_part_2}") #1434
print(f"Duration: {time.time() - start_time} seconds")