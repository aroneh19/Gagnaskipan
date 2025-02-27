class SLL_Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def print_list(head):
    if head is None:
        print()
        return
    print(head.data, end=" ")
    print_list(head.next)

def add_zero_between_each_node(head):
    if head.next is None:
        return head
    else:
        temp_node = head.next
        head.next = SLL_Node(0)
        head.next.next = temp_node
        add_zero_between_each_node(temp_node)
    return head

def to_arraylist_reverse(head):
    ret_list = ArrayList()
    to_arraylist_reverse_recur(head, ret_list)
    return ret_list

def to_arraylist_reverse_recur(head, ret_list):
    if head is None:
        return
    to_arraylist_reverse_recur(head.next, ret_list)
    ret_list.append(head.data)

class ArrayList:
    def __init__(self):
        self.capacity = 4
        self.arr = [None] * self.capacity
        self.size = 0

    def append(self, value):
        self.resize()
        self.arr[self.size] = value
        self.size += 1

    def resize(self):
        if self.size == self.capacity:
            self.capacity *= 2
            temp_arr = [None] * self.capacity
            for i in range(self.size):
                temp_arr[i] = self.arr[i]
            self.arr = temp_arr

    def print_list(self):
        for i in range(self.size):
            print(self.arr[i], end=" ")
        print()


if __name__ == "__main__":
    head = SLL_Node(5, SLL_Node(7, SLL_Node(1, SLL_Node(9, SLL_Node(2, SLL_Node(4))))))
    print_list(head)
    print(type(head).__name__)
    print("")
    arr_list = to_arraylist_reverse(head)
    arr_list.print_list()
    print(type(arr_list).__name__)
    print("")
    add_zero_between_each_node(head)
    print_list(head)
    print(type(head).__name__)
    print("")
    arr_list = to_arraylist_reverse(head)
    arr_list.print_list()
    print(type(arr_list).__name__)
    print("")