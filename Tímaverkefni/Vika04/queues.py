
class Queue:
    def __init__(self) -> None:
        self.capacity = 8
        self.size = 0
        self.arr = [None] * self.capacity
    
    def __str__(self):
        return_string = ""
        for i in range(self.size):
            return_string += f"{self.arr[i]}, "
        return return_string.rstrip(", ")
    
    def add(self, value):
        self.resize()
        self.arr[self.size] = value
        self.size += 1

    def remove(self):
        if self.size == 0:
            raise ValueError("Array is empty")
        removed_value = self.arr[0]
        for i in range(self.size):
            self.arr[i] = self.arr[i + 1]
        self.size -= 1
        return removed_value
    
    def resize(self):
        """Resize the ArrayList if the size exceeds the capacity.

        Time complexity: O(n) - linear time in size of list
        """
        if self.size + 1 > self.capacity:
            self.capacity *= 2
            tmp_arr = [0] * self.capacity

            for i in range(self.size):
                tmp_arr[i] = self.arr[i]

            self.arr = tmp_arr

queue_lis = Queue()
queue_lis.add(1)
queue_lis.add(2)
queue_lis.add(3)
queue_lis.remove()
print(queue_lis)