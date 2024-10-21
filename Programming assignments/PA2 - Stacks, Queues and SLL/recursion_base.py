class Node:
    """Represents a node in a singly linked list.

    Attributes:
    - data: The data stored in the node.
    - next: Reference to the next node in the linked list.
    """
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

def print_to_screen(head):
    """Recursively prints the data of each node in the linked list, starting from the given head.

    Parameters:
    - head: The head node of the linked list.
    """
    if head != None:
        print(head.data, end=" ")
        print_to_screen(head.next)
    else:
        print("")

def get_size(head):
    """Recursively calculates the size of the linked list starting from the given head.

    Parameters:
    - head: The head node of the linked list.

    Returns:
    - int: The size of the linked list.
    """
    if head is None:
        return 0
    return 1 + get_size(head.next)

def reverse_list(head):
    """Reverses the linked list starting from the given head.

    Parameters:
    - head: The head node of the linked list.

    Returns:
    - Node: The new head node of the reversed linked list.
    """
    if head == None:
        return head
    elif head.next == None:
        return head
    back_head = reverse_list(head.next)
    head.next.next = head
    head.next = None
    return back_head

def palindrome(head):
    """Determines if the linked list is a palindrome.

    Parameters:
    - head: The head node of the linked list.

    Returns:
    - bool: True if the linked list is a palindrome, False otherwise.
    """
    length = get_size(head)
    return palindrome_recursive(head, length)[0]

def palindrome_recursive(node, length):
    """Helper function for palindrome. Recursively checks if the linked list is a palindrome.

    Parameters:
    - node: The current node being compared.
    - length: The remaining length of the linked list to be checked.

    Returns:
    - tuple: (bool, Node) True if the linked list is a palindrome, and the next node to be compared.
    """
    if length == 0:
        return True, node
    if length == 1:
        return True, node.next
    result, tail = palindrome_recursive(node.next, length - 2)
    if not result or tail is None:
        return False, None
    return node.data == tail.data, tail.next
        
if __name__ == "__main__":
    ##
    print("GET_SIZE TESTS")
    print("\n")
    head = Node("A", Node("E", Node("L", Node("E", Node("A", None)))))
    print_to_screen(head)
    print("size: " + str(get_size(head)))
    print_to_screen(head)

    print("\n")
    head = None
    print_to_screen(head)
    print("size: " + str(get_size(head)))
    print_to_screen(head)

    print("\n")
    head = Node("A", None)
    print_to_screen(head)
    print("size: " + str(get_size(head)))
    print_to_screen(head)

    print("\n")
    head = Node("A", Node("C", None))
    print_to_screen(head)
    print("size: " + str(get_size(head)))
    print_to_screen(head)


    ##
    print("REVERSE TESTS")
    print("\n")
    head = Node("A", Node("B", Node("C", Node("D", Node("E", None)))))
    print_to_screen(head)
    rev_head = reverse_list(head)
    print_to_screen(rev_head)

    print("\n")
    head = Node("A", Node("A", Node("A", Node("B", Node("A", None)))))
    print_to_screen(head)
    rev_head = reverse_list(head)
    print_to_screen(rev_head)

    print("\n")
    head = Node("C", Node("B", Node("A", Node("B", Node("A", None)))))
    print_to_screen(head)
    rev_head = reverse_list(head)
    print_to_screen(rev_head)

    print("\n")
    head = Node("C", None)
    print_to_screen(head)
    rev_head = reverse_list(head)
    print_to_screen(rev_head)

    print("\n")
    head = None
    print_to_screen(head)
    rev_head = reverse_list(head)
    print_to_screen(rev_head)

    print("\n")
    head = Node("C", Node("B", None))
    print_to_screen(head)
    rev_head = reverse_list(head)
    print_to_screen(rev_head)


    ##
    print("PALINDROME TESTS")
    print("\n")
    head = Node("A", Node("E", Node("L", Node("E", Node("A", None)))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("A", Node("E", Node("L", Node("B", Node("A", None)))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("C", Node("A", Node("L", Node("L", Node("A", Node("C", None))))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("C", Node("A", Node("L", Node("T", Node("E", Node("C", None))))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")
