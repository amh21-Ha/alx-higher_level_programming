#!/usr/bin/python3
class Node:
    """A node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Instantiation with data and next_node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Property to retrieve data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Property setter to set data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Property to retrieve next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Property setter to set next_node"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A singly linked list"""

    def __init__(self):
        """Simple instantiation"""
        self.head = None

    def __str__(self):
        """Print the entire list in stdout, one node number by line"""
        result = ""
        current = self.head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result[:-1]

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position in the list (increasing order)"""
        new_node = Node(value)
        if self.head is None or self.head.data >= value:
            # Insert at the beginning
            new_node.next_node = self.head
            self.head = new_node
        else:
            # Insert in the middle or at the end
            current = self.head
            while current.next_node and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
