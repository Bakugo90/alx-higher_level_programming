#!/usr/bin/python3
"""struct data programming"""


class Node:
    """strcut data node"""

    def __init__(self, data, next_node=None):
        """init method"""
        if not (isinstance(data, int)):
            raise TypeError("data must be an integer")
        elif isinstance(next_node, Node) is False and next_node != None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__data = data
            self.__next_node = next_node

    @property
    def data(self):
        """getters for data"""
        return self.__data

    @data.setter
    def data(self, value):
        """setters for data"""
        if not (isinstance(value, int)):
            raise TypeError("data must be an integer")
        return self.__data

    @property
    def next_node(self):
        """getter next node for struct"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter the next node for struct"""
        if isinstance(value, Node) is False and value != None:
            raise TypeError("next_node must be a Node object")
        return self.__next_node

    def __str__(self):
        return str(self.__data)


class SinglyLinkedList:
    """ singly linked list"""

    def __init__(self):
        """init method for singly linked list"""
        self.__head = None


    def __str__(self):
        """string methode"""
        head = self.__head
        n = ""
        while head != None:
            n = str(head)
            if head.__next_node != None:
                n += "\n"
            head = head.__next_node
        return n


    def sorted_node(self):
        """sort the node"""
        head = self.__head
        if head is None:
            return
        while head is not None:
            tmp = head
            s = head
            while s is not None:
                if tmp.__data > s.__data:
                    head.__data = s.__data
                    s.__data = tmp.__data
                s = s.__next_node
            head = head.__next_node


    def sorted_insert(self, value):
        """insertion in the node sorted"""
        self.sorted_node()
        head = self.__head
        prev = self.__head
        new = Node(value, None)
        if head is None:
            head = new
        else:
            while new.__data >= head.__data:
                prev = head
                head = head.__next_data
            
            new.next_node(prev.__next_node)
            prev.__next_node = new

        return new
