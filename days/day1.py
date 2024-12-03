import sys

sys.path.insert(1, sys.path[0].replace("days", "helpers"))
import helpers as helpers

# get daily input
day = helpers.get_current_day(__file__)
isTest = sys.argv[-1] == "test"
input = helpers.read_input(day, test=isTest)

# code for both parts
left_list = []
right_list = []
for line in input:
  line = line.split()
  left_list.append(int(line[0]))
  right_list.append(int(line[1]))

result_part_1 = 0
result_part_2 =  0

left_list.sort()
right_list.sort()

for i in range(len(left_list)):
  # part 1
  result_part_1 += abs(left_list[i] - right_list[i])
  
  # part 2
  result_part_2 += left_list[i] * right_list.count(left_list[i])


# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") #3569916
print(f"Part 2: {result_part_2}") #26407426