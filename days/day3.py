import re
import sys
import time

sys.path.insert(1, sys.path[0].replace("days", "helpers"))
import helpers as helpers

# get daily input
day = helpers.get_current_day(__file__)
isTest = sys.argv[-1] == "test"
input = helpers.read_input(day, split_lines=False,  test=isTest)

# start timer for whole day puzzle after reading the input
start_time = time.time()

# code for both parts
def multiply(mul):
  numbers = mul.replace("mul(", "").replace(")", "").split(",")
  return int(numbers[0]) * int(numbers[1])

instructions = re.findall(r"mul\([\d]{1,3},[\d]{1,3}\)|don't\(\)|do\(\)", input)

allowed = True
result_part_1 = 0
result_part_2 =  0

for ins in instructions:
  if ins.startswith("mul"):
    product = multiply(ins)
    result_part_1 += product
    if allowed:
      result_part_2 += product
  else:
    allowed = True if ins.startswith("do()") else False


# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") #167090022
print(f"Part 2: {result_part_2}") #89823704
print(f"Duration: {time.time() - start_time} seconds")