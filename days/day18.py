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
WIDTH = 71 #71
HEIGHT = 71 #71
start = 0 + 0j
end = (WIDTH-1) + (HEIGHT-1) * 1j
num_bytes = 1024

corrupted_bytes = []
for line in input:
  x,y = line.split(",")
  corrupted_bytes.append(int(x) + int(y) * 1j)


def bfs(start, end, corrupted_bytes, num_bytes):
  # node, cost
  queue = [(start, 0)]
  visited = {}
  # north, south, east, west
  directions = [-1j, 1j, 1, -1]

  while queue:
    # get the current node, steps and cost
    node, cost = queue.pop(0)
    
    # if node is already visited and has a lower cost, skip current node
    if node in visited and visited[node] <= cost:
      continue
    # add current node to visited with the cost
    visited[node] = cost
    
    # move in all directions if the new node is not a wall
    for d in directions:
      new_node = node + d
      x, y = int(new_node.real), int(new_node.imag)
      if 0 <= x < WIDTH and 0 <= y < HEIGHT and new_node not in corrupted_bytes[:num_bytes]:
        queue.append((new_node, cost+1))
  
  return visited[end] if end in visited else None

# part 1
result_part_1 = bfs(start, end, corrupted_bytes, num_bytes)

# part 2
low, high = num_bytes, len(corrupted_bytes)

while low < high:
  mid = (low + high) // 2
  
  end_reached = bfs(start, end, corrupted_bytes, mid)
  
  if end_reached is not None:
    low = mid + 1
  else:
    high = mid
  
problem_byte = corrupted_bytes[low-1]
x,y = int(problem_byte.real), int(problem_byte.imag)
result_part_2 = f"{x},{y}"

# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") #432
print(f"Part 2: {result_part_2}") #56,27
print(f"Duration: {time.time() - start_time} seconds")