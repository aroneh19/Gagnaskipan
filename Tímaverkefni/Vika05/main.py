from node import Node
from node_list import NodeList


if __name__ == '__main__':
    my_list = NodeList()
    for i in range(10):
        my_list.push_front(i)
    
    print(my_list)
    my_list.pop_back()
    print(my_list)
    
    my_list.pop_front()
    print(my_list)

    my_list.push_back(10)
    print(my_list)