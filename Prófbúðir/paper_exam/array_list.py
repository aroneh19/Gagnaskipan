
class ArrayList:
    def __init__(self):
        self.capacity = 4
        self.size = 0
        self.arr = [None] * self.capacity

    def resize(self):
        # create new array double the size
        new_arr = [None] * (self.capacity * 2)

        # copy old array to new array
        for i in range(self.size):
            new_arr[i] = self.arr[i]

        # update instance variable
        self.arr = new_arr
        self.capacity = self.capacity * 2

    def append(self, val):
        if self.size == self.capacity:
            self.resize()

        self.arr[self.size] = val
        self.size += 1

    def prepend(self, val):
        if self.size == self.capacity:
            self.resize()

        # shift all elements to the right
        for i in range(self.size, 0, -1):
            self.arr[i] = self.arr[i - 1]

        self.arr[0] = val
        self.size += 1
      

    def __str__(self):
        if self.size == 0:
            return "<empty>"

        out = ""
        for i in range(self.size):
            out += str(self.arr[i])
            if i < self.size - 1:
                out += ","
            out += " "

        return out
        

if __name__ == "__main__":
    a = ArrayList()

    print(a)

    for i in range(10):
        a.append(i)

    for i in range(10, 20):
        print(a)
        a.prepend(i)

    print(a)
