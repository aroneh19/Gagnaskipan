class BTNode:
    def __init__(self, data=None, left= None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

    def populate_tree(self):
        self.root = self.populate_tree_recurr()

    def populate_tree_recurr(self):
        value = input("Enter node value: ")
        if value == "":
            return None
        
        new_node = BTNode(value)

        new_node.left = self.populate_tree_recurr()
        new_node.right = self.populate_tree_recurr()

        return new_node
    
# print preorder
    def print_preorder(self):
        self.print_preorder_recurr(self.root)
        print()

    def print_preorder_recurr(self, node):
        if node == None:
            return
        
        print(node.data, end=" ")

        self.print_preorder_recurr(node.left)
        self.print_preorder_recurr(node.right)

# print inorder    
    def print_inorder(self):
        self.print_inorder_recurr(self.root)
        print()

    def print_inorder_recurr(self, node):
        if node == None:
            return
        
        self.print_inorder_recurr(node.left)
        print(node.data, end=" ")
        self.print_inorder_recurr(node.right)

# print postorder
    def print_postorder(self):
        self.print_postorder_recurr(self.root)
        print()

    def print_postorder_recurr(self, node):
        if node == None:
            return
        
        self.print_postorder_recurr(node.left)
        self.print_postorder_recurr(node.right)
        print(node.data, end=" ")


if __name__ == "__main__":
    bt = BinaryTree()
    bt.populate_tree()
    bt.print_preorder()
    bt.print_inorder()
    bt.print_postorder()