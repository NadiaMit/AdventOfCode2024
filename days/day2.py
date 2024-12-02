import math
import sys

sys.path.insert(1, sys.path[0].replace("days", "helpers"))
import helpers as helpers

# get daily input
day = helpers.get_current_day(__file__)
isTest = sys.argv[-1] == "test"
input = helpers.read_input(day, test=isTest)

# code for both parts
reports = [[int(i) for i in line.split()] for line in input]

# part 1
result_part_1 = 0
for report in reports:
  sign = None
  safe = True
  for i in range(len(report)-1):
    diff = report[i] - report[i+1]
    
    if sign is None:
      sign = math.copysign(1, diff)
    elif sign != math.copysign(1, diff):
      safe = False
      break
    
    if abs(diff) < 1 or abs(diff) > 3:
      safe = False
      break

  if safe:
    result_part_1 += 1

# part 2
result_part_2 =  0

# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}")
print(f"Part 2: {result_part_2}")