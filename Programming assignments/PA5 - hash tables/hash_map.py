class ItemExistsException(BaseException):
    pass

class NotFoundException(BaseException):
    pass

class Node:
    """A node in a linked list, representing a key-value pair."""
    def __init__(self, key, val):
        """Initialize a Node with the provided key and value.

        Args:
            key: The key of the key-value pair.
            val: The value associated with the key.
        """
        self.key = key
        self.val = val
        self.next = None

class Bucket:
    """A bucket for storing key-value pairs using a linked list."""

    def __init__(self):
        """Initialize an empty Bucket."""
        self.head = None
        self.size = 0

    def insert(self, key, val):
        """Insert a key-value pair into the bucket.

        Args:
            key: The key of the key-value pair.
            val: The value associated with the key.

        Raises:
            ItemExistsException: If the key already exists in the bucket.
        """
        new_node = Node(key, val)
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            if current.key == key:
                raise ItemExistsException()
            current = current.next
        if current.key == key:
            raise ItemExistsException()
        current.next = new_node
        self.size += 1

    def update(self, key, val):
        """Update the value associated with the given key.

        Args:
            key: The key of the key-value pair to be updated.
            val: The new value to be associated with the key.

        Raises:
            NotFoundException: If the key doesn't exist in the bucket.
        """
        current = self.head
        while current:
            if current.key == key:
                current.val = val
                return
            current = current.next
        raise NotFoundException()

    def find(self, key):
        """Find the value associated with the given key.

        Args:
            key: The key of the key-value pair to be found.

        Returns:
            The value associated with the key.

        Raises:
            NotFoundException: If the key doesn't exist in the bucket.
        """
        current = self.head
        while current:
            if current.key == key:
                return current.val
            current = current.next
        raise NotFoundException()
            

    def contains(self, key):
        """
        Check if the bucket contains the given key.

        Args:
            key: The key to be checked.

        Returns:
            True if the key exists in the bucket, False otherwise.
        """
        current = self.head
        while current:
            if current.key == key:
                return True
            current = current.next
        return False

    def remove(self, key):
        """
        Remove the key-value pair with the given key from the bucket.

        Args:
            key: The key of the key-value pair to be removed.
        """
        if self.head == None:
            return
 
        if self.head.key == key:
            self.head = self.head.next
            self.size -= 1
            return

        current_node = self.head
        prev_node = None

        while current_node is not None and current_node.key != key:
            prev_node = current_node
            current_node = current_node.next

        if current_node is None:
            return

        prev_node.next = current_node.next
        self.size -= 1

    def __setitem__(self, key, val):
        """Set the value associated with the given key.

        If the key already exists, update its value; otherwise, insert a new key-value pair.

        Args:
            key: The key of the key-value pair.
            val: The value associated with the key.
        """
        try:
            self.update(key, val)
        except NotFoundException:
            self.insert(key, val)

    def __getitem__(self, key):
        """Get the value associated with the given key.

        Args:
            key: The key of the key-value pair to retrieve.

        Returns:
            The value associated with the key.

        Raises:
            NotFoundException: If the key doesn't exist in the bucket.
        """
        return self.find(key)

    def __len__(self):
        """Get the number of key-value pairs in the bucket.

        Returns:
            The number of key-value pairs.
        """
        return self.size
    
    def __str__(self) -> str:
        """Get a string representation of the bucket.

        Returns:
            A string representation of the bucket, showing its key-value pairs.
        """
        current_node = self.head
        result = ""
        while current_node:
            result += f"{{{current_node.key}:{current_node.val}}}"
            current_node = current_node.next
            if current_node:
                result += " "
        return result

