"""Implementation of a Singly Linked List Data structure in Python"""

class Node:
    """
    An Object for storing a single node of a linked list.
    Models two attributes - data and the link to the next node in the list
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"<Node data: {self.data}>"


class LinkedList:
    """
    Singly linked list
    """

    def __init__(self):
        """
        Initializes the LinkedList data structure, sets the head to none
        """
        self.head = None

    def is_empty(self):
        """
        Checks if the list is empty and returns a True or False
        """
        return self.head is None

    def size(self):
        """
        Returns the number of nodes in the list.
        Takes O(n) time - Linear time
        """
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count

    def add(self, data):
        """
        Add a new node to containing data at the head of the list.
        Takes O(n) time - Constant time
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
        Search for the first node containing data that matches the key
        Return the node or 'None' if not found

        Takes O(n) time - Linear time
        """
        current = self.head

        while current:
            if current.data == key:
                return current
            current = current.next_node
        return None

    def insert(self, data, index):
        """
        Inserts a new Node containing data at index position
        Insertion takes O(1) time but finding the node at the 
        insertion point takes O(n) time.

        Takes an overall O(n) time
        """
        if index == 0:
            self.add(data)

        assert index <= self.size(), f"IndexError: '{index}' is not a valid index in list'"

        if index > 0:
            new_node = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new_node
            new_node.next_node = next_node

    def remove(self, key):
        """
        Removes Node containing data that matches the key
        Returns the node or None if the key doesn't exists
        Takes O(n) time
        """

        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        return current

    def pop(self, index=0):
        """
        Removes a Node using the index position and returns the removed node data
        It removes or pops the first node by default
        """

        current = self.head

        assert index <= self.size() - 1, f"IndexError: '{index}' is not a valid index in list'"

        if index == 0:
            self.head = current.next_node

        if index > 0:
            position = index

            while position > 1:
                current = current.next_node
                position -= 1

            previous = current
            current  = current.next_node
            previous.next_node = current.next_node
        return current

    def get_by_index(self, index): # personal Implementation of get node at index
        current = None

        assert index <= self.size() - 1, f"IndexError: '{index}' is not a valid index in list'"

        if index == 0:
            return self.head

        if index > 0:
            position = index
            current = self.head

            while position > 0:
                current = current.next_node
                position -= 1
        return current

    def node_at_index(self, index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0

            while position < index:
                current = current.next_node
                position += 1

            return current

    def __repr__(self):
        """
        Returns a string representation of the list.
        Takes O(n) time
        """
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append(f"[Head: {current.data}]")
            elif current.next_node is None:
                nodes.append(f"[Tail: {current.data}]")
            else:
                nodes.append(f"{current.data}")
            current = current.next_node
        if nodes:
            return '-> '.join(nodes)

        return '[Null]'

# TODO - add type casting for LinkedList e.g convert list, tuple or string to linked list
