# Data Structures: Lists, Tuples

# Learning Objectives

* What are lists and how to use them
* What are the differences and similarities between strings and lists
* What are the most common methods of lists and how to use them
* How to use lists as stacks and queues
* What are list comprehensions and how to use them
* What are tuples and how to use them
* When to use tuples versus lists
* What is a sequence
* What is tuple packing
* What is sequence unpacking
* What is the `del` statement and how to use it

# Tasks

## Print a list of integers

Write a function that prints all integers of a list.

* Prototype: `def print_list_integer(my_list=[]):`
* Format: one integer per line. See example
* You are not allowed to import any module
* You can assume that the list only contains integers
* You are not allowed to cast integers into strings
* You have to use `str.format()` to print integers

**Solution:** [0-print_list_integer.py](https://github.com/Bakugo90/alx-higher_level_programming/blob/main/0x03-python-data_structures/0-print_list_integer.py)

```
$ amonkeyprogrammer@ubuntu:~/0x03$ cat 0-main.py
#!/usr/bin/python3
print_list_integer = __import__('0-print_list_integer').print_list_integer

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)

$ amonkeyprogrammer@ubuntu:~/0x03$ ./0-main.py
1
2
3
4
5
$ amonkeyprogrammer@ubuntu:~/0x03$
```

## Secure access to an element in a list

Write a function that retrieves an element from a list like in C.

* Prototype: `def element_at(my_list, idx):`
* If `idx` is negative, the function should return `None`
* If `idx` is out of range (> of number of element in `my_list`), the function should return `None`
* You are not allowed to import any module
* You are not allowed to use `try/except`

**Solution:** [1-element_at.py](https://github.com/Bakugo90/alx-higher_level_programming/blob/main/0x03-python-data_structures/1-element_at.py)

```
$ amonkeyprogrammer@ubuntu:~/0x03$ cat 1-main.py
#!/usr/bin/python3
element_at = __import__('1-element_at').element_at

my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

$ amonkeyprogrammer@ubuntu:~/0x03$ ./1-main.py
Element at index 3 is 4
$ amonkeyprogrammer@ubuntu:~/0x03$
```