# Exceptions

# Learning Objectives

* What’s the difference between errors and exceptions
* What are exceptions and how to use them
* When do we need to use exceptions
* How to correctly handle an exception
* What’s the purpose of catching exceptions
* How to raise a builtin exception
* When do we need to implement a clean-up action after an exception* 

# Tasks

## Safe list printing

Write a function that prints `x` elements of a list.

* Prototype: `def safe_print_list(my_list=[], x=0):`
* `my_list` can contain any type (integer, string, etc.)
* All elements must be printed on the same line followed by a new line.
* `x` represents the number of elements to print
* `x` can be bigger than the length of `my_list`
* Returns the real number of elements printed
* You have to use `try: / except:`
* You are not allowed to import any module
* You are not allowed to use `len()`

**Solution:** [0-safe_print_list.py](https://github.com/bakugo90/alx-higher_level_programming/blob/main/0x05-python-exceptions/0-safe_print_list.py)

$ amonkeyprogrammer@ubuntu:~/0x05$ cat 0-main.py
#!/usr/bin/python3
safe_print_list = __import__('0-safe_print_list').safe_print_list

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))

$ amonkeyprogrammer@ubuntu:~/0x05$ ./0-main.py
12
nb_print: 2
12345
nb_print: 5
12345
nb_print: 5
$ amonkeyprogrammer@ubuntu:~/0x05$
```

## Safe printing of an integers list

Write a function that prints an integer with `"{:d}".format()`.

* Prototype: `def safe_print_integer(value):`
* `value` can be any type (integer, string, etc.)
* The integer should be printed followed by a new line
* Returns `True` if `value` has been correctly printed (it means the `value` is an integer)
* Otherwise, returns `False`
* You have to use `try: / except:`
* You have to use `"{:d}".format()` to print as integer
* You are not allowed to import any module
* You are not allowed to use `type()`

**Solution:** [1-safe_print_integer.py](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x05-python-exceptions/1-safe_print_integer.py)

```
