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
warehouse = {}
robot = 0
moves = []
convert_moves = False
for y, line in enumerate(input):
  if line == '':
    convert_moves = True
    continue

  for x, char in enumerate(line):
    if convert_moves:
      if char == "^":
        moves.append(-1j)
      elif char == "v":
        moves.append(1j)
      elif char == "<":
        moves.append(-1)
      elif char == ">":
        moves.append(1)
    else:
      warehouse[x + (y * 1j)] = char
      if char == '@':
        robot = x + (y * 1j)

def move_boxes(box, move):
  new_box = box + move
  if warehouse[new_box] == '#':
    return False
  elif warehouse[new_box] == '.':
    warehouse[box] = '.'
    warehouse[new_box] = 'O'
    return True
  elif warehouse[new_box] == 'O' and move_boxes(new_box, move):
    warehouse[box] = '.'
    warehouse[new_box] = 'O'
    return True
  return False

for move in moves:
  can_move = False
  # if the robot walks into a wall, check the next move
  if warehouse[robot + move] == '#':
    continue
  # if the robot walks into a box, check if it can be pushed away or check the next move
  if warehouse[robot + move] == 'O':
    can_move = move_boxes(robot + move, move)
    if not can_move:
      continue
  # else move the robot in the direction
  warehouse[robot] = '.'
  robot += move
  warehouse[robot] = '@'


# part 1
result_part_1 = 0
for key, value in warehouse.items():
  if value == 'O':
    result_part_1 += round(100 * key.imag + key.real)

# part 2
result_part_2 =  0

# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") #1552879
print(f"Part 2: {result_part_2}")
print(f"Duration: {time.time() - start_time} seconds")