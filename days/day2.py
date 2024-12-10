import math
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
reports = [[int(i) for i in line.split()] for line in input]

def check_is_safe(report):
  diffs = [report[i] - report[i+1] for i in range(len(report)-1)]
  # check if all the diffs are between 1 and 3
  amount_safe = all([0 < abs(diff) < 4 for diff in diffs])
  # check the signs are all the same
  sign_safe = all([math.copysign(1, diff) == math.copysign(1, diffs[0]) for diff in diffs])
  
  return amount_safe and sign_safe

result_part_1 = 0
result_part_2 = 0
for report in reports:
  safe = check_is_safe(report)

  if safe:
    result_part_1 += 1
    result_part_2 += 1
  else:
    for i in range(len(report)):
      copy = report.copy()
      copy.pop(i)
      if check_is_safe(copy):
        result_part_2 += 1
        break


# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") #670
print(f"Part 2: {result_part_2}") #700
print(f"Duration: {time.time() - start_time} seconds")