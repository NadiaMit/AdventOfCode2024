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

result_part_1 = 0

change_sequences = {}
for secret in initial_numbers:
  secrets = [secret] + [secret := evolve(secret) for _ in range(2000)]
  prices = [price % 10 for price in secrets]
  changes = [prices[i] - prices[i-1] for i in range(1,len(prices))]
  
  # part 1
  result_part_1 += secrets[-1]
  
  # part 2
  seen = set()
  for i in range(len(changes)-3):
    sequence = tuple(changes[i:i+4])
    if sequence not in seen:
      seen.add(sequence)
      change_sequences[sequence] = change_sequences.get(sequence, 0) + prices[i+4]

# part 2
result_part_2 = max(change_sequences.values())

# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") #20071921341
print(f"Part 2: {result_part_2}") #2242
print(f"Duration: {time.time() - start_time} seconds")