import sys
import time

import numpy as np

sys.path.insert(1, sys.path[0].replace("days", "helpers"))
import helpers as helpers

# get daily input
day = helpers.get_current_day(__file__)
isTest = sys.argv[-1] == "test"
input = helpers.read_input(day, test=isTest)

# start timer for whole day puzzle after reading the input
start_time = time.time()

# code for both parts
claw_machines = []
for i in range(0, len(input), 4):
  button_a = input[i].split(": ")[1].split(', ')
  button_b = input[i + 1].split(": ")[1].split(', ')
  prize = input[i + 2].split(": ")[1].split(', ')
  
  button_a = [int(x.split('+')[1]) for x in button_a]
  button_b = [int(x.split('+')[1]) for x in button_b]
  prize = [int(x.split('=')[1]) for x in prize]
  
  claw_machines.append({'A': button_a, 'B': button_b, 'prize': prize})


def solve_equation(claw, position_addition = 0):
  x_a, y_a = claw['A']
  x_b, y_b = claw['B']
  x_p, y_p = claw['prize']
  
  # calculate the number of times i need to press A and B using math
  prize = np.array([x_p + position_addition, y_p + position_addition], dtype=int)
  buttons = np.array([[x_a, x_b], [y_a, y_b]], dtype=int)
  result = np.linalg.solve(buttons, prize)
  
  # round the result if its close enough to an integer since i got values like x.00002 or x.0000000000001 that should be just x
  tolerance = 1e-3
  result = np.where(
    np.abs(result - np.rint(result)) < tolerance, 
    np.rint(result),
    result
  )
  
  a = result[0]
  b = result[1]
  if a.is_integer() and b.is_integer():
    return int(abs(a)*3 + abs(b)*1)
  return 0

result_part_1 = 0
result_part_2 = 0
for claw in claw_machines:
  result_part_1 += solve_equation(claw)
  result_part_2 += solve_equation(claw, 10000000000000)

# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") #33921
print(f"Part 2: {result_part_2}") #82261957837868
print(f"Duration: {time.time() - start_time} seconds")