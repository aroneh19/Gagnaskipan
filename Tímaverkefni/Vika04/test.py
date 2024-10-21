class Queue:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.size = 0
        self.front = 0  # Index for the front element
        self.rear = 0   # Index for the rear element
        self.arr = [None] * self.capacity
    
    def __str__(self):
        return_string = ""
        current = self.front
        for i in range(self.size):
            return_string += f"{self.arr[current]}, "
            current = (current + 1) % self.capacity
        return return_string.rstrip(", ")
    
    def add(self, value):
        self.resize()
        self.arr[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1

    def remove(self):
        if self.size == 0:
            raise ValueError("Queue is empty")
        
        removed_value = self.arr[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return removed_value
    
    def resize(self):
        if self.size == self.capacity:
            self.capacity *= 2
            new_arr = [None] * self.capacity

            current = self.front
            for i in range(self.size):
                new_arr[i] = self.arr[current]
                current = (current + 1) % self.size

            self.arr = new_arr
            self.front = 0
            self.rear = self.size

# Example usage
queue = Queue()
queue.add(1)
queue.add(2)
queue.add(3)
print(queue.remove())  # Output: 1
queue.add(4)
print(queue)  # Output: 2, 3, 4
