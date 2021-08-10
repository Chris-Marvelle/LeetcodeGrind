class LRUCache:
    def __init__(self, capacity: int):
        self.len = capacity
        self.dict = {}
    
    def get(self, key: int) -> int:
        value = self.dict.get(key)
        if value is not None:
            del self.dict[key]
            self.dict[key] = value
            return value
        else:            
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            del self.dict[key]
        else:
            if len(self.dict) == self.len:
                del self.dict[next(iter(self.dict))]                
        self.dict[key] = value
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)