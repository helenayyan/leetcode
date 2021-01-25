class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        self.freq = 0


class LinkedList:
    def __init__(self):
        self.head = Node(0, 0)  # least recent
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head  # most recent
        self.length = 0

    def add_tail(self, node):
        node.prev = self.tail.prev
        node.prev.next = node
        self.tail.prev = node
        node.next = self.tail
        self.length += 1

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.length -= 1

    def remove_head(self):
        node = self.head.next
        self.remove_node(node)
        return node.key

    def get_length(self):
        return self.length


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.minfreq = 0
        self.keys_dict = dict()  # key: key.val, value: Node type key
        self.freq_dict = dict()
        self.freq_dict[0] = LinkedList()  # key:freq, value: linked list of nodes with freq

    def get(self, key: int) -> int:
        if key in self.keys_dict:
            node_key = self.keys_dict[key]

            self.freq_dict[node_key.freq].remove_node(node_key)

            if self.freq_dict[self.minfreq].get_length() == 0:
                self.minfreq += 1

            node_key.freq += 1

            if node_key.freq in self.freq_dict:
                self.freq_dict[node_key.freq].add_tail(node_key)
            else:
                self.freq_dict[node_key.freq] = LinkedList()
                self.freq_dict[node_key.freq].add_tail(node_key)
            print(self.freq_dict[self.minfreq].get_length())
            return node_key.val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.keys_dict:
            self.keys_dict[key].val = value
            node_key = self.keys_dict[key]
            node_key.val = value
            self.freq_dict[node_key.freq].remove_node(node_key)
            if self.freq_dict[self.minfreq].get_length() == 0:
                self.minfreq += 1

            node_key.freq += 1

            if node_key.freq in self.freq_dict:
                self.freq_dict[node_key.freq].add_tail(node_key)
            else:
                self.freq_dict[node_key.freq] = LinkedList()
                self.freq_dict[node_key.freq].add_tail(node_key)

        else:
            self.capacity -= 1
            if self.capacity < 0:
                if self.freq_dict[self.minfreq].get_length() > 0:
                    removed = self.freq_dict[self.minfreq].remove_head()
                    self.keys_dict.pop(removed)
                else:
                    return

            node = Node(key, value)
            self.keys_dict[key] = node
            self.freq_dict[node.freq].add_tail(node)

            self.minfreq = 0

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)