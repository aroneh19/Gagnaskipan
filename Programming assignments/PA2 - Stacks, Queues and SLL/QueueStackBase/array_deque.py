#this class should not be changed
#either stack or queue should forward calls to this class for their implementation
class ArrayDeque():
    def __init__(self):
        self.capacity = 4
        self.arr = [None] * self.capacity
        self.size = 0

    def resize(self):
        tmp_arr = [0] * self.capacity * 2
        for i in range(self.size):
            tmp_arr[i] = self.arr[i]
        self.arr = tmp_arr
        self.capacity *= 2

    #O(1)
    def push_back(self, value):
        if self.size >= self.capacity:
            self.resize()
        self.arr[self.size] = value
        self.size += 1

    #O(n)
    def push_front(self, value):
        if self.size >= self.capacity:
            self.resize()
        i = self.size
        while(i > 0):
            self.arr[i] = self.arr[i - 1]
            i -= 1
        self.arr[0] = value
        self.size += 1

    #O(1)
    def pop_back(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.arr[self.size]

    #O(n)
    def pop_front(self):
        if self.size == 0:
            return None
        ret_val = self.arr[0]
        for i in range(1, self.size):
            self.arr[i - 1] = self.arr[i]
        self.size -= 1
        return ret_val

    #O(1)
    def get_size(self):
        return self.size

    #O(n)
    def __str__(self):
        str_val = ""
        for i in range(self.size - 1):
            str_val += str(self.arr[i]) + " "
        if self.size > 0:
            str_val += str(self.arr[self.size - 1])
        return str_val


if __name__ == "__main__":
    
    deque = ArrayDeque()
    deque.push_front(11)
    deque.push_front(10)
    deque.push_back(3)
    deque.push_back(1)
    deque.push_back(6)
    deque.push_back(9)
    print("size: " + str(deque.get_size()))
    print(deque)
    print(deque.pop_back())
    print(deque.pop_back())
    print(deque.pop_back())
    print("size: " + str(deque.get_size()))
    print(deque)
    deque.push_front(12)
    deque.push_front(16)
    deque.push_front(13)
    print("size: " + str(deque.get_size()))
    print(deque)
    print(deque.pop_back())
    print(deque.pop_back())
    print(deque.pop_back())
    print(deque.pop_back())
    print(deque.pop_back())
    print(deque.pop_back())
    print(deque.pop_back())
    print(deque.pop_back())
    print(deque.pop_back())
    print("size: " + str(deque.get_size()))
    print(deque)
    deque.push_front(12)
    deque.push_front(16)
    deque.push_front(13)
    print("size: " + str(deque.get_size()))
    print(deque)
    print(deque.pop_front())
    print(deque.pop_front())
    print("size: " + str(deque.get_size()))
    print(deque)
    deque.push_front(10)
    deque.push_back(3)
    deque.push_back(1)
    print("size: " + str(deque.get_size()))
    print(deque)
    print(deque.pop_front())
    print(deque)
    print(deque.pop_back())
    print(deque.pop_front())
    print(deque.pop_back())
    print(deque.pop_front())
    print(deque.pop_back())
