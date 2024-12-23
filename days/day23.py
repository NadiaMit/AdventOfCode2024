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

connections = set()
for node, neighbors in graph.items():
  for neighbor in neighbors:
    common_neighbors = set(graph[node]).intersection(graph[neighbor])
    for shared_node in common_neighbors:
      connections.add(tuple(sorted([node, neighbor, shared_node])))

# part 1
result_part_1 = 0
for connection in connections:
  if any([x.startswith("t") for x in connection]):
    result_part_1 += 1

# part 2
biggest_connections = connections.copy()

while True:
  new_connections = set()
  for clique in biggest_connections:
    for node in graph:
      if node not in clique and all(node in graph[neighbor] for neighbor in clique):
        new_clique = tuple(sorted(list(clique) + [node]))
        new_connections.add(new_clique)
  
  if len(new_connections) == 0:
    break
  biggest_connections = new_connections
  
result_part_2 = (',').join(max(biggest_connections, key=lambda x: len(x)))

# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") #1075
print(f"Part 2: {result_part_2}") #az,cg,ei,hz,jc,km,kt,mv,sv,sx,wc,wq,xy
print(f"Duration: {time.time() - start_time} seconds")