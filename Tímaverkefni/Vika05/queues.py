from node import Node
from node_list import NodeList

class Queue(NodeList):
    def add(self, data):
        self.push_front(data)
    
    def pop(self):
        self.pop_front()

my_queue = Queue()
for i in range(10):
    my_queue.add(i)
print(my_queue)

my_queue.pop()
print(my_queue)