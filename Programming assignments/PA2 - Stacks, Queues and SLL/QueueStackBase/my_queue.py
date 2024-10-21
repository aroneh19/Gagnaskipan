from array_deque import ArrayDeque
from my_linked_list import LinkedList

class Queue:
    """A simple queue implementation using an ArrayDeque as the underlying container."""
    def __init__(self):
        """Initialize an empty queue."""
        self.container = ArrayDeque()

    def add(self, data):
        """
        Add the given data to the back of the queue.

        Args:
        - data: The data to be added to the queue.
        """
        self.container.push_front(data)
    
    def remove(self):
        """Remove and return the front element from the queue.

        Returns:
        - The front element of the queue.
        """
        return self.container.pop_back()

    def get_size(self):
        """Get the current size of the queue.

        Returns:
        - The number of elements in the queue.
        """
        return self.container.get_size()

    def __str__(self):
        """Return a string representation of the queue.

        Returns:
        - A string representation of the queue.
        """
        return str(self.container)