import sys
from itertools import product

sys.path.insert(1, sys.path[0].replace("days", "helpers"))
import helpers as helpers

# get daily input
day = helpers.get_current_day(__file__)
isTest = sys.argv[-1] == "test"
input = helpers.read_input(day, test=isTest)

# code for both parts
def check_combinations(test, numbers, op_types):
  # this generates all the possible combinations of operations from op_types and then calculates the result based on the operations
  for operations in product(op_types, repeat=len(numbers)-1):
    result = numbers[0]
    for i, op in zip(range(1, len(numbers)), operations):
      if op == "+":
        result += numbers[i]
      elif op == "*":
        result *= numbers[i]
      elif op == '||':
        result = int(f"{result}{numbers[i]}")

    # if the result is the same as the test, return the test value otherwise continue and return 0
    if result == test:
      return test
  return 0


calibrations = []
for line in input:
  parts = line.split(": ")
  calibrations.append((int(parts[0]), [int(x) for x in parts[1].split(" ")]))

result_part_1 = 0
result_part_2 = 0
for test, numbers in calibrations:
  result_part_1 += check_combinations(test, numbers, ["+", "*"])
  result_part_2 += check_combinations(test, numbers, ["+", "*", '||'])


# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") #303876485655
print(f"Part 2: {result_part_2}") #146111650210682