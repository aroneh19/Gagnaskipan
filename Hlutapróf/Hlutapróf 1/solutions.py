class ArrayList:
    def __init__(self):
        self.capacity = 4
        self.size = 0
        self.array = [None] * self.capacity

    def __str__(self):
        ret_str = ""
        for i in range(0, self.size):
            ret_str += str(self.array[i]) + " "
        return ret_str
    
    def resize(self):
        if self.capacity == self.size:
            self.capacity *= 2
            temparr = [None] * self.capacity
            for i in range(0, self.size):
                temparr[i] = self.array[i]
            self.array = temparr

    def append(self, value):
        self.resize()
        self.array[self.size] = value
        self.size += 1

    def remove_largest(self):
        if self.size > 0:
            largest = self.array[0]
            largest_index = 0
            for i in range(self.size):
                if self.array[i] > largest:
                    largest = self.array[i]
                    largest_index = i
            
            self.size -= 1
            for i in range(self.size):
                if i >= largest_index:
                    self.array[i] = self.array[i + 1]

def count_in_range(lis, range_from, range_to):
    if lis != []:
        head = lis[1:]
        if range_from <= lis[0] <= range_to:
            return 1 + count_in_range(head, range_from, range_to)
        return count_in_range(head, range_from, range_to)
    return 0
        
def remove_odd_indexes(lis, index=0):
    if index >= len(lis):
        return []
    return [lis[index]] + remove_odd_indexes(lis, index + 2)

if __name__ == "__main__":
    print("Arraylist tests:")
    arrlis = ArrayList()
    arrlis.append(8)
    arrlis.append(62)
    arrlis.append(15)
    arrlis.append(19)
    arrlis.append(24)
    arrlis.append(7)
    print(arrlis)
    arrlis.remove_largest()
    print(arrlis)
    arrlis.remove_largest()
    print(arrlis)
    arrlis.remove_largest()
    print(arrlis)
    arrlis.remove_largest()
    print(arrlis)
    arrlis.remove_largest()
    print(arrlis)
    arrlis.remove_largest()
    print(arrlis)
    print("Recursion tests:")
    print(count_in_range([5,1,22,7,19,8,31,4,6,10,17,13], 5, 20))
    print(count_in_range([5,1,22,7,19,8,31,4,6,10,17,13], 1, 5))
    print(count_in_range([5,1,22,7,19,8,31,4,6,10,17,13], 0, 25))
    print(count_in_range([5,1,22,7,19,8,31,4,6,10,17,13], 0, 100))
    print(remove_odd_indexes([5,1,22,7,19,8,31,4,6,10,17,13]))
    