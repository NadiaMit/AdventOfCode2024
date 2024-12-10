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
rules_input, updates = input.split("\n\n")
rules_input = rules_input.splitlines()
updates = [u.split(',') for u in updates.splitlines()]

# load rules into a dictionary based on the first number
rules = {}
for rule in rules_input:
  rule = rule.split("|")
  rules.setdefault(rule[0], []).append(rule[1])


def check_update(update):
  update_len = len(update)
  incorrectly = []
  
  for i in range(update_len):
    for j in range(i+1, update_len):
      # check if the current page is not in one of the later pages rules
      if update[j] in list(rules.keys()) and update[i] in rules[update[j]]:
        incorrectly = [i, j]
        return False, incorrectly
  return True, incorrectly

def switch_elemenst(list, elements):
  list[elements[0]], list[elements[1]] = list[elements[1]], list[elements[0]]
  return list

result_part_1 = 0
result_part_2 =  0
for update in updates:
  update_len = len(update)
  rule_check, incorrectly = check_update(update)
  
  if rule_check:
    middle = update[update_len//2]
    result_part_1 += int(middle)
  else:
    while not rule_check:
      update = switch_elemenst(update, incorrectly)
      rule_check, incorrectly = check_update(update)
    middle = update[update_len//2]
    result_part_2 += int(middle)


# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") #4872
print(f"Part 2: {result_part_2}") #5564
print(f"Duration: {time.time() - start_time} seconds")