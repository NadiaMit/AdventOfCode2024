![](https://img.shields.io/badge/stars%20⭐-2-yellow)
![](https://img.shields.io/badge/days%20completed%20📅-1-blue)

# Advent of Code 2024 in Python [![Python](https://skillicons.dev/icons?i=python)](https://skillicons.dev)

This is my try on the Advent of code of 2024 challanges in Python.

<!-- I managed to complete 13 days (some only part 1) and got a total of 25 stars. -->

## Structure

- `days` - folder: the code for each day will be in the days folder as a `dayX.py` file.
- `inputs` - folder: all my input data for each day is saved the inputs folder as a `inputX.txt` file. I also have a `test.txt` file, that I use for the example input of each days puzzle.
- `helpers` - folder: contains my `helpers.py` and `template.py` files. The helper files has some functions to read the input data an I am pretty sure, I will add some other helping functions if I see that puzzles will need some generic functionality more than once. And the template file is my base for every days puzzle.

## Run Days

Simply run the wanted days file with python. (I used `python 3.12`)

This for example runs day1:
`python .\days\day1.py`

For any other wanted day just simply exchange the 1 with the day's number!
If you want to run the day with the test input file, add a `test` to the command:

Example for day1 with the test input:
`python .\days\day1.py test`
