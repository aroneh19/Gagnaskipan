class GeneralTreeNode:
    def __init__(self, data=None):
        self.data = data
        self.children = []

class GeneralTree:
    def __init__(self):
        #this tree will be used in tests but your code must work for other tree setups as well
        self.root = GeneralTreeNode(7)
        root_child_1 = GeneralTreeNode(2)
        root_child_2 = GeneralTreeNode(1)
        root_child_3 = GeneralTreeNode(9)
        self.root.children = [root_child_1,root_child_2,root_child_3]
        root_grandchild_1 = GeneralTreeNode(13)
        root_grandchild_2 = GeneralTreeNode(4)
        root_grandchild_3 = GeneralTreeNode(2)
        root_grandchild_4 = GeneralTreeNode(6)
        root_grandchild_5 = GeneralTreeNode(1)
        root_grandchild_6 = GeneralTreeNode(8)
        root_grandchild_7 = GeneralTreeNode(15)
        root_grandchild_8 = GeneralTreeNode(5)
        self.root.children[0].children = [root_grandchild_1]
        self.root.children[1].children = [root_grandchild_2,root_grandchild_3,root_grandchild_4,root_grandchild_5]
        self.root.children[2].children = [root_grandchild_6,root_grandchild_7,root_grandchild_8]

    def find_smallest(self):
        return self.find_smallest_recur(self.root)

    def find_smallest_recur(self, node):
        if not node:
            return    
        smallest = node.data
        for child in node.children:
            small = self.find_smallest_recur(child)
            if smallest > small:
                smallest = small
        return smallest

    def sum_tree(self):
        return self.sum_tree_recur(self.root)

    def sum_tree_recur(self, node):
        if not node:
            return 0        
        sum = node.data
        for child in node.children:
            sum += self.sum_tree_recur(child)
        return sum

    def odd_numbers(self):
        return self.odd_numbers_recur(self.root)
    
    def odd_numbers_recur(self, node):
        odds = []
        if node.data % 2 != 0:
            odds.append(node.data)
        for child in node.children:
            odds += self.odd_numbers_recur(child)
        return odds

if __name__ == "__main__":
    print("Testing find_smallest")
    tree = GeneralTree()
    print(tree.find_smallest())
    print("Testing sum_tree")
    tree = GeneralTree()
    print(tree.sum_tree())
    print("Testing odd_numbers")
    tree = GeneralTree()
    print(sorted(tree.odd_numbers()))
    