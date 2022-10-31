# Almost a Circle

# Learning Objectives

* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* What is `*args` and how to use it
* What is `**kwargs` and how to use it
* How to handle named arguments in a function

# Tasks

## If it's not tested it doesn't work

All your files, classes and methods must be unit tested and be PEP 8 validated.

```
$ amonkeyprogramer@ubuntu:~/$ python3 -m unittest discover tests
...................................................................................
...................................................................................
.......................
----------------------------------------------------------------------
Ran 31 tests in 13.135s

OK
$ amonkeyprogramer@ubuntu:~/$
```

## Base class

Write the first class `Base`:

Create a folder named `models` with an empty file `__init__.py` inside - with this file, the folder will become a Python module

Create a file named `models/base.py`:

* Class `Base`:
    * private class attribute `__nb_objects = 0`
    * class constructor: `def __init__(self, id=None):`:
        * if `id` is not `None`, assign the public instance attribute `id` with this argument value - you can assume `id` is an integer and you don’t need to test the type of it
        * otherwise, increment `__nb_objects` and assign the new value to the public instance attribute `id`
