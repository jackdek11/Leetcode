from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)  # Move the accessed key to the end to mark it as most recently used
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key]  # Remove the existing key to update its value
        elif len(self.cache) == self.capacity:
            self.cache.popitem(last=False)  # Remove the least recently used key (first item in the OrderedDict)
        self.cache[key] = value  # Add the new key-value pair

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)