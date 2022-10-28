"""HW_5 """


class LRUCache:
    """class LRUCache """

    def __init__(self, limit=42):
        self.list = LinkedList()
        self.dict = {}
        self.capacity = limit

    def _insert(self, key, val):
        node = ListNode(key, val)
        self.list.insert(node)
        self.dict[key] = node

    def get(self, key):
        if key in self.dict:
            val = self.dict[key].val
            self.list.delete(self.dict[key])
            self._insert(key, val)
            return val
        return None

    def set(self, key, val):
        if key in self.dict:
            self.list.delete(self.dict[key])
        elif len(self.dict) == self.capacity:
            del self.dict[self.list.head.key]
            self.list.delete(self.list.head)
        self._insert(key, val)


class ListNode:
    """supportive class """

    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None


class LinkedList:
    """supportive class """

    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, node):
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node

    def delete(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev


if __name__ == '__main__':
    cache = LRUCache(2)

    cache.set("k1", "val1")
    cache.set("k2", "val2")

    print(cache.get("k3"))  # None
    print(cache.get("k2"))  # "val2"
    print(cache.get("k1"))  # "val1"

    cache.set("k3", "val3")

    print(cache.get("k3"))  # "val3"
    print(cache.get("k2"))  # None
    print(cache.get("k1"))  # "val1"
