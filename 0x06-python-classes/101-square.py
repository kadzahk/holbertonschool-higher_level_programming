#!/usr/bin/python3
""" Coordinates of a square """


class Square:
    """define variables and methods"""

    def __init__(self, size=0, position=(0, 0)):
        """initialize attributes"""
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int) and value >= 0:
            self.__size = value
        elif not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) and len(value) is 2 and\
           value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """define area method, evaluate square area"""
        return self.__size ** 2

    def my_print(self):
        """define my_print method, printing of a square"""
        if self.__size is 0:
            print('')
        else:
            if self.__position[1] > 0:
                for k in range(self.__position[1]):
                    print('')
            for j in range(self.__size):
                if self.__position[0] > 0:
                    for h in range(self.__position[0]):
                        print(' ', end='')
                for i in range(self.__size):
                    print('#', end='')
                print('')

    def __str__(self):
        """define special __str__ method for printing a square
        when print(self) is called"""
        pri = ''
        if self.__size is 0:
            return pri
        else:
            if self.__position[1] > 0:
                for k in range(self.__position[1]):
                    pri += '\n'
            for j in range(self.__size):
                if self.__position[0] > 0:
                    for h in range(self.__position[0]):
                        pri += ' '
                for i in range(self.__size):
                    pri += '#'
                if j is not self.__size - 1:
                    pri += '\n'
            return pri
