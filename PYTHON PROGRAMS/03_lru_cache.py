from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity):
        if capacity < 1:
            raise ValueError("capacity must be positive")
        self.capacity = capacity
        self.data = OrderedDict()

    def get(self, key, default=None):
        if key not in self.data:
            return default
        self.data.move_to_end(key)
        return self.data[key]

    def put(self, key, value):
        if key in self.data:
            self.data.move_to_end(key)
        self.data[key] = value
        if len(self.data) > self.capacity:
            self.data.popitem(last=False)

    def __len__(self):
        return len(self.data)


if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put("user:1", {"name": "Asha"})
    cache.put("user:2", {"name": "Ravi"})
    cache.get("user:1")
    cache.put("user:3", {"name": "Maya"})
    print(cache.get("user:2"))
    print(cache.get("user:1"))
