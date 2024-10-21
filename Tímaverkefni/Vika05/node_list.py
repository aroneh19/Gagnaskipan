from node import Node

class NodeList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        ret_str = ""
        index_node = self.head
        while index_node != None:
            ret_str += f"{index_node.data}, "
            index_node = index_node.next
        ret_str = ret_str.rstrip(", ")
        return ret_str
    
    def pop_front(self):
        if self.head == None:
            return None
        ret_data = self.head.data
        self.head = self.head.next
        return ret_data
    
    def pop_back(self):
        if self.head == None:
            return None
        index_node = self.head
        while index_node.next.next != None:
            index_node = index_node.next
        ret_data = index_node.next.data
        index_node.next = None
        self.tail = index_node
        return ret_data

    def push_front(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
          new_node.next = self.head
          self.head = new_node
    
    def push_back(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node