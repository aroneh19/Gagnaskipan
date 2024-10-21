class GTNode:
    def __init__(self, data=None) -> None:
        self.data = data
        self.children = []

class GeneralTree:
    def __init__(self):
        self.root = None

    def populate_tree(self):
        self.root = self.populate_tree_recur()

    def populate_tree_recur(self):
        value = input("Enter node value: ")
        if value == "":
            return None
        
        new_node = GTNode(value)

        while True:
            child = self.populate_tree_recur()
            if child is None:
                break
            new_node.children.append(child)

        return new_node
    
# print preorder
    def print_preorder(self):
        self.print_preorder_recur(self.root)
        print()

    def print_preorder_recur(self, node):
        if node == None:
            return
        
        print(node.data, end=" ")

        for child in node.children:
            self.print_preorder_recur(child)

# print postorder    
    def print_postorder(self):
        self.print_postorder_recur(self.root)
        print()

    def print_postorder_recur(self, node):
        if node == None:
            return
        
        for child in node.children:
            self.print_postorder_recur(child)

        print(node.data, end=" ")

if __name__ == "__main__":
    gt = GeneralTree()
    gt.populate_tree()
    gt.print_preorder()
    gt.print_postorder()