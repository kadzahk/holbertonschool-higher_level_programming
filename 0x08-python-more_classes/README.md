# 0x05. Python - Exceptions

## Learning Objectives

<h3>General</h3>

<ul>
<li>Why Python programming is awesome </li>
<li>What is OOP</li>
<li>“first-class everything”</li>
<li>What is a class</li>
<li>What is an object and an instance</li>
<li>What is the difference between a class and an object or instance</li>
<li>What is an attribute</li>
<li>What are and how to use public, protected and private attributes</li>
<li>What is <code>self</code></li>
<li>What is a method</li>
<li>What is the special <code>__init__</code> method and how to use it</li>
<li>What is Data Abstraction, Data Encapsulation, and Information Hiding</li>
<li>What is a property</li>
<li>What is the difference between an attribute and a property in Python</li>
<li>What is the Pythonic way to write getters and setters in Python</li>
<li>What are the special <code>__str__</code> and <code>__repr__</code> methods and how to use them</li>
<li>What is the difference between <code>__str__</code> and <code>__repr__</code></li>
<li>What is a class attribute</li>
<li>What is the difference between a object attribute and a class attribute</li>
<li>What is a class method</li>
<li>What is a static method</li>
<li>How to dynamically create arbitrary new attributes for existing instances of a class</li>
<li>How to bind attributes to object and classes</li>
<li>What is and what does contain <code>__dict__</code> of a class and of an instance of a class</li>
<li>How does Python find the attributes of an object or class</li>
<li>How to use the <code>getattr</code> function</li>
</ul>

## Requirements

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the pycodestyle (version <code>2.8.*</code>)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
</ul>

- All files are created and executed on Ubuntu 20.04 LTS using Python3 (version 3.8.10)

## Tasks

### [0. Simple rectangle](./0-rectangle.py)

- Write an empty class Rectangle that defines a rectangle:

```
guillaume@ubuntu:~/0x08$ cat 0-main.py
```

```python
#!/usr/bin/python3
Rectangle = __import__('0-rectangle').Rectangle

my_rectangle = Rectangle()
print(type(my_rectangle))
print(my_rectangle.__dict__)

```

```
guillaume@ubuntu:~/0x08$ ./0-main.py
<class '0-rectangle.Rectangle'>
{}
```

---

### [1. Real definition of a rectangle](./1-rectangle.py)

- Write a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
  - Private instance attribute: width:
    - property `def width(self)`: to retrieve it
    - property setter `def width(self, value)`: to set it:
      - width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
      - if width is less than 0, raise a ValueError exception with the message width must be >= 0
  - Private instance attribute: height:
    - property `def height(self)`: to retrieve it
    - property setter `def height(self, value)`: to set it:
      - height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
      - if height is less than 0, raise a ValueError exception with the message height must be >= 0
  - Instantiation with optional width and height: `def __init__(self, width=0, height=0)`:

```
guillaume@ubuntu:~/0x08$ cat 1-main.py
```

```python
#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)

```

```sh
guillaume@ubuntu:~/0x08$ ./1-main.py
{'_Rectangle__height': 4, '_Rectangle__width': 2}
{'_Rectangle__height': 3, '_Rectangle__width': 10}
```

---

### [2. Area and Perimeter](./2-rectangle.py)

- Write a class Rectangle that defines a rectangle by: (based on 1-rectangle.py)
  - Public instance method: `def area(self)`: that returns the rectangle area
  - Public instance method: `def perimeter(self)`: that returns the rectangle perimeter:
    - if width or height is equal to 0, perimeter is equal to 0

```
guillaume@ubuntu:~/0x08$ cat 2-main.py
```

```python
#!/usr/bin/python3
Rectangle = __import__('2-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

```

```
guillaume@ubuntu:~/0x08$ ./2-main.py
Area: 8 - Perimeter: 12
--
Area: 30 - Perimeter: 26
```

---

### [3. String representation](./3-rectangle.py)

- Write a class Rectangle that defines a rectangle by: (based on 2-rectangle.py)
  - print() and str() should print the rectangle with the character #: (see example below)
    - if width or height is equal to 0, return an empty string

```
guillaume@ubuntu:~/0x08$ cat 3-main.py
```

```python
#!/usr/bin/python3
Rectangle = __import__('3-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print(str(my_rectangle))
print(repr(my_rectangle))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle)
print(repr(my_rectangle))

```

```
guillaume@ubuntu:~/0x08$ ./3-main.py
Area: 8 - Perimeter: 12
##
##
##
##
<3-rectangle.Rectangle object at 0x7f92a75a2eb8>
--
##########
##########
##########
<3-rectangle.Rectangle object at 0x7f92a75a2eb8>
```

---

### [4. Eval is magic](./4-rectangle.py)

- Write a class Rectangle that defines a rectangle by: (based on 3-rectangle.py)
  - repr() should return a string representation of the rectangle to be able to recreate a new instance by using eval() (see example below)

```
guillaume@ubuntu:~/0x08$ cat 4-main.py
```

