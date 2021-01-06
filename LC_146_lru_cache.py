"""
after python 3.7, dict is by default ordered
tricly part is how to get the first key in the map

you can covert map into iter and then call next to get the first key
"""
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        
        val = self.map.pop(key)
        self.map[key] = val
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map.pop(key)
        if len(self.map) == self.capacity:
            self.map.pop(next(iter(self.map)))
        self.map[key] = value
