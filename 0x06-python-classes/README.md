# Classes and Objects

# Learning Objectives

* What is OOP
* “first-class everything”
* What is a class
* What is an object and an instance
* What is the difference between a class and an object or instance
* What is an attribute
* What are and how to use public, protected and private attributes
* What is self
* What is a method``
* What is the special `__init__` method and how to use it
* What is Data Abstraction, Data Encapsulation, and Information Hiding
* What is a property
* What is the difference between an attribute and a property in Python
* What is the Pythonic way to write getters and setters in Python
* How to dynamically create arbitrary new attributes for existing instances of a class
* How to bind attributes to object and classes
* What is the `__dict__` of a class and/or instance of a class and what does it contain
* How does Python find the attributes of an object or class
* How to use the `getattr` function

# Tasks

## My first square

Write an empty class `Square` that defines a square:

* You are not allowed to import any module

**Solution:** [0-square.py](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x06-python-classes/0-square.py)

```
$ amonkeyprogrammer@ubuntu:~/0x06$ cat 0-main.py
#!/usr/bin/python3
Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)

$ amonkeyprogrammer@ubuntu:~/0x06$ ./0-main.py
<class '0-square.Square'>
{}
$ amonkeyprogrammer@ubuntu:~/0x06$
```

## Square with size

Write a class `Square` that defines a square by: (based on `0-square.py`)

* Private instance attribute: `size`
* Instantiation with `size` (no type/value verification)
* You are not allowed to import any module

**Solution:** [1-square.py](https://github.com/Bakugo/alx-higher_level_programming/blob/main/0x06-python-classes/1-square.py)