```python
#!/usr/bin/python3
Rectangle = __import__('4-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(str(my_rectangle))
print("--")
print(my_rectangle)
print("--")
print(repr(my_rectangle))
print("--")
print(hex(id(my_rectangle)))
print("--")

# create new instance based on representation
new_rectangle = eval(repr(my_rectangle))
print(str(new_rectangle))
print("--")
print(new_rectangle)
print("--")
print(repr(new_rectangle))
print("--")
print(hex(id(new_rectangle)))
print("--")

print(new_rectangle is my_rectangle)
print(type(new_rectangle) is type(my_rectangle))

```

```
guillaume@ubuntu:~/0x08$ ./4-main.py
##
##
##
##
--
##
##
##
##
--
Rectangle(2, 4)
--
0x7f09ebf7cc88
--
##
##
##
##
--
##
##
##
##
--
Rectangle(2, 4)
--
0x7f09ebf7ccc0
--
False
True
```

---

### [5. Detect instance deletion](./5-rectangle.py)

- Write a class Rectangle that defines a rectangle by: (based on 4-rectangle.py)
  - Print the message Bye rectangle... (... being 3 dots not ellipsis) when an instance of Rectangle is deleted

```
guillaume@ubuntu:~/0x08$ cat 5-main.py
```

```python
#!/usr/bin/python3
Rectangle = __import__('5-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

del my_rectangle

try:
    print(my_rectangle)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

```

```
guillaume@ubuntu:~/0x08$ ./5-main.py
Area: 8 - Perimeter: 12
Bye rectangle...
[NameError] name 'my_rectangle' is not defined
```

---

### [6. How many instances](./6-rectangle.py)

- Write a class Rectangle that defines a rectangle by: (based on 5-rectangle.py)
  - Public class attribute number_of_instances:
    - Initialized to 0
    - Incremented during each new instance instantiation
    - Decremented during each instance deletion

```
guillaume@ubuntu:~/0x08$ cat 6-main.py
```

```python
#!/usr/bin/python3
Rectangle = __import__('6-rectangle').Rectangle

my_rectangle_1 = Rectangle(2, 4)
my_rectangle_2 = Rectangle(2, 4)
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
del my_rectangle_1
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
del my_rectangle_2
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))

```

```
guillaume@ubuntu:~/0x08$ ./6-main.py
2 instances of Rectangle
Bye rectangle...
1 instances of Rectangle
Bye rectangle...
0 instances of Rectangle
```

---

### [7. Change representation](./7-rectangle.py)

- Write a class Rectangle that defines a rectangle by: (based on 6-rectangle.py)
  - Public class attribute print_symbol:
    - Initialized to #
    - Used as symbol for string representation
    - Can be any type

```
guillaume@ubuntu:~/0x08$ cat 7-main.py
```

```python
#!/usr/bin/python3
Rectangle = __import__('7-rectangle').Rectangle

my_rectangle_1 = Rectangle(8, 4)
print(my_rectangle_1)
print("--")
my_rectangle_1.print_symbol = "&"
print(my_rectangle_1)
print("--")

my_rectangle_2 = Rectangle(2, 1)
print(my_rectangle_2)
print("--")
Rectangle.print_symbol = "C"
print(my_rectangle_2)
print("--")

my_rectangle_3 = Rectangle(7, 3)
print(my_rectangle_3)

print("--")

my_rectangle_3.print_symbol = ["C", "is", "fun!"]
print(my_rectangle_3)

print("--")

```

```
guillaume@ubuntu:~/0x08$ ./7-main.py
########
########
########
########
--
&&&&&&&&
&&&&&&&&
&&&&&&&&
&&&&&&&&
--
##
--
CC
--
CCCCCCC
CCCCCCC
CCCCCCC
--
['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
--
Bye rectangle...
Bye rectangle...
Bye rectangle...
```

---

### [8. Compare rectangles](./8-rectangle.py)

- Write a class Rectangle that defines a rectangle by: (based on 7-rectangle.py)
  - Static method `def bigger_or_equal(rect_1, rect_2)`: that returns the biggest rectangle based on the area
    - rect_1 must be an instance of Rectangle, otherwise raise a TypeError exception with the message rect_1 must be an instance of Rectangle
    - rect_2 must be an instance of Rectangle, otherwise raise a TypeError exception with the message rect_2 must be an instance of Rectangle
    - Returns rect_1 if both have the same area value

```
guillaume@ubuntu:~/0x08$ cat 8-main.py
```

```python
#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

my_rectangle_1 = Rectangle(8, 4)
my_rectangle_2 = Rectangle(2, 3)

if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")


my_rectangle_2.width = 10
my_rectangle_2.height = 5
if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")

```

```
guillaume@ubuntu:~/0x08$ ./8-main.py
my_rectangle_1 is bigger or equal to my_rectangle_2
my_rectangle_2 is bigger than my_rectangle_1
Bye rectangle...
Bye rectangle...
```

---

### [9. A square is a rectangle](./9-rectangle.py)

- Write a class Rectangle that defines a rectangle by: (based on 8-rectangle.py)
  - Class method `def square(cls, size=0)`: that returns a new Rectangle instance with width == height == size

```
guillaume@ubuntu:~/0x08$ cat 9-main.py
```

```python
#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

my_square = Rectangle.square(5)
print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
print(my_square)

```

```
guillaume@ubuntu:~/0x08$ ./9-main.py
Area: 25 - Perimeter: 20
#####
#####
#####
#####
#####
Bye rectangle...
```

---