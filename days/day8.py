import sys

sys.path.insert(1, sys.path[0].replace("days", "helpers"))
import helpers as helpers

# get daily input
day = helpers.get_current_day(__file__)
isTest = sys.argv[-1] == "test"
input = helpers.read_input(day, test=isTest)
antenna_map = [list(line) for line in input]

# code for both parts
def in_bound(x, y):
  return 0 <= x < len(antenna_map[0]) and 0 <= y < len(antenna_map)

def create_antinodes(a, b, part):
  # calculate the difference between the two antennas in x and y direction
  x_diff = a[0] - b[0]
  y_diff = a[1] - b[1]
  
  antinodes = []
  
  if part == 1:
    # calculate the two antinotes that are before and after the two antennas on the line
    antinode = (a[0] + x_diff, a[1] + y_diff)
    if in_bound(antinode[0], antinode[1]):
      antinodes.append(antinode)
    antinode = (b[0] - x_diff, b[1] - y_diff)
    if in_bound(antinode[0], antinode[1]):
      antinodes.append(antinode)
    
  else:
    # calculate all antinodes on the line of the two antennas
    antinodes.append(a)
    i = 1
    while True:
      antinode = (a[0] + (x_diff*i), a[1] + (y_diff*i))
      if not in_bound(antinode[0], antinode[1]):
        break
      antinodes.append(antinode)
      i += 1
    
    i = -1
    while True:
      antinode = (a[0] + (x_diff*i), a[1] + (y_diff*i))
      if not in_bound(antinode[0], antinode[1]):
        break
      antinodes.append(antinode)
      i -= 1
  
  return antinodes 

# save every antenna position in a dictionary
antennas = {}
for y in range(len(antenna_map)):
  for x in range(len(antenna_map[y])):
    if antenna_map[y][x] != ".":
      antennas.setdefault(antenna_map[y][x], []).append((x, y))

antinodes_p1 = set()
antinodes_p2 = set()

for antenna in antennas:
  for i in range(len(antennas[antenna])):
    for j in range(i + 1, len(antennas[antenna])):
      antinodes_p1.update(create_antinodes(antennas[antenna][i], antennas[antenna][j], part=1))
      antinodes_p2.update(create_antinodes(antennas[antenna][i], antennas[antenna][j], part=2))

result_part_1 = len(antinodes_p1)
result_part_2 = len(antinodes_p2)

# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") #323
print(f"Part 2: {result_part_2}") #1077