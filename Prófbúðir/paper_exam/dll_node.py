class DLL_Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.next = next
        self.prev = prev


class DLL_Deque:
    def __init__(self):
        self.header = DLL_Node("header")
        self.trailer = DLL_Node("trailer")
        self.header.next = self.trailer
        self.trailer.prev = self.header

    def push_back(self, value) -> None:
        # make new node
        new_node = DLL_Node(value)

        # Fetch the old last node
        old_last = self.trailer.prev

        # connect new node to trailer
        new_node.next = self.trailer
        self.trailer.prev = new_node

        # connect old last node to new node
        new_node.prev = old_last
        old_last.next = new_node

    def contains_value(self, value) -> bool:
        
        # start at the first data node
        curr = self.header.next

        # iterate through the list
        while curr is not self.trailer:

            # Check if the node contains the value
            if curr.data == value:
                return True

            curr = curr.next
        
        return False


def print_deque(deque):
    print("forward pass")

    forward_pass = []
    curr = deque.header.next
    while curr is not deque.trailer:
        forward_pass.append(str(curr.data))
        curr = curr.next

    print(*forward_pass, sep=', ')

    print("backward pass")
    curr = deque.trailer.prev

    backward_list = []
    while curr is not deque.header:
        backward_list.append(str(curr.data))
        curr = curr.prev 

    print(*backward_list[::-1], sep=', ')

       

if __name__ == "__main__":
    d = DLL_Deque()

    for i in range(10):
        d.push_back(i)

    print_deque(d)

    for val in range(5, 15):
        print(f"Contains {val}: {d.contains_value(val)}")
        