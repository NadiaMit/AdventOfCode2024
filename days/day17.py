import re
import sys
import time

sys.path.insert(1, sys.path[0].replace("days", "helpers"))
import helpers as helpers

# get daily input
day = helpers.get_current_day(__file__)
isTest = sys.argv[-1] == "test"
input = helpers.read_input(day, split_lines = False, test=isTest)

# start timer for whole day puzzle after reading the input
start_time = time.time()

# code for both parts
reg_a, reg_b, reg_c, *program = map(int, re.findall(r'\d+', input))
original_program = program.copy()
program = [(program[i], program[i+1]) for i in range(0, len(program), 2)]

def run_program(a, b, c):
  pointer = 0
  output = []
  while pointer < len(program):
    command, value = program[pointer]
    use_value = [0,1,2,3,a,b,c][value]
    pointer += 1
    
    match command:
      case 0: a = a >> use_value
      case 1: b = b ^ value
      case 2: b = use_value % 8
      case 3: pointer = value if a != 0 else pointer
      case 4: b = b ^ c
      case 5: output.append(use_value%8)
      case 6: b = a >> use_value
      case 7: c = a >> use_value
  
  return str.join(",", [str(x) for x in output])


# part 1
result_part_1 = run_program(reg_a, reg_b, reg_c)

# part 2
result_part_2 =  0
original_program = str.join(",", [str(x) for x in original_program])

new_a = 0
found = False

while not found:
  for new_a in range(new_a, new_a+8):
    output = run_program(new_a, reg_b, reg_c)
    if original_program.endswith(output):
      if original_program == output:
        result_part_2 = new_a
        found = True
      else:
        new_a = new_a << 3
      break


# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") #7,1,5,2,4,0,7,6,1
print(f"Part 2: {result_part_2}") #37222273957364
print(f"Duration: {time.time() - start_time} seconds")