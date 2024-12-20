import sys
import time
import re

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

halt = False
while not halt:
  command, value = program[pointer]
  
  if command == 0:
    pass
  elif command == 1:
    pass
  elif command == 2:
    pass
  elif command == 3:
    pass
  elif command == 4:
    pass
  elif command == 5:
    pass
  elif command == 6:
    pass
  elif command == 7:
    pass
  
  halt = True

# part 1
result_part_1 = 0

# part 2
result_part_2 =  0

# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}")
print(f"Part 2: {result_part_2}")
print(f"Duration: {time.time() - start_time} seconds")