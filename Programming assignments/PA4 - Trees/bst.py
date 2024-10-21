class ItemExistsException(Exception):
    pass

class NotFoundException(Exception):
    pass

class BSTNode:
    def __init__(self, key, value) -> None:
        """Node class for Binary Search Tree (BST).

        Attributes:
        - key: The key of the node.
        - value: The value associated with the key.
        - left: Reference to the left child node.
        - right: Reference to the right child node.
        """
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BSTMap:
    def __init__(self) -> None:
        """Binary Search Tree (BST) implementation for mapping keys to values.

        Attributes:
        - root: The root node of the BST.
        - size: The number of elements in the BST.
        """
        self.root = None
        self.size = 0
    
    def insert(self, key, value):
        """Inserts a new key-value pair into the BST.

        Args:
        - key: The key to be inserted.
        - value: The value associated with the key.
        """
        self.root = self._insert_recur(key, value, self.root)
        self.size += 1

    def _insert_recur(self, key, value, root):
        """Recursively inserts a new key-value pair into the BST.

        Args:
        - key: The key to be inserted.
        - value: The value associated with the key.
        - root: The root node of the subtree to insert into.

        Returns:
        - BSTNode: The root node of the subtree after insertion.
        """
        if root is None:
            return BSTNode(key, value)
        
        if key < root.key:
            root.left = self._insert_recur(key, value, root.left)
        elif key > root.key:
            root.right = self._insert_recur(key, value, root.right)
        else:
            raise ItemExistsException()
        return root

    def update(self, key, value):
        """Updates the value associated with a key in the BST.

        Args:
        - key: The key whose value is to be updated.
        - value: The new value to be associated with the key.
        """
        self.root = self._update_recur(key, value, self.root)
    
    def _update_recur(self, key, value, root):
        """Recursively updates the value associated with a key in the BST.

        Args:
        - key: The key whose value is to be updated.
        - value: The new value to be associated with the key.
        - root: The root node of the subtree to search for the key.

        Returns:
        - BSTNode: The root node of the subtree after update.
        """
        if root is None:
            raise NotFoundException()

        if key < root.key:
            root.left = self._update_recur(key, value, root.left)
        elif key > root.key:
            root.right = self._update_recur(key, value, root.right)
        else:
            root.value = value
        return root

    def find(self, key):
        """Finds the value associated with a given key in the BST.

        Args:
        - key: The key to search for.

        Returns:
        - The value associated with the given key.
        """
        result = self._find_recur(key, self.root)
        if result is None:
            raise NotFoundException()
        return result.value

    def _find_recur(self, key, root):
        """Recursively searches for a key in the BST.

        Args:
        - key: The key to search for.
        - root: The root node of the subtree to search in.

        Returns:
        - BSTNode: The node containing the key-value pair, or None if not found.
        """
        if root is None or root.key == key:
            return root

        if key < root.key:
            return self._find_recur(key, root.left)
        return self._find_recur(key, root.right)

    def contains(self, key):
        """Checks if a key exists in the BST.

        Args:
        - key: The key to check for.

        Returns:
        - bool: True if the key exists, False otherwise.
        """
        return self._contain_recur(key, self.root)
    
    def _contain_recur(self, key, root):
        """Recursively checks if a key exists in the BST.

        Args:
        - key: The key to check for.
        - root: The root node of the subtree to search in.

        Returns:
        - bool: True if the key exists, False otherwise.
        """
        if root is None:
            return False
        if root.key == key:
            return True
        elif key < root.key:
            return self._contain_recur(key, root.left)
        elif key >= root.key:
            return self._contain_recur(key, root.right)

    def remove(self, key):
        """Removes a key-value pair from the BST.

        Args:
        - key: The key to be removed.
        """
        if self.root is not None:
            self.root = self._remove_recur(key, self.root)
            self.size -= 1

    def _remove_recur(self, key, root):
        """Recursively removes a key-value pair from the BST.

        Args:
        - key: The key to be removed.
        - root: The root node of the subtree to remove from.

        Returns:
        - BSTNode: The root node of the subtree after removal.
        """
        if root is None:
            raise NotFoundException()

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
        """Finds the node with the minimum key in a subtree.

        Args:
        - root: The root node of the subtree.

        Returns:
        - BSTNode: The node with the minimum key.
        """
        current = root
        while current.left is not None:
            current = current.left
        return current

    def __setitem__(self, key, value):
        """Allows setting key-value pairs using the indexing syntax.

        Args:
        - key: The key to be inserted or updated.
        - value: The value associated with the key.
        """
        try:
            self.update(key, value)
        except NotFoundException:
            self.insert(key, value)

    def __getitem__(self, key):
        """Allows retrieving values using the indexing syntax.

        Args:
        - key: The key whose value is to be retrieved.

        Returns:
        - The value associated with the given key.
        """
        return self.find(key)

    def __len__(self):
        """Returns the number of elements in the BST."""
        return self.size

    def __str__(self):
        """Returns a string representation of the BST."""
        result = []
        self._print_inorder_recur(self.root, result)
        return ' '.join(result)

    def _print_inorder_recur(self, root, result):
        """Recursively performs an inorder traversal of the BST.

        Args:
        - root: The root node of the subtree.
        - result: A list to store the string representation of nodes.
        """

        if root is not None:
            self._print_inorder_recur(root.left, result)
            result.append(f'{{{root.key}:{root.value}}}')
            self._print_inorder_recur(root.right, result)

class MyComparableKey:
    """A custom class for creating keys that can be compared.

    Attributes:
    - int_value: An integer value associated with the key.
    - string_value: A string value associated with the key.
    """
    def __init__(self, int_value, string_value):
        self.int_value = int_value
        self.string_value = string_value

    def __lt__(self, other):
        """Defines the less-than comparison for instances of this class.

        Args:
        - other: Another instance of MyComparableKey.

        Returns:
        - bool: True if this instance is less than the other, False otherwise.
        """
        return (self.int_value) < (other.int_value)