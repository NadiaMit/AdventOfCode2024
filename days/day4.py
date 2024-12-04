import sys

sys.path.insert(1, sys.path[0].replace("days", "helpers"))
import helpers as helpers

# get daily input
day = helpers.get_current_day(__file__)
isTest = sys.argv[-1] == "test"
input = helpers.read_input(day, test=isTest)

# code for both parts
xmas = "XMAS"
mas = "MAS"

def string_check(to_check, check):
  return to_check == check or to_check == check[::-1]

def xmas_count(data, row, col):
  height = len(data)
  width = len(data[0])
  xmas_count = 0
  mas_count = 0
  checks = []
  
  # horizontal check
  if col + 3 < width:
    checks.append(data[row][col:col+4])
  
  # vertical check
  if row + 3 < height:
    checks.append(str.join('',[data[row+i][col] for i in range(0,4)]))
  
  # diagonal check
  # top left to bottom right
  if row + 3 < height and col + 3 < width:
    checks.append(str.join('', [data[row+i][col+i] for i in range(0,4)]))

  # top right to bottom left
  if row + 3 < height and col - 3 >= 0:
    checks.append(str.join('', [data[row+i][col-i] for i in range(0,4)]))
  
  for check in checks:
    xmas_count += int(string_check(check, xmas))
  
  # mas in form of X count
  if row + 2 < height and col + 2 < width:
    # top left to bottom right
    right = str.join('', [data[row+i][col+i] for i in range(0,3)])
    right_check = string_check(right, mas)
    
    # top right to bottom left
    left = str.join('', [data[row+i][col+2-i] for i in range(0,3)])
    left_check = string_check(left, mas)
    
    if right_check and left_check:
      mas_count += 1
  
  return [xmas_count, mas_count]


result_part_1 = 0
result_part_2 =  0
for row in range(len(input)):
  for col in range(len(input[row])):
    count = xmas_count(input, row, col)
    result_part_1 += count[0]
    result_part_2 += count[1]


# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") #2613
print(f"Part 2: {result_part_2}") #1905