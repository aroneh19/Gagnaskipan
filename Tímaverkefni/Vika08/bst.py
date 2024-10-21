class BSTNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self) -> None:
        self.root = None
    
    def _insert_recur(self, value, root):
        if root is None:
            return BSTNode(value)
        
        if value < root.value:
            root.left = self._insert_recur(value, root.left)
        elif value >= root.value:
            root.right = self._insert_recur(value, root.right)
        return root

    def insert(self, value):
        self.root = self._insert_recur(value, self.root)
    
    
# print preorder    
    def print_inorder(self):
        self.print_inorder_recurr(self.root)
        print()

    def print_inorder_recurr(self, root):
        if root == None:
            return
        
        self.print_inorder_recurr(root.left)
        print(root.value, end=", ")
        self.print_inorder_recurr(root.right)
    
    def contains(self, value):
        return self._contain_recur(value, self.root)
    
    def _contain_recur(self, value, root):
        if root is None:
            return False
        if root.value == value:
            return True
        elif value < root.value:
            return self._contain_recur(value, root.left)
        elif value >= root.value:
            return self._contain_recur(value, root.right)
    

if __name__ == "__main__":
    bst = BST()
    bst.insert(5)
    bst.insert(2)
    bst.insert(1)
    bst.insert(4)
    bst.insert(8)
    bst.insert(8)
    bst.insert(7)
    bst.insert(3)
    bst.print_inorder()
    print(bst.contains(10))