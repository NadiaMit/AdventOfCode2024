import copy
import sys

sys.path.insert(1, sys.path[0].replace("days", "helpers"))
import helpers as helpers

# get daily input
day = helpers.get_current_day(__file__)
isTest = sys.argv[-1] == "test"
input = helpers.read_input(day, test=isTest)

# code for both parts
topographic_map = [[int(x) for x in line] for line in input]

def in_bounds(x, y, map):
  return 0 <= x < len(map[0]) and 0 <= y < len(map)

def flood_fill(map, y, x, height, visited):
  trail_end = 0
  
  if not in_bounds(x, y, map) or map[y][x] != height or (y, x) in visited:
    return trail_end
  
  if map[y][x] == 9:
    visited.add((y, x))
    return trail_end+1
  
  visited.add((y, x))
  
  # up, down, left, right
  new_height = height+1
  trail_end += flood_fill(map, y-1, x, new_height, visited)
  trail_end += flood_fill(map, y+1, x, new_height, visited)
  trail_end += flood_fill(map, y, x-1, new_height, visited)
  trail_end += flood_fill(map, y, x+1, new_height, visited)
    
  return trail_end

result_part_1 = 0
for y in range(len(topographic_map)):
  for x in range(len(topographic_map[y])):
    if topographic_map[y][x] == 0:
      result_part_1 += flood_fill(topographic_map, y, x, 0, set())


# part 2
result_part_2 =  0

# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") #468
print(f"Part 2: {result_part_2}")