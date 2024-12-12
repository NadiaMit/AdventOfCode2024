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
topographic_map = [[int(x) for x in line] for line in input]

def bfs(map, start):
  queue = [(start, [start])]
  # up, down, left, right
  directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
  paths = set()
  ends = set()
  height = 0

  while queue:
    node, path = queue.pop(0)
    height = map[node[0]][node[1]]
    
    if height == 9:
      ends.add(node)
      paths.add(tuple(path))
    
    for y, x in directions:
      new_node = (node[0]+y, node[1]+x)
      if helpers.in_bounds(new_node, map) and map[new_node[0]][new_node[1]] == height+1:
        queue.append((new_node, path+[new_node]))
    
  return len(ends), len(paths)

result_part_1 = 0
result_part_2 =  0
for y in range(len(topographic_map)):
  for x in range(len(topographic_map[y])):
    if topographic_map[y][x] == 0:
      trail_ends, paths = bfs(topographic_map, (y, x))
      result_part_1 += trail_ends
      result_part_2 += paths

# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") #468
print(f"Part 2: {result_part_2}") #966
print(f"Duration: {time.time() - start_time} seconds")