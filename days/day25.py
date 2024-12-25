import sys
import time

sys.path.insert(1, sys.path[0].replace("days", "helpers"))
import helpers as helpers

# get daily input
day = helpers.get_current_day(__file__)
isTest = sys.argv[-1] == "test"
input = helpers.read_input(day, split_lines=False, test=isTest)

# start timer for whole day puzzle after reading the input
start_time = time.time()

# code for both parts
locks = []
keys = []
schemantics = input.split("\n\n")

for schemantic in schemantics:
  lines = schemantic.split("\n")
  colums = [''.join(col[1:6]) for col in zip(*lines)]
  
  # parse locks
  if lines[0] == '#####':
    locks.append([col.count('#') for col in colums])
  # parse keys
  else:
    keys.append([col.count('#') for col in colums])


# part 1
result_part_1 = 0
for lock in locks:
  for key in keys:
    if all([lock[i]+key[i] <= 5 for i in range(5)]):
      result_part_1 += 1

# part 2
result_part_2 =  0

# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") #2840
print(f"Part 2: {result_part_2}")
print(f"Duration: {time.time() - start_time} seconds")