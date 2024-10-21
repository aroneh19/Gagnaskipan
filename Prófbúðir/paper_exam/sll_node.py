class SLL_Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def length(head):
    if head is None:
        return 0

    return 1 + length(head.next)

def length_iter(head):
    curr = head
    lngth = 0
    while curr is not None:
        lngth += 1
        curr = curr.next
    return lngth
        


# Helper
def make_sll(lis):
    if len(lis) == 0:
        return None

    head = SLL_Node(lis[0])
    cur = head
    for el in lis[1:]:
        next_node = SLL_Node(el)
        cur.next = next_node
        cur = cur.next

    return head
    
if __name__ == "__main__":
    l = [1, 5, 6, 7]
    lis = make_sll(l)

    print(f"Length of {l} is {length(lis)}")