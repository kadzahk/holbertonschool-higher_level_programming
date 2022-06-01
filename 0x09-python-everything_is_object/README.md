# 0x09. Python - Everything is object

<p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/252/r_208403_QPSN8.jpg" alt="" style=""><br></p>

## Learning Objectives

<h3>General</h3>

<ul>
<li>Why Python programming is awesome</li>
<li>What is an object</li>
<li>What is the difference between a class and an object or instance</li>
<li>What is the difference between immutable object and mutable object</li>
<li>What is a reference</li>
<li>What is an assignment</li>
<li>What is an alias</li>
<li>How to know if two variables are identical</li>
<li>How to know if two variables are linked to the same object</li>
<li>How to display the variable identifier (which is the memory address in the CPython implementation)</li>
<li>What is mutable and immutable</li>
<li>What are the built-in mutable types</li>
<li>What are the built-in immutable types</li>
<li>How does Python pass variables to functions</li>
</ul>

## Requirements

<h3>Python Scripts</h3>
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

<h3><code>.txt</code> Answer Files</h3>
<ul>
<li>Only one line</li>
<li>No Shebang</li>
<li>All your files should end with a new line</li>
</ul>

- All files are created and executed on Ubuntu 20.04 LTS using Python3 (version 3.8.10)

## Tasks

### [0. Who am I?](./0-answer.txt)

- What function would you use to print the type of an object?

---

### [1. Where are you?](./1-answer.txt)

- How do you get the variable identifier (which is the memory address in the CPython implementation)?

---

### [2. Right count](./2-answer.txt)

- In the following code, do a and b point to the same object?
  Answer with Yes or No.

```python
>>> a = 89
>>> b = 100
```

---

### [3. Right count =](./3-answer.txt)

- In the following code, do a and b point to the same object?
  Answer with Yes or No.

```python
>>> a = 89
>>> b = 89
```

---

### [4. Right count =](./4-answer.txt)

- In the following code, do a and b point to the same object?
  Answer with Yes or No.

```python
>>> a = 89
>>> b = a
```

---

### [5. Right count =+](./5-answer.txt)

- In the following code, do a and b point to the same object?
  Answer with Yes or No.

```python
>>> a = 89
>>> b = a + 1
```

---

### [6. Is equal](./6-answer.txt)

- What do these 3 lines print?

```python
>>> s1 = "Holberton"
>>> s2 = s1
>>> print(s1 == s2)
```

---

### [7. Is the same](./7-answer.txt)

- What do these 3 lines print?

```python
>>> s1 = "Holberton"
>>> s2 = s1
>>> print(s1 is s2)
```

---

### [8. Is really equal](./8-answer.txt)

- What do these 3 lines print?

```python
>>> s1 = "Holberton"
>>> s2 = "Holberton"
>>> print(s1 == s2)
```

---

### [9. Is really the same](./9-answer.txt)

- What do these 3 lines print?

```python
>>> s1 = "Holberton"
>>> s2 = "Holberton"
>>> print(s1 is s2)
```

---

### [10. And with a list, is it equal](./10-answer.txt)

- What do these 3 lines print?

```python
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3]
>>> print(l1 == l2)
```

---

### [11. And with a list, is it the same](./11-answer.txt)

- What do these 3 lines print?

```python
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3]
>>> print(l1 is l2)
```

---

### [12. And with a list, is it really equal](./12-answer.txt)

- What do these 3 lines print?

```python
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
```

---

### [13. And with a list, is it really the same](./13-answer.txt)

- What do these 3 lines print?

```python
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
```

---

### [14. List append](./14-answer.txt)

- What does this script print?

```python
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
```

---

### [15. List add](./15-answer.txt)

- What does this script print?

```python
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
```

---

### [16. Integer incrementation](./16-answer.txt)

- What does this script print?

```python
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
```

---

### [17. List incrementation](./17-answer.txt)

- What does this script print?

```python
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
```

---

### [18. List assignation](./18-answer.txt)

- What does this script print?

```python
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
```

---

### [19. Copy a list object](./19-copy_list.py)

- Write a function def copy_list(l): that returns a copy of a list.
  - The input list can contain any type of objects
  - Your file should be maximum 3-line long (no documentation needed)
  - You are not allowed to import any module

```
guillaume@ubuntu:~/0x09$ cat 19-main.py
```

```python
#!/usr/bin/python3
copy_list = __import__('19-copy_list').copy_list

my_list = [1, 2, 3]
print(my_list)

new_list = copy_list(my_list)

print(my_list)
print(new_list)

print(new_list == my_list)
print(new_list is my_list)

```

```
guillaume@ubuntu:~/0x09$ ./19-main.py
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]
True
False
guillaume@ubuntu:~/0x09$ wc -l 19-copy_list.py
3 19-copy_list.py
```

---

### [20. Tuple or not?](./20-answer.txt)

- Is a a tuple? Answer with Yes or No.

```python
a = ()
```

---

### [21. Tuple or not?](./21-answer.txt)

- Is a a tuple? Answer with Yes or No.

```python
a = (1, 2)
```

---

### [22. Tuple or not?](./22-answer.txt)

- Is a a tuple? Answer with Yes or No.

