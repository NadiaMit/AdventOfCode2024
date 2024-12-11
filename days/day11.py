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
stones_input = input.split(' ')
stones_dict = {}
for i in range(len(stones_input)):
  stones_dict[stones_input[i]] = stones_dict.setdefault(stones_input[i], 0) + 1

def count_stones_blink(stones, blink):
  for _ in range(blink):
    new_stones = {}
    for key, value in stones.items():
      # if stone has 0, replace with 1
      if key == '0':
        new_stones['1'] = new_stones.setdefault('1', 0) + value
      # if stone has even number of digits, split in half
      elif len(key) % 2 == 0:
        half = len(key) // 2
        left = key[:half]
        right = key[half:].lstrip('0') or '0'
        
        new_stones[left] = new_stones.setdefault(left, 0) + value
        new_stones[right] = new_stones.setdefault(right, 0) + value
      # else multiply by 2024
      else:
        times = str(int(key) * 2024)
        new_stones[times] = new_stones.setdefault(times, 0) + value
    
    stones = new_stones
  
  return sum(stones.values())

result_part_1 = count_stones_blink(stones_dict.copy(), 25)
result_part_2 = count_stones_blink(stones_dict.copy(), 75)

# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") #235850
print(f"Part 2: {result_part_2}") #279903140844645
print(f"Duration: {time.time() - start_time} seconds")