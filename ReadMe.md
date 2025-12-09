![](https://img.shields.io/badge/stars_⭐-41-yellow)
![](https://img.shields.io/badge/days_completed_📅-18-blue)
![](https://img.shields.io/badge/days_half_completed_🌗-5-white)

# Advent of Code 2024 in Python [![Python](https://skillicons.dev/icons?i=python)](https://skillicons.dev)

This is my try on the Advent of code of 2024 challanges in Python.

## My Progress 41/50⭐

- Day 1 - [Historian Hysteria](https://adventofcode.com/2024/day/1): ⭐⭐
- Day 2 - [Red-Nosed Reports](https://adventofcode.com/2024/day/2): ⭐⭐
- Day 3 - [Mull It Over](https://adventofcode.com/2024/day/3): ⭐⭐
- Day 4 - [Ceres Search](https://adventofcode.com/2024/day/4): ⭐⭐
- Day 5 - [Print Queue](https://adventofcode.com/2024/day/5): ⭐⭐
- Day 6 - [Guard Gallivant](https://adventofcode.com/2024/day/6): ⭐⭐
- Day 7 - [Bridge Repair](https://adventofcode.com/2024/day/7): ⭐⭐
- Day 8 - [Resonant Collinearity](https://adventofcode.com/2024/day/8): ⭐⭐
- Day 9 - [Disk Fragmenter](https://adventofcode.com/2024/day/9): ⭐⭐
- Day 10 - [Hoof It](https://adventofcode.com/2024/day/10): ⭐⭐
- Day 11 - [Plutonian Pebbles](https://adventofcode.com/2024/day/11): ⭐⭐
- Day 12 - [Garden Groups](https://adventofcode.com/2024/day/12): ⭐
- Day 13 - [Claw Contraption](https://adventofcode.com/2024/day/13): ⭐⭐
- Day 14 - [Restroom Redoubt](https://adventofcode.com/2024/day/14): ⭐⭐
- Day 15 - [Warehouse Woes](https://adventofcode.com/2024/day/15): ⭐
- Day 16 - [Reindeer Maze](https://adventofcode.com/2024/day/16): ⭐
- Day 17 - [Chronospatial Computer](https://adventofcode.com/2024/day/17): ⭐⭐
- Day 18 - [RAM Run](https://adventofcode.com/2024/day/18): ⭐⭐
- Day 19 - [Linen Layout](https://adventofcode.com/2024/day/19): ⭐⭐
- ...
- Day 22 - [Monkey Market](https://adventofcode.com/2024/day/22): ⭐⭐
- Day 23 - [LAN Party](https://adventofcode.com/2024/day/23): ⭐⭐
- Day 24 - [Crossed Wires](https://adventofcode.com/2024/day/24): ⭐
- Day 25 - [Code Chronicle](https://adventofcode.com/2024/day/25): ⭐

## Structure

- `main.py` - file: this file provides code to automatically create the needed files for each day and run the code.
- `days` - folder: the code for each day will be in the days folder as a `dayX.py` file.
- `inputs` - folder: all my input data for each day is saved the inputs folder as a `dayX.txt` file. I also have a `test.txt` file, that I use for the example input of each days puzzle.
- `helpers` - folder: contains my `helpers.py` and `template.py` files. The helper files has some functions to read the input data an I am pretty sure, I will add some other helping functions if I see that puzzles will need some generic functionality more than once. And the template file is my base for every days puzzle.

## Create a Day

To create a new day you can run the following command:

`python main.py create <day>`

where `<day>` is the number of the day you want to create.

This will create a new file in the `days` folder called `day<day>.py` (with the content of the `template.py` file is existend) and a new file in the `inputs` folder called `day<day>.txt`.

(You can also create the files by hand if you want of course)

## Run Days

There are two ways to run a day:

### 1. Run from main.py

Simply run the following command:

`python main.py run <day> [test]`

where `<day>` is the number of the day you want to run and `[test]` is an optional parameter to run the day with the test input file otherwise it will automatically use the day's input file.
<br><br><br>
Example for day1 with day1 input file:

`python main.py run 1`

Example for day1 with the test input:

`python main.py run 1 test`

### 2. Run from the day file

Simply run the wanted days file with python:

`python .\days\day<day>.py [test]`

where `<day>` is the number of the day you want to run and `[test]` is an optional parameter to run the day with the test input file otherwise it will automatically use the day's input file.
<br><br><br>
Example for day1 with day1 input file:

`python .\days\day1.py`

Example for day1 with the test input:

`python .\days\day1.py test`
