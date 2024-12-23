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

def evolve(secret):
  secret ^= (secret * 64) %16777216
  secret ^= (secret // 32) %16777216
  secret ^= (secret * 2048) %16777216
  return secret

# part 1
result_part_1 = 0
for secret in initial_numbers:
  result_part_1 += [secret := evolve(secret) for _ in range(2000)][-1]

# part 2
result_part_2 =  0

# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") #20071921341
print(f"Part 2: {result_part_2}")
print(f"Duration: {time.time() - start_time} seconds")