```python
* a = (1)
```

---

### [23. Tuple or not?](./23-answer.txt)

- Is a a tuple? Answer with Yes or No.

```python
* a = (1, )
```

---

### [24. Richard Sim's special #0](./24-answer.txt)

- What does this script print?

```python
a = (1)
b = (1)
a is b
```

---

### [25. Richard Sim's special #1](./25-answer.txt)

- What does this script print?

```python
a = (1, 2)
b = (1, 2)
a is b
```

---

### [26. Richard Sim's special #2](./26-answer.txt)

- What does this script print?

```python
a = ()
b = ()
a is b
```

---

### [27. Richard Sim's special #3](./27-answer.txt)

- Will the last line of this script print 139926795932424? Answer with Yes or No.

```python
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
```

---

### [28. Richard Sim's special #4](./28-answer.txt)

- Will the last line of this script print 139926795932424? Answer with Yes or No.

```
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
```

---

### [29. Python3: Mutable, Immutable... everything is object!](https://medium.com/@tuvo1106/everything-is-an-object-8e9de11c49a9)

- Write a blog post about everything you just learned / this project is covering. Your blog post should be articulated this way (one paragraph per item):
  - introduction
  - id and type
  - mutable objects
  - immutable objects
  - why does it matter and how differently does Python treat mutable and immutable objects
  - how arguments are passed to functions and what does that imply for mutable and immutable objects

---

### [30. #pythonic](./100-magic_string.py)

- Write a function magic_string() that returns a string “Holberton” n times the number of the iteration (see code):
  - Your file should be maximum 4-line long (no documentation needed)

```
guillaume@ubuntu:~/0x09$ cat 100-main.py
```

```python
#!/usr/bin/python3
magic_string = __import__('100-magic_string').magic_string

for i in range(10):
    print(magic_string())

```

```
guillaume@ubuntu:~/0x09$ ./100-main.py | cat -e
Holberton$
Holberton, Holberton$
Holberton, Holberton, Holberton$
Holberton, Holberton, Holberton, Holberton$
Holberton, Holberton, Holberton, Holberton, Holberton$
Holberton, Holberton, Holberton, Holberton, Holberton, Holberton$
Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton$
Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton$
Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton$
Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton$
guillaume@ubuntu:~/0x09$ wc -l 100-magic_string.py
4 100-magic_string.py
```

---

### [31. Low memory cost](./101-locked_class.py)

- Write a class LockedClass with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called first_name.

```
guillaume@ubuntu:~/0x09$ cat 101-main.py
```

```python
#!/usr/bin/python3
LockedClass = __import__('101-locked_class').LockedClass

lc = LockedClass()
lc.first_name = "John"
try:
    lc.last_name = "Snow"
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

```

```
guillaume@ubuntu:~/0x09$ ./101-main.py
[AttributeError] 'LockedClass' object has no attribute 'last_name'
```

---

### [32. int 1/3](./103-line1.txt)

- Assuming we are using a CPython implementation of Python3 with default options/configuration:
  - How many int objects are created by the execution of the first line of the script? (./103-line1.txt)
  - How many int objects are created by the execution of the second line of the script (./103-line2.txt)

```python
a = 1
b = 1
```

---

### [33. int 2/3](./104-line1.txt)

- Assuming we are using a CPython implementation of Python3 with default options/configuration:
  - How many int objects are created by the execution of the first line of the script? (./104-line1.txt)
  - How many int objects are created by the execution of the second line of the script (./104-line2.txt)
  - After the execution of line 3, is the int object pointed by a deleted? Answer with Yes or No (./104-line3.txt)
  - After the execution of line 4, is the int object pointed by b deleted? Answer with Yes or No (./104-line4.txt)
  - How many int objects are created by the execution of the last line of the script (./104-line5.txt)

```python
a = 1024
b = 1024
del a
del b
c = 1024
```

---

### [34. int 3/3](./105-line1.txt)

- Assuming we are using a CPython implementation of Python3 with default options/configuration:
  - Before the execution of line 2 (print("Love")), how many int objects have been created and are still in memory? (105-line1.txt)

```python
print("I")
print("Love")
print("Python")
```

---

### [35. Clear strings ](./106-line1.txt)

- Assuming we are using a CPython implementation of Python3 with default options/configuration (For answers with numbers use integers, don’t spell out the word):
  - How many string objects are created by the execution of the first line of the script? (./106-line1.txt)
  - How many string objects are created by the execution of the second line of the script (./106-line2.txt)
  - After the execution of line 3, is the string object pointed by a deleted? Answer with Yes or No (./106-line3.txt)
  - After the execution of line 4, is the string object pointed by b deleted? Answer with Yes or No (./106-line4.txt)
  - How many string objects are created by the execution of the last line of the script (./106-line5.txt)

```python
a = "HBTN"
b = "HBTN"
del a
del b
c = "HBTN"
```

---


## Author

- **Juan Manuel Muñoz Rincon** - Kadzahk[![M](https://upload.wikimedia.org/wikipedia/fr/thumb/c/c8/Twitter_Bird.svg/30px-Twitter_Bird.svg.png)](https://twitter.com/kadzahk)