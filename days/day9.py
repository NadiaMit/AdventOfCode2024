import sys

sys.path.insert(1, sys.path[0].replace("days", "helpers"))
import helpers as helpers

# get daily input
day = helpers.get_current_day(__file__)
isTest = sys.argv[-1] == "test"
input = helpers.read_input(day, split_lines=False, test=isTest)

# code for both parts
blocks = [int(x) for x in list(input)]

# part 1
result_part_1 = 0

full_free_string = []
ID = 0
for i in range (0, len(blocks)):
  add = '.'
  if i % 2 == 0:
    add = str(ID)
    ID += 1
  for j in range(0, blocks[i]):
    full_free_string.append(add)

reordered_string = []
insert_numbers = [x for x in full_free_string if x != "."]
for i in range(0, len(insert_numbers)):
  if full_free_string[i] == ".":
    reordered_string.append(insert_numbers.pop())
  else:
    reordered_string.append(full_free_string[i])

for i in range(0, len(reordered_string)):
  result_part_1 += i * int(reordered_string[i])

# part 2
result_part_2 =  0

# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") #6283404590840
print(f"Part 2: {result_part_2}")