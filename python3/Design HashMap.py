class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.hash_map = [None] * self.size

    def _hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        if not self.hash_map[index]:
            self.hash_map[index] = ListNode(key, value)
        else:
            current = self.hash_map[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                if not current.next:
                    break
                current = current.next
            current.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = self._hash(key)
        current = self.hash_map[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return -1

    def remove(self, key: int) -> None:
        index = self._hash(key)
        current = self.hash_map[index]
        dummy = ListNode(-1, -1)
        dummy.next = current
        prev = dummy
        while current:
            if current.key == key:
                prev.next = current.next
                break
            prev = current
            current = current.next
        self.hash_map[index] = dummy.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)