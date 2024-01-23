#!/usr/bin/python3
"""This module contains two classes that represent a node and a singly linked
list."""


class Node:
    """A class that represents a node of a singly linked list.

    Attributes:
        __data (int): The data stored in the node.
        __next_node (Node): The next node in the list.
    """

    def __init__(self, data, next_node=None):
        """Initializes a node object with data and next_node.

        Args:
            data (int): The data stored in the node.
            next_node (Node, optional): The next node in the list.
            Defaults to None.

        Raises:
            TypeError: If data is not an integer or next_node is not a Node or
            None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Returns the data of the node.

        Returns:
            int: The data of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data of the node.

        Args:
            value (int): The new data of the node.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Returns the next node of the node.

        Returns:
            Node: The next node of the node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next node of the node.

        Args:
            value (Node): The new next node of the node.

        Raises:
            TypeError: If value is not a Node or None.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A class that represents a singly linked list.

    Attributes:
        __head (Node): The head of the list.
    """

    def __init__(self):
        """Initializes a singly linked list object with an empty head.

        Args:
            None
        """
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position in the
        list (increasing order).

        Args:
            value (int): The data of the new node.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and current.next_node.data < (
                    value):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Returns a string representation of the list.

        Returns:
            str: A string that contains the data of each node in the list,
            one per line.
        """
        result = ""
        current = self.__head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result[:-1]
