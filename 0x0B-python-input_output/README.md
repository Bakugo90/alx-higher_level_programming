# Input/Output

# Learning Objectives

* How to open a file
* How to write text in a file
* How to read the full content of a file
* How to read a file line by line
* How to move the cursor in a file
* How to make sure a file is closed after using it
* What is and how to use the [with](https://docs.python.org/3/reference/compound_stmts.html#with) statement
* What is [JSON](https://en.wikipedia.org/wiki/JSON)
* What is serialization
* What is deserialization
* How to convert a Python data structure to a JSON string
* How to convert a JSON string to a Python data structure

# Tasks

## Read file

Write a function that reads a text file (`UTF8`) and prints it to stdout:

* Prototype: `def read_file(filename=""):`
* You must use the `with` statement
* You don’t need to manage `file permission` or `file doesn't exist` exceptions.
* You are not allowed to import any module

**Solution:** [0-read_file.py](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x0B-python-input_output/0-read_file.py)