class HashMap():
    """A hash map implementation using buckets to handle collisions."""
    def __init__(self):
        """Initialize an empty hash map."""
        self.capacity = 8
        self.size = 0
        self.buckets = [Bucket() for _ in range(self.capacity)]

    def _index(self, key):
        """Get the index in the bucket list for the given key.

        Args:
            key: The key to be hashed.

        Returns:
            The index for the key in the bucket list.
        """
        return hash(key) % self.capacity

    def _rebuild(self):
        """Rebuild the hash map if its load factor exceeds a certain threshold."""
        if self.size > 1.2 * self.capacity:
            self.capacity *= 2
            new_buckets = [Bucket() for _ in range(self.capacity)]
            for bucket in self.buckets:
                current_node = bucket.head
                while current_node:
                    index = self._index(current_node.key)
                    new_buckets[index].insert(current_node.key, current_node.val)
                    current_node = current_node.next
            self.buckets = new_buckets

    def insert(self, key, val):
        """Insert a key-value pair into the hash map.

        Args:
            key: The key of the key-value pair.
            val: The value associated with the key.

        Raises:
            ItemExistsException: If the key already exists in the hash map.
        """
        index = self._index(key)
        if self.buckets[index].contains(key):
            raise ItemExistsException()
        self.buckets[index].insert(key, val)
        self.size += 1
        self._rebuild()

    def update(self, key, val):
        """Update the value associated with the given key.

        Args:
            key: The key of the key-value pair to be updated.
            val: The new value to be associated with the key.
        """
        index = self._index(key)
        self.buckets[index].update(key, val)

    def find(self, key):
        """Find the value associated with the given key.

        Args:
            key: The key of the key-value pair to be found.

        Returns:
            The value associated with the key.
        """
        index = self._index(key)
        return self.buckets[index].find(key)

    def contains(self, key):
        """Check if the hash map contains the given key.

        Args:
            key: The key to be checked.

        Returns:
            True if the key exists in the hash map, False otherwise.
        """
        index = self._index(key)
        return self.buckets[index].contains(key)

    def remove(self, key):
        """Remove the key-value pair with the given key from the hash map.

        Args:
            key: The key of the key-value pair to be removed.
        """
        index = self._index(key)
        self.buckets[index].remove(key)
        self.size -= 1

    def __setitem__(self, key, val):
        """Set the value associated with the given key.

        If the key already exists, update its value; otherwise, insert a new key-value pair.

        Args:
            key: The key of the key-value pair.
            val: The value associated with the key.
        """
        index = self._index(key)
        try:
            self.buckets[index].update(key, val)
        except NotFoundException:
            self.buckets[index].insert(key, val)
            self.size += 1
            self._rebuild()

    def __getitem__(self, key):
        """Get the value associated with the given key.

        Args:
            key: The key of the key-value pair to retrieve.

        Returns:
            The value associated with the key.

        Raises:
            NotFoundException: If the key doesn't exist in the hash map.
        """
        index = self._index(key)
        return self.buckets[index][key]

    def __len__(self):
        """Get the number of key-value pairs in the hash map.

        Returns:
            The number of key-value pairs.
        """
        return self.size
    
    def __str__(self):
        """Get a string representation of the hash map.

        Returns:
            A string representation of the hash map, showing its key-value pairs.
        """
        ret_str = ""
        for bucket in self.buckets:
            ret_str += f"{str(bucket)}\n"
        return ret_str

class MyHashableKey():
    """A custom hashable key class."""

    def __init__(self, int_value, string_value) -> None:
        """Initialize a MyHashableKey with an integer value and a string value.

        Args:
            int_value: An integer value.
            string_value: A string value.
        """
        self.int_value = int_value
        self.string_value = string_value
    
    def __eq__(self, other):
        """Check if this MyHashableKey is equal to another object.

        Args:
            other: The object to compare with.

        Returns:
            True if the objects are equal, False otherwise.
        """
        if self.int_value == other.int_value and self.string_value == other.string_value:
            return True
        return False

    def __hash__(self):
        """Calculate the hash value of this MyHashableKey.

        Returns:
            The hash value.
        """
        PRIME = 31
        result = PRIME + self.int_value
        
        for char in self.string_value:
            char_to_num = ord(char)
            result = result * 550 + char_to_num
    
        return result

if __name__ == '__main__':
    m = HashMap()
    for i in range(5000):
        s = str(i)
        m.insert(MyHashableKey(i, s), s)

    counts = [0] * 20
    for bucket in m.buckets:
        counts[len(bucket)] += 1

    ret = []
    for index, count in enumerate(counts):
        if count:
            ret.append((index, count))

    print(ret)