import sys
import time

sys.path.insert(1, sys.path[0].replace("days", "helpers"))
import helpers as helpers

# get daily input
day = helpers.get_current_day(__file__)
isTest = sys.argv[-1] == "test"
input = helpers.read_input(day, split_lines=False, test=isTest)

# start timer for whole day puzzle after reading the input
start_time = time.time()

# code for both parts
stones = input.split(' ')

for _ in range(25):
  new_stones = []
  for i in range(len(stones)):
    # if stone has 0, replace with 1
    if stones[i] == '0':
      new_stones.append('1')
    # if stone has even number of digits, split in half
    elif len(stones[i]) % 2 == 0:
      half = len(stones[i]) // 2
      left = stones[i][:half]
      right = stones[i][half:].lstrip('0') or '0'
      new_stones.append(left)
      new_stones.append(right)
    # else multiply by 2024
    else:
      new_stones.append(str(int(stones[i]) * 2024))
  
  stones = new_stones

result_part_1 = len(stones)
result_part_2 = 0

# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") #235850
print(f"Part 2: {result_part_2}")
print(f"Duration: {time.time() - start_time} seconds")