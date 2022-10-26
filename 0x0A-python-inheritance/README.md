# Python - Inheritance

# Learning Objectives

* What is a superclass, baseclass or parentclass
* What is a subclass
* How to list all attributes and methods of a class or instance
* When can an instance have new attributes
* How to inherit class from another
* How to define a class with multiple base classes
* What is the default class every class inherit from
* How to override a method or attribute inherited from the base class
* Which attributes or methods are available by heritage to subclasses
* What is the purpose of inheritance
* What are, when and how to use `isinstance`, `issubclass`, `type` and `super` built-in functions

# Tasks

## Lookup

Write a function that returns the list of available attributes and methods of an object:

* Prototype: `def lookup(obj):`
* Returns a `list` object
* You are not allowed to import any module

**Solution:** [0-lookup.py](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x0A-python-inheritance/0-lookup.py)

```
$ amonkeyprogrammer@ubuntu:~/0x0A$ cat 0-main.py
#!/usr/bin/python3
lookup = __import__('0-lookup').lookup

class MyClass1(object):
    pass

class MyClass2(object):
    my_attr1 = 3
    def my_meth(self):
        pass

print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))

$ amonkeyprogrammer@ubuntu:~/0x0A$ ./0-main.py
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'my_attr1', 'my_meth']
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
$ amonkeyprogrammer@ubuntu:~/0x0A$
```

## My list

Write a class `MyList` that inherits from `list`:

* Public instance method: `def print_sorted(self):` that prints the list, but sorted (ascending sort)
* You can assume that all the elements of the list will be of type `int`
* You are not allowed to import any module

**Solution:** [1-my_list.py](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x0A-python-inheritance/1-my_list.py), [tests/1-my_list.txt](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x0A-python-inheritance/tests/1-my_list.txt)

```
$ amonkeyprogrammer@ubuntu:~/0x0A$ cat 1-main.py
#!/usr/bin/python3
MyList = __import__('1-my_list').MyList

my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
print(my_list)
my_list.print_sorted()
print(my_list)

$ amonkeyprogrammer@ubuntu:~/0x0A$ ./1-main.py
[1, 4, 2, 3, 5]
[1, 2, 3, 4, 5]
[1, 4, 2, 3, 5]
$ amonkeyprogrammer@ubuntu:~/0x0A$
```

## Exact same object

Write a function that returns `True` if the object is exactly an instance of the specified class ; otherwise `False`.

* Prototype: `def is_same_class(obj, a_class):`
* You are not allowed to import any module