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
class Gate:
  def __init__(self, inputs, operand, output):
    self.inputs = inputs
    self.operand = operand
    self.output = output
  
  def operate(self, inputs):
    output_value = 0
    if self.operand == "AND":
      output_value = inputs[0] & inputs[1]
    elif self.operand == "OR":
      output_value = inputs[0] | inputs[1]
    elif self.operand == "XOR":
      output_value = inputs[0] ^ inputs[1]
    return self.output, output_value

index = input.index("")

values = {variable: int(value) for variable, value in [line.split(": ") for line in input[:index]]}

gates = []
for gate in input[index+1:]:
  parts = gate.split(" -> ")
  operation = parts[0].split(" ")
  gates.append(Gate([operation[0], operation[2]], operation[1], parts[1]))

while gates:
  gate = gates.pop(0)
  if all([input in values for input in gate.inputs]):
    inputs = [values[input] for input in gate.inputs]
    output, value = gate.operate(inputs)
    values[output] = value
  else:
    gates.append(gate)
    continue


values = dict(sorted(values.items()))
z_values = [str(value) for key, value in values.items() if key.startswith("z")]
z_values.reverse()
z_values = ('').join(z_values)

# part 1
result_part_1 = int(z_values, 2)

# part 2
result_part_2 =  0

# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") #45121475050728
print(f"Part 2: {result_part_2}")
print(f"Duration: {time.time() - start_time} seconds")