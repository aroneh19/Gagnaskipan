class Node:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class ADT:
    def __init__(self) -> None:
        self.root = None
        self.size = 0
    
    def insert(self, key, value):
        self.root = self._insert_recur(key, value, self.root)
        self.size += 1

    def _insert_recur(self, key, value, root):
        if root is None:
            return Node(key, value)
        
        if key < root.key:
            root.left = self._insert_recur(key, value, root.left)
        elif key > root.key:
            root.right = self._insert_recur(key, value, root.right)
        else:
            return "Error"
        return root

    def find(self, key):
        result = self._find_recur(key, self.root)
        if result is None:
            return "Error"
        return result.value

    def _find_recur(self, key, root):
        if root is None or root.key == key:
            return root

        if key < root.key:
            return self._find_recur(key, root.left)
        return self._find_recur(key, root.right)

    def update(self, key, value):
        self.root = self._update_recur(key, value, self.root)
    
    def _update_recur(self, key, value, root):
        if root is None:
            return "Error"

        if key < root.key:
            root.left = self._update_recur(key, value, root.left)
        elif key > root.key:
            root.right = self._update_recur(key, value, root.right)
        else:
            root.value = value
        return root

    def remove(self, key):
        if self.root is not None:
            self.root = self._remove_recur(key, self.root)
            self.size -= 1

    def _remove_recur(self, key, root):
        if root is None:
            return "Error"

        if key < root.key:
            root.left = self._remove_recur(key, root.left)
        elif key > root.key:
            root.right = self._remove_recur(key, root.right)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            successor = self._find_min(root.right)
            root.key, root.value = successor.key, successor.value
            root.right = self._remove_recur(successor.key, root.right)

        return root

    def _find_min(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current
    
    def __len__(self):
        return self.size

    def __hash__(self):
        return hash((self.key, self.value))
    
    def __eq__(self, other) -> bool:
        return self.size == other.size
    
    def __str__(self):
        result = []
        self._print_inorder_recur(self.root, result)
        return ' '.join(result)

    def _print_inorder_recur(self, root, result):
        if root is not None:
            self._print_inorder_recur(root.left, result)
            result.append(f'{{{root.key}:{root.value}}}')
            self._print_inorder_recur(root.right, result)

if __name__ == '__main__':
    m = ADT()
    
    