def read_file(file_path):
  """
  Reads the content of a file.
  """
  with open(file_path, "r") as file:
    return file.read()

def create_file(file_path, file_content = None):
  """
  Creates a file with the given content or an empty file if no content is provided.
  """
  with open(file_path, "w") as file:
    file.write(file_content if file_content else "")

def get_current_day(file_path):
  """
  Extracts the day number from the file path.
  """
  return file_path.split('\\')[-1].split(".")[0].replace("day", "")

def read_input(day, split_lines=True, test=False):
  """
  Reads the input from the current days txt file.
  split_lines: if True, the input will be split by lines [default: True]
  test: if True, the test input will be read [default: False]
  """
  path = f"./inputs/day{day}.txt" if not test else f"./inputs/test.txt"
  input = read_file(path)
  return input.splitlines() if split_lines else input

def in_bounds(pos, map):
  """
  Checks if a position is inside the map.
  """
  y, x = pos
  return 0 <= x < len(map) and 0 <= y < len(map[0])

