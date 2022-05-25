#!/usr/bin/python3
""" Singly linked list """


class Node:
    """define variables and methods"""

    def __init__(self, data, next_node=None):
        """initialize attibute"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """define variables and methods """

    def __init__(self):
        """initialize attibute"""
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value, None)
        temp = self.__head
        if not self.__head:
            self.__head = new_node
            return
        if temp.data > value:
            new_node.next_node = temp
            self.__head = new_node
            return
        while temp.next_node is not None:
            if temp.next_node.data > value:
                break
            temp = temp.next_node
        new_node.next_node = temp.next_node
        temp.next_node = new_node
        return

    def __str__(self):
        """define special __str__ method for printing the list values when print(self) is called """
        list_values = ''
        temp = self.__head
        while temp is not None:
            list_values += str(temp.data)
            if temp.next_node is not None:
                list_values += '\n'
            temp = temp.next_node
        return list_values
