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
race_map = {}
start = 0
end = 0

for y, line in enumerate(input):
  for x, char in enumerate(line):
    if char == "S":
      start = x + y * 1j
    if char == "E":
      end = x + y * 1j
    race_map[x + y * 1j] = char
    

def calculate_new_cost(cost, prev_step, new_step):
  # add 1 for a step
  cost += 1
  # if there is a direction change, add 1000
  if new_step != prev_step:
    cost += 1000
  return cost

def bfs(map, start, end):
  # node, path steps, cost with east as first step
  queue = [(start, [1], 0)]
  visited = {}
  # north, south, east, west
  directions = [-1j, 1j, 1, -1]
  
  while queue:
    # get the current node, steps and cost
    node, steps, cost = queue.pop(0)
    
    # if node is already visited and has a lower cost, skip current node
    if node in visited and visited[node] <= cost:
      continue
    # add current node to visited with the cost
    visited[node] = cost
    
    # move in all directions if the new node is not a wall
    for d in directions:
      new_node = node + d
      if new_node in map and map[new_node] != "#":
        # calculate the new moving cost using the previous cost and step and current step
        new_cost = calculate_new_cost(cost, steps[-1], d)
        queue.append((new_node, steps + [d], new_cost))
    
  return visited[end]

# part 1
result_part_1 = bfs(race_map, start, end)

# part 2
result_part_2 =  0

# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") #122492
print(f"Part 2: {result_part_2}")
print(f"Duration: {time.time() - start_time} seconds")