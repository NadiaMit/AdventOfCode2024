![](https://img.shields.io/badge/stars_⭐-34-yellow)
![](https://img.shields.io/badge/days_completed_📅-15-blue)
![](https://img.shields.io/badge/days_half_completed_🌗-4-white)

# Advent of Code 2024 in Python [![Python](https://skillicons.dev/icons?i=python)](https://skillicons.dev)

This is my try on the Advent of code of 2024 challanges in Python.

<!-- I managed to complete 13 days (some only part 1) and got a total of 25 stars. -->

## Structure

- `main.py` - file: this file provides code to automatically create the needed files for each day and run the code.
- `days` - folder: the code for each day will be in the days folder as a `dayX.py` file.
- `inputs` - folder: all my input data for each day is saved the inputs folder as a `inputX.txt` file. I also have a `test.txt` file, that I use for the example input of each days puzzle.
- `helpers` - folder: contains my `helpers.py` and `template.py` files. The helper files has some functions to read the input data an I am pretty sure, I will add some other helping functions if I see that puzzles will need some generic functionality more than once. And the template file is my base for every days puzzle.

## Create a Day

To create a new day you can run the following command:

`python main.py create <day>`

where `<day>` is the number of the day you want to create.

This will create a new file in the `days` folder called `day<day>.py` (with the content of the `template.py` file is existend) and a new file in the `inputs` folder called `input<day>.txt`.

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
