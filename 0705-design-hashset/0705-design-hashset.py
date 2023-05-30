class MyHashSet:

    def __init__(self):
        self.hashTable=[None]*10000

    def add(self, key: int) -> None:
        hashval=key%10000
        if self.hashTable[hashval]==None:
            self.hashTable[hashval]=[key]
        else:
            self.hashTable[hashval].append(key) 
        # print(self.hashTable)
            
    def remove(self, key: int) -> None:
        hashval=key%10000
        if self.hashTable[hashval]!=None:
            while key in self.hashTable[hashval]: 
                self.hashTable[hashval].remove(key)
        

    def contains(self, key: int) -> bool:
        hashval=key%10000
        if self.hashTable[hashval]!=None and key in self.hashTable[hashval]:
            return True
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)