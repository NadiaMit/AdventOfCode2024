import sys
import time
import re
import math

sys.path.insert(1, sys.path[0].replace("days", "helpers"))
import helpers as helpers

# get daily input
day = helpers.get_current_day(__file__)
isTest = sys.argv[-1] == "test"
input = helpers.read_input(day, test=isTest)

# start timer for whole day puzzle after reading the input
start_time = time.time()

# code for both parts
registers = {}
program = []
pointer = 0

pattern = re.compile(r"Register ([ABC]): (\d+)")
for i in range(len(input[0:3])):
  match = pattern.match(input[i])
  reg = match.group(1)
  val = int(match.group(2))
  registers[reg] = val

program_string = input[4].split(" ")[1]
program_string = program_string.split(",")
for i in range(0, len(program_string), 2):
  program.append((int(program_string[i]), int(program_string[i+1])))

output = []
halt = False
while not halt or pinter < len(program):
  command, value = program[pointer]

  # get new value 
  use_value = value
  if value == 4:
    use_value = registers["A"]
  elif value == 5:
    use_value = registers["B"]
  elif value == 6:
    use_value = registers["C"]
  elif value == 7:
    print("ERROR SHOULD NOT BE HERE")
    break
  
  if command == 0:
    a = registers["A"]
    registers["A"] = math.trunc(a/2**use_value)
    pointer += 1
    
  elif command == 1:
    b = registers["B"]
    # bitwise XOR with value
    registers["B"] = b ^ value
    pointer += 1
    
  elif command == 2:
    registers["B"] = use_value % 8
    pointer += 1
    
  elif command == 3:
    pass
  elif command == 4:
    b = registers["B"]
    c = registers["C"]
    registers["B"] = b ^ c
    pointer += 1
    
  elif command == 5:
    output.append(use_value%8)
    pointer += 1
    
  elif command == 6:
    a = registers["A"]
    registers["B"] = math.trunc(a/2**use_value)
    pointer += 1
    
  elif command == 7:
    a = registers["A"]
    registers["C"] = math.trunc(a/2**use_value)
    pointer += 1


# part 1
result_part_1 = str.join(",", [str(x) for x in output])

# part 2
result_part_2 =  0

# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}")
print(f"Part 2: {result_part_2}")
print(f"Duration: {time.time() - start_time} seconds")