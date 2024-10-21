class Node:
    """A node in a linked list."""
    def __init__(self, data = None, next = None):
        """Initialize the node with data and a reference to the next node."""
        self.data = data
        self.next = next


class LinkedList():
    """A linked list implementation."""
    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None
        self.tail = None
    
    def push_front(self, data):
        """Removes and returns the data from the node at the beginning of the linked list.

        Returns:
        - The data from the removed node, or None if the list is empty.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
          new_node.next = self.head
          self.head = new_node
    
    def pop_front(self):
        if self.head is None:
            return None
        ret_data = self.head.data
        self.head = self.head.next
        return ret_data
    
    def push_back(self, data):
        """Inserts a new node with the given data at the end of the linked list.

        Args:
        - data: The data to be added to the new node.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node

    def pop_back(self):
        """Removes and returns the data from the node at the end of the linked list.

        Returns:
        - The data from the removed node, or None if the list is empty.
        """
        if self.head is None:
            return None
        if self.head.next is None:
            ret_data = self.head.data
            self.head = None
            self.tail = None
            return ret_data
        index_node = self.head
        while index_node.next.next is not None:
            index_node = index_node.next
        ret_data = index_node.next.data
        index_node.next = None
        self.tail = index_node
        return ret_data

    def get_size(self):
        """Returns the number of nodes in the linked list.

        Returns:
        - The number of nodes in the linked list.
        """
        index_node = self.head
        count = 0
        while index_node != None:
            count += 1
            index_node = index_node.next
        return count


    def __str__(self):
        """Returns a string representation of the linked list."""
        ret_str = ""
        index_node = self.head
        while index_node != None:
            ret_str += f"{index_node.data} "
            index_node = index_node.next
        ret_str = ret_str.rstrip(" ")
        return ret_str
