import sys
from dll import DLL

from random import Random

def test_print(dll):
    print(str(dll).strip() + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))

def test_insert(dll, num):
    print("insert " + str(num))
    dll.insert(num)
    test_print(dll)

def test_remove(dll):
    print("remove")
    dll.remove()
    test_print(dll)

def test_move_to_next(dll):
    print("move_to_next")
    dll.move_to_next()
    test_print(dll)

def test_move_to_prev(dll):
    print("move_to_prev")
    dll.move_to_prev()
    test_print(dll)

def test_move_to_pos(dll, pos):
    print("move_to_pos " + str(pos))
    dll.move_to_pos(pos)
    test_print(dll)

def test_clear(dll):
    print("clear")
    dll.clear()
    test_print(dll)

def test_sort(dll):
    print("sort")
    dll.sort()
    test_print(dll)

def test_partition(dll):
    print("partition")
    if len(dll) != 0:
        dll.partition(dll.get_first_node(), dll.get_last_node())
    else:
        print("empty list")    
    test_print(dll)

def test_get_first_node(dll):
    print("get_first_node")
    result = dll.get_first_node()
    if result != None:
        result = result.data
    print("first node: ", str(result))
    test_print(dll)

def test_get_last_node(dll):
    print("get_last_node")
    result = dll.get_last_node()
    if result != None:
        result = result.data
    print("last node: ", str(result))
    test_print(dll)

def test_dll(fin):
    for cmd in fin:
        cmd = cmd.strip().split()
        if cmd[0] == "new":
            dll = DLL()
            test_print(dll)
        elif cmd[0] == "insert":
            test_insert(dll, int(cmd[1]))
        elif cmd[0] == "remove":
            test_remove(dll)
        elif cmd[0] == "move_to_next":
            test_move_to_next(dll)
        elif cmd[0] == "move_to_prev":
            test_move_to_prev(dll)
        elif cmd[0] == "move_to_pos":
            test_move_to_pos(dll, int(cmd[1]))
        elif cmd[0] == "get_first_node":
            test_get_first_node(dll)
        elif cmd[0] == "get_last_node":
            test_get_last_node(dll)
        elif cmd[0] == "clear":
            test_clear(dll)
        elif cmd[0] == "sort":
            test_sort(dll)
        elif cmd[0] == "partition":
            test_partition(dll)

def main():

    orig_stdout = sys.stdout
    fout = open('out.txt', 'w+')
    sys.stdout = fout

    fin = open("tests.txt")

    test_dll(fin)

    sys.stdout = orig_stdout
    fout.close()


if __name__ == "__main__":
    main()


