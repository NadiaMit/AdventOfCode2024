import sys

sys.path.insert(1, sys.path[0].replace("days", "helpers"))
import helpers as helpers

# get daily input
day = helpers.get_current_day(__file__)
isTest = sys.argv[-1] == "test"
input = helpers.read_input(day, test=isTest)

map = [list(line) for line in input]

# code for both parts

def turn_right(dir):
  [x, y] = dir
  # from up to right
  if x == 0 and y == -1:
    return [1, 0]
  # from right to down
  if x == 1 and y == 0:
    return [0, 1]
  # from down to left
  if x == 0 and y == 1:
    return [-1, 0]
  # from left to up
  if x == -1 and y == 0:
    return [0, -1]

def check_map_boundaries(x, y):
  return y > 0 and y < len(map)-1 and x > 0 and x < len(map[y])-1

# find the guards starting position in the area
position = [0, 0]
direction = [0, 0]
for y in range(len(map)):
    start = map[y].index('^') if '^' in map[y] else -1
    if start != -1:
      position = [start, y]
      direction = [0, -1]
      map[y][start] = 'X'
      break

guard_left = False
# follow the path of the guard
while not guard_left:
  [x, y] = position
  [dir_x, dir_y] = direction
  
  # as long as the guard does not leave the map or run into an obstacle go straight
  while check_map_boundaries(x, y) and map[y+dir_y][x+dir_x] != '#' :
    x += dir_x
    y += dir_y
    position = [x, y]
    map[y][x] = 'X'
  else:
    # if the guard goes outside the map, stop
    if not check_map_boundaries(x, y):
      guard_left = True
      break
    # if the guard runs into an obstacle, turn right
    else:
      direction = turn_right(direction)

# part 1
result_part_1 = 0
for line in map:
  result_part_1 += line.count('X')

# part 2
result_part_2 =  0

# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") #4939
print(f"Part 2: {result_part_2}")