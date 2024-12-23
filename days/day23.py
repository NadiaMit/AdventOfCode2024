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
graph = {}
for line in input:
  com = line.split("-")
  graph.setdefault(com[0], []).append(com[1])
  graph.setdefault(com[1], []).append(com[0])

inter_connected = set()
for node, neighbors in graph.items():
  for neighbor in neighbors:
    common_neighbors = set(graph[node]).intersection(graph[neighbor])
    for shared_node in common_neighbors:
      if node.startswith("t") or neighbor.startswith("t") or shared_node.startswith("t"):
        inter_connected.add(tuple(sorted([node, neighbor, shared_node])))

# part 1
result_part_1 = len(inter_connected)

# part 2
result_part_2 =  0

# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") #1075
print(f"Part 2: {result_part_2}")
print(f"Duration: {time.time() - start_time} seconds")