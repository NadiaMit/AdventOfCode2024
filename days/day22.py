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
initial_numbers = list(map(int, input))

def mix(secret, value):
  return secret ^ value

def prune(value):
  return value % 16777216

# part 1
result_part_1 = 0
for secret in initial_numbers:
  new_secret = secret
  for i in range(2000):
    new_secret = prune(mix(new_secret, new_secret * 64))
    new_secret = prune(mix(new_secret, new_secret // 32))
    new_secret = prune(mix(new_secret, new_secret * 2048))
  
  result_part_1 += new_secret

# part 2
result_part_2 =  0

# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") #20071921341
print(f"Part 2: {result_part_2}")
print(f"Duration: {time.time() - start_time} seconds")