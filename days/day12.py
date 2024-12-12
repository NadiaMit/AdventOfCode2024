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
area_map = [list(x) for x in input]

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def flood_fill(start_pos, region):
  queue = [start_pos]
  visited = set([start_pos])
  perimeter = 0
  
  while queue:
    node = queue.pop(0)
    
    for direction in directions:
      new_node = (node[0] + direction[0], node[1] + direction[1])
      
      # if the new node is in the map, not visited and part of the region add it to the queue and visited set
      if helpers.in_bounds(new_node, area_map) and area_map[new_node[0]][new_node[1]] == region:
        if new_node not in visited:
          queue.append(new_node)
          visited.add(new_node)
      # otherwise increment the perimeter
      else:
        perimeter += 1
  
  # mark visited nodes with '#'
  for node in visited:
    area_map[node[0]][node[1]] = '#'
  
  # return the area and perimeter
  return len(visited), perimeter

# part 1
result_part_1 = 0
for y in range(len(area_map)):
  for x in range(len(area_map[0])):
    region = area_map[y][x]
    if region != '#':
      area, perimeter = flood_fill((y, x), region)
      result_part_1 += (area * perimeter)

# part 2
result_part_2 =  0

# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") #1485656
print(f"Part 2: {result_part_2}")
print(f"Duration: {time.time() - start_time} seconds")