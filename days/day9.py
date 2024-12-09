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

block_info = []
full_free = []
ID = 0
for i in range (0, len(blocks)):
  add = '.'
  if i % 2 == 0:
    add = str(ID)
    ID += 1
  for _ in range(0, blocks[i]):
    full_free.append(add)
  block_info.append((add, blocks[i]))

reordered = []
insert_numbers = [x for x in full_free if x != "."]
for i in range(0, len(insert_numbers)):
  if full_free[i] == ".":
    reordered.append(insert_numbers.pop())
  else:
    reordered.append(full_free[i])

for i in range(0, len(reordered)):
  result_part_1 += i * int(reordered[i])

# part 2
result_part_2 =  0
reordered = block_info

for i in range(len(reordered)-1, 0, -1):
  block, amount = reordered[i]
  if block == '.':
    continue
  for j in range(0, i):
    check_block, check_amount = reordered[j]
    if check_block == '.' and check_amount >= amount:
      
      reordered[i] = ('.', amount)
      reordered = reordered[:j] + [(block, amount)] + reordered[j:]
      rest_amount = check_amount - amount
      reordered[j+1] = ('.', rest_amount)
      break


new_blocks = []
for block, amount in reordered:
  for _ in range(0, amount):
    new_blocks.append(block)
for i in range(0, len(new_blocks)):
  if new_blocks[i] != '.':
    result_part_2 += i * int(new_blocks[i])


# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") #6283404590840
print(f"Part 2: {result_part_2}") #6304576012713