class LinkedList:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.storage = dict()  # key=key, value = linkedlistnode
        self.capacity = capacity  # available space

        # Use a linked list to store the order of keys added; head -> least recent, tail -> most recent
        self.head = LinkedList(0, 0)
        self.tail = LinkedList(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.storage:
            return -1

        node = self.storage[key]
        self.move_to_tail(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.storage:
            new_key = LinkedList(key, value)
            self.storage[key] = new_key
            self.add_to_tail(new_key)

            if self.capacity == 0:
                remove = self.remove_head()
                self.storage.pop(remove.key)
            else:
                self.capacity -= 1
        else:
            node = self.storage[key]
            node.val = value
            self.move_to_tail(node)

    def add_to_tail(self, node):
        node.prev = self.tail.prev
        node.prev.next = node
        self.tail.prev = node
        node.next = self.tail

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def move_to_tail(self, node):
        self.remove_node(node)
        self.add_to_tail(node)

    def remove_head(self):
        node = self.head.next
        self.remove_node(node)
        return node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)