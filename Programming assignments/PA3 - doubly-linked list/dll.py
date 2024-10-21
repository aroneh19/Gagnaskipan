
class Node:
    def __init__(self, data = None, prev = None, next = None):
        """Initialize a new Node.

        Parameters:
        - data: The data to be stored in the node.
        - prev: Reference to the previous node in the doubly linked list.
        - next: Reference to the next node in the doubly linked list.
        """
        self.data = data
        self.prev = prev
        self.next = next

class DLL():
    def __init__(self):
        """Initialize a new Doubly Linked List.

        The list is initialized with a head and a tail node, both pointing to each other.
        """
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.curr = self.head.next
        self.size = 0
    
    def insert(self, data):
        """Insert a new node with the given data after the current node.

        Parameters:
        - data: The data to be stored in the new node.
        """
        new_node = Node(data, self.curr.prev, self.curr)

        if self.size == 0:
            self.head.next = self.tail.prev = new_node
        else:
            new_node.prev.next = self.curr.prev = new_node

        self.size += 1
        self.curr = new_node

    def remove(self):
        """Remove the current node from the doubly linked list."""
        if self.curr.data is None:
            return 
                
        self.curr.prev.next = self.curr.next
        self.curr.next.prev = self.curr.prev

        self.size -= 1        
        self.curr = self.curr.next
    
    def get_value(self):
        """Get the data stored in the current node.

        Returns:
        - The data in the current node or None if the current node is empty.
        """
        if self.curr != None:
            return self.curr.data
        return None

    def move_to_next(self):
        """Move the current node to the next node in the list."""
        if self.curr != self.tail:
            self.curr = self.curr.next

    def move_to_prev(self):
        """Move the current node to the previous node in the list."""
        if self.curr.prev.data is not None:
            self.curr = self.curr.prev

    def move_to_pos(self, pos):
        """Move the current node to the specified position in the list.

        Parameters:
        - pos: The position to move the current node to.
        """
        if pos < 0 or pos > self.size + 1:
            return

        current = self.head.next
        for i in range(self.size + 1):
            if i == pos:
                self.curr = current
                break
            current = current.next

    def clear(self):
        """Clear the doubly linked list by resetting the head, tail, and current node."""
        self.head.next = self.tail
        self.tail.prev = self.head
        self.curr = self.head.next
        self.size = 0

    def get_first_node(self):
        """Get the first node in the doubly linked list.

        Returns:
        - The first node in the list.
        """
        return self.head.next

    def get_last_node(self):
        """Get the last node in the doubly linked list.

        Returns:
        - The last node in the list.
        """
        return self.tail.prev

    def partition(self, low, high):
        """Partition the list between the low and high nodes based on their data values.

        Parameters:
        - low: The starting node for partitioning.
        - high: The ending node for partitioning.
        """
        if self.size == 0:
            return
        node = low.next
        while node != high.next:
            if node.data < low.data:
                self.curr = node
                value = self.curr.data
                self.remove()
                self.curr = low
                self.insert(value)
            node = node.next
        self.curr = low

    def sort(self):
        """Sort the doubly linked list using the quicksort algorithm."""
        if self.size > 0:
            self.quicksort(self.get_first_node(), self.get_last_node())
        self.curr = self.head.next

    def quicksort(self, low, high):
        """Recursively apply quicksort to the sublist between the low and high nodes.

        Parameters:
        - low: The starting node of the sublist.
        - high: The ending node of the sublist.
        """
        high_c = high.next
        low_c = low.prev
        self.partition(low, high)
        low = low_c.next
        high = high_c.prev
        if low is not self.curr:
            self.quicksort(low, self.curr.prev)
        if high is not self.curr:
            self.quicksort(self.curr.next, high)

    def __len__(self):
        """Get the size of the doubly linked list.

        Returns:
        - The number of nodes in the list.
        """
        return self.size

    def __str__(self):
        """Return a string representation of the doubly linked list.

        Returns:
        - A string containing the data values of the nodes in the list.
        """
        ret_str = ""
        index_node = self.head.next
        for _ in range(self.size):
            ret_str += f"{index_node.data} "
            index_node = index_node.next
        return ret_str[:-1]

if __name__ == "__main__":
    dll = DLL()
    dll.insert("A")
    dll.insert("C")
    dll.insert("B")
    print(dll)