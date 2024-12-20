import sys
import time
from functools import lru_cache

sys.path.insert(1, sys.path[0].replace("days", "helpers"))
import helpers as helpers

# get daily input
day = helpers.get_current_day(__file__)
isTest = sys.argv[-1] == "test"
input = helpers.read_input(day, test=isTest)

# start timer for whole day puzzle after reading the input
start_time = time.time()

# code for both parts
patterns = input[0].split(', ')
patterns.sort(key=len, reverse=True)
designs = input[2:]

@lru_cache(maxsize=None)
def check_design(remaining):
  if not remaining:
    return 1
  
  num_arrangements = 0
  for pattern in patterns:
    if remaining.startswith(pattern):
      num_arrangements += check_design(remaining[len(pattern):])
    
  return num_arrangements

result_part_1 = sum(1 for design in designs if check_design(design) > 0)
result_part_2 = sum(check_design(design) for design in designs)

# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") #327
print(f"Part 2: {result_part_2}") #772696486795255
print(f"Duration: {time.time() - start_time} seconds")