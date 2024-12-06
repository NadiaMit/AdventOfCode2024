import sys

sys.path.insert(1, sys.path[0].replace("days", "helpers"))
import helpers as helpers

# get daily input
day = helpers.get_current_day(__file__)
isTest = sys.argv[-1] == "test"
input = helpers.read_input(day, test=isTest)

area_map = [list(line) for line in input]

# code for both parts

def turn_right(direction):
  [x, y] = direction
  # clockwise rotation of 90 degrees
  return [-y, x]

def in_bound(x, y):
  return 0 <= x < len(area_map[0]) and 0 <= y < len(area_map)

# find the guards starting position in the area
start_pos = [0, 0]
start_dir = [0, -1]
for y in range(len(area_map)):
    start = area_map[y].index('^') if '^' in area_map[y] else -1
    if start != -1:
      start_pos = [start, y]
      break

# part 1
position = start_pos
direction = start_dir

visited = {(position[0], position[1])}
# follow the path of the guard until they leave the map
while True:
  [x, y] = [position[0] + direction[0], position[1] + direction[1]]
  
  # check if next position is outside the map
  if not in_bound(x, y):
    break
  
  # if there is no obstacle, move
  if area_map[y][x] != '#':
    position = [x, y]
    visited.add((x, y))
  # otherwise, turn right
  else:
    direction = turn_right(direction)

result_part_1 = len(visited)

# part 2
result_part_2 =  0

# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") #4939
print(f"Part 2: {result_part_2}")