from array_deque import ArrayDeque
from my_linked_list import LinkedList

class Stack:
    """A simple stack implementation using an ArrayDeque as the underlying container."""
    def __init__(self):
        """Initialize an empty stack."""
        self.container = ArrayDeque()

    def push(self, data):
        """Push the given data onto the stack.

        Args:
        - data: The data to be pushed onto the stack.
        """
        self.container.push_back(data)
    
    def pop(self):
        """Pop and return the top element from the stack.

        Returns:
        - The top element of the stack.
        """
        return self.container.pop_back()
    
    def get_size(self):
        """Get the current size of the stack.

        Returns:
        - The number of elements in the stack.
        """
        return self.container.get_size()

    def __str__(self):
        """Return a string representation of the stack.

        Returns:
        - A string representation of the stack.
        """
        return str(self.container)
