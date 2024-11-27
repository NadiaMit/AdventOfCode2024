
# get current day number
def get_current_day(file_path):
    return file_path.split('\\')[-1].split(".")[0].replace("day", "")

# reads input from the current days txt file
def read_input(day, split_lines=True, test=False):
    path = f"./inputs/day{day}.txt" if not test else f"./inputs/test.txt"
    with open(path, 'r') as file:
        input = file.read()
        return input.splitlines() if split_lines else input