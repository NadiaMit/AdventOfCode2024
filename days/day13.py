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
def solve_equation(button_a, button_b, prize, prize_add = 0):
  x_a, y_a = button_a
  x_b, y_b = button_b
  x_p, y_p = prize
  
  # calculate the number of times i need to press A and B using math
  # prize vector
  p = np.array([[x_p + prize_add], [y_p + prize_add]])
  
  # buttons matrix and calculate the inverse
  M = np.vstack([[y_b, -x_b], [-y_a, x_a]])
  det = x_a * y_b - y_a * x_b
  M_inv = (1/det) * M
  
  # solve equation: (a,b) = M^-1 * p
  result  = M_inv @ p
  a = round(result[0, 0], 2)
  b = round(result[1, 0], 2)
  
  if a.is_integer() and b.is_integer():
    return int(abs(a)*3 + abs(b)*1)
  return 0


result_part_1 = 0
result_part_2 = 0

for i in range(0, len(input), 4):
  button_a = input[i].split(": ")[1].split(', ')
  button_b = input[i + 1].split(": ")[1].split(', ')
  prize = input[i + 2].split(": ")[1].split(', ')
  
  button_a = [int(x.split('+')[1]) for x in button_a]
  button_b = [int(x.split('+')[1]) for x in button_b]
  prize = [int(x.split('=')[1]) for x in prize]
  
  result_part_1 += solve_equation(button_a, button_b, prize)
  result_part_2 += solve_equation(button_a, button_b, prize, 10000000000000)

# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") #33921
print(f"Part 2: {result_part_2}") #82261957837868
print(f"Duration: {time.time() - start_time} seconds")