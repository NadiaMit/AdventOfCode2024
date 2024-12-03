import re
import sys

sys.path.insert(1, sys.path[0].replace("days", "helpers"))
import helpers as helpers

# get daily input
day = helpers.get_current_day(__file__)
isTest = sys.argv[-1] == "test"
input = helpers.read_input(day, split_lines=False,  test=isTest)

# code for both parts
def multiply(mul):
  numbers = mul.replace("mul(", "").replace(")", "").split(",")
  return int(numbers[0]) * int(numbers[1])


# part 1
result_part_1 = 0

multiplications = re.findall(r"mul\([\d]{1,3},[\d]{1,3}\)", input)
for mul in multiplications:
    result_part_1 += multiply(mul)

# part 2
result_part_2 =  0

instructions = re.findall(r"mul\([\d]{1,3},[\d]{1,3}\)|don't\(\)|do\(\)", input)
allowed = True
for ins in instructions:
  if ins.startswith("mul"):
    if allowed:
      result_part_2 += multiply(ins)
  elif ins.startswith("don't"):
    allowed = False
  else:
    allowed = True



# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") #167090022
print(f"Part 2: {result_part_2}") #89823704