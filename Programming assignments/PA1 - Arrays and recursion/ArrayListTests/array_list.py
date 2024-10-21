class IndexOutOfBounds(Exception):
    pass

class NotFound(Exception):
    pass

class Empty(Exception):
    pass

class NotOrdered(Exception):
    pass

class ArrayList:
    def __init__(self):
        """Initialize an empty ArrayList with default capacity."""
        self.size = 0
        self.capacity = 4
        self.arr = [0] * self.capacity

    def __str__(self):
        """Return a string representation of the ArrayList."""
        return_string = ""
        for i in range(self.size - 1):
            return_string += f"{self.arr[i]}, "
        if self.size > 0:
            return_string += f"{self.arr[self.size - 1]}"
        return return_string

    def prepend(self, value):
        """Insert a value at the beginning of the ArrayList.

        Time complexity: O(n) - linear time in size of list
        """
        self.resize()

        for i in range(self.size - 1, -1, -1):
            self.arr[i + 1] = self.arr[i]
        
        self.insert_to_array(0, value)

    def insert(self, value, index: int):
        """Insert a value at a specified index in the ArrayList.

        Time complexity: O(n) - linear time in size of list
        """
        self.check_index(index, 1)
        self.resize()

        for i in range(self.size - 1, index - 1, -1):
            self.arr[i + 1] = self.arr[i]

        self.insert_to_array(index, value)

    def append(self, value):
        """Append a value to the end of the ArrayList.

        Time complexity: O(1) - constant time
        """
        self.resize()
        self.insert_to_array(self.size, value)

    def set_at(self, value, index):
        """Set the value at a specified index in the ArrayList.

        Time complexity: O(1) - constant time
        """
        self.check_index(index)
        self.arr[index] = value

    def get_first(self):
        """Get the first element of the ArrayList.

        Time complexity: O(1) - constant time
        """    
        if self.size == 0:
            raise Empty()
        return self.arr[0]

    def get_at(self, index):
        """Get the value at a specified index in the ArrayList.

        Time complexity: O(1) - constant time
        """
        self.check_index(index)
        return self.arr[index]

    def get_last(self):
        """Get the last element of the ArrayList.

        Time complexity: O(1) - constant time
        """
        if self.size == 0:
            raise Empty()
        return self.arr[self.size - 1]

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

    def remove_at(self, index):
        """Remove the element at a specified index in the ArrayList.

        Time complexity: O(n) - linear time in size of list
        """
        self.check_index(index)

        for i in range(index, self.size -1):
            self.arr[i] = self.arr[i + 1]
        
        self.size -= 1

    def clear(self):
        """Clear the ArrayList, resetting its size and capacity.

        Time complexity: O(1) - constant time
        """
        self.size = 0
        self.capacity = 4
        self.arr = [0] * self.capacity

    def insert_ordered(self, value):
        """Insert a value in an ordered manner into the ArrayList.

        Time complexity: O(n) - linear time in size of list
        """
        if not self.order_check():
            raise NotOrdered("Array is not ordered")

        index = 0
        for i in range(self.size):
            if self.arr[i] >= value:
                break
            index += 1

        self.insert(value, index)

    def find(self, value):
        """Find the index of a specified value in the ArrayList.

        Time complexity:
        - O(n) - linear time in size of list (unordered list)
        - O(log n) - logarithmic time in size of list (ordered list)
        """
        if self.order_check():
            return self.binary_search(self.arr, 0, self.size - 1, value)
        return self.linear_search(self.arr, value, 0)

    def binary_search(self, arr, low, high, value):
        """Perform binary search on an ordered list.

        Time complexity: O(log n) - logarithmic time in size of list
        """
        if high >= low:
            mid = (high + low) // 2
            if arr[mid] == value:
                return mid
            elif arr[mid] > value:
                return self.binary_search(arr, low, mid - 1, value)
            return self.binary_search(arr, mid + 1, high, value)
        raise NotFound("Value not found in list")

    def linear_search(self, my_list, value, index):
        """Perform linear search on an unordered list.

        Time complexity: O(n) - linear time in size of list
        """
        if not my_list:
            raise NotFound("Value not found in list")
        
        head = my_list[0]
        tail = my_list[1:]

        if head == value:
            return index
        
        return self.linear_search(tail, value, index + 1)

    def remove_value(self, value):
        """Remove the first occurrence of a specified value from the ArrayList.

        Time complexity: O(n) - linear time in size of list
        """
        index = self.find(value)
        self.remove_at(index)

    def insert_to_array(self, index, value):
        """Helper function to insert a value at a specified index in the ArrayList."""
        self.arr[index] = value
        self.size += 1

    def check_index(self, index, insert=0):
        """Check if the index is within bounds of the ArrayList.

        Returns: True if the index is valid, raises IndexOutOfBounds otherwise.
        """
        if index < 0 or index >= (self.size + insert):
            raise IndexOutOfBounds("Index is out of bounds")
        
        return True

    def order_check(self):
        """Check if the ArrayList is ordered.

        Returns: True if the ArrayList is ordered, False otherwise.
        """
        for i in range(self.size - 1):
            if self.arr[i] > self.arr[i + 1]:
                return False
        return True

if __name__ == "__main__":
    arr_lis = ArrayList()
    print(str(arr_lis))
