
class HashMap: 

    def __init__(self, capacity): 
        self.capacity = capacity 
        self.size = 0 
        self.buckets = [[] for _ in range(capacity)]

    def __len__(self): 
        return self.size

    def __contains__(self, key):

        index = self._hash_function(key)
        bucket = self.buckets[index]

        for k, _ in bucket:
            if k == key: 
                return True 
 
        return False 

    def put(self, key, value):

        index = self._hash_function(key)
        bucket = self.buckets[index]

        for i, (k,v) in enumerate(bucket):
            if k == key: 
                bucket[i] = (key, value)
                return
            
        bucket.append((key, value)) 
        self.size += 1       

    def get(self, key): 

        index = self._hash_function(key)
        bucket = self.buckets[index]

        for k, v in bucket: 
            if key == k: 
                return v 

        raise IndexError("key not found")

    def remove(self, key):

        index = self._hash_function(key)
        bucket = self.buckets[index]

        for i, (k, _) in enumerate(bucket): 
            if k == key: 
                del self.buckets[index][i]
                self.size -= 1 
                break
        else: 
            raise KeyError("Key Not Found") 
         

    def keys(self):
        return [k for bucket in self.buckets for k, _ in bucket]

    def values(self): 
        return [v for bucket in self.buckets for _, v in bucket] 

    def items(self): 
        return [(k, v) for bucket in self.buckets for k, v in bucket]

    def _hash_function(self, key):
        key_string = str(key)
        hash = 0 
        for c in key_string: 
            hash = (hash * 31 + ord(c)) % self.capacity 

        return hash 

        

if __name__ == "__main__": 
    hash_map = HashMap(3)

    hash_map.put("name", "kaka")
    hash_map.put("name", "gomaa")
    hash_map.put("age", 24)


    if "name" in hash_map: 
        print("yes")

    print(f"Keys: {hash_map.keys()}")
    print({f"Values: {hash_map.values()}"})
    print(hash_map.get("name"))
    print(hash_map.remove("name"))

    print(hash_map.items())


