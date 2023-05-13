class node:
    def __init__(self,data=0, flag=0):
        self.data=data
        self.flag=0 
        self.children={} 
class Trie:
    def __init__(self):
        self.root=node()
        

    def insert(self, word: str) -> None: 
        temp=self.root
        n=len(word)
        for i in range(n):
            if i==n-1:
                if temp and word[i] in temp.children:
                    temp=temp.children[word[i]] 
                    temp.flag=1
                else:
                    newnode=node(word[i])
                    temp.children[word[i]]=newnode
                    newnode.flag=1
                    
            elif i==0:
                if temp and word[i] in temp.children:
                    temp=temp.children[word[i]] 
                else:
                    newnode=node(word[i])
                    temp.children[word[i]]=newnode  
                    temp=newnode
            
            else:
                if temp and word[i] in temp.children:
                    temp=temp.children[word[i]] 
                else:
                    newnode=node(word[i])
                    temp.children[word[i]]=newnode
                    temp=newnode 
        

    def search(self, word: str) -> bool:
        temp=self.root
        n=len(word) 
        for i in range(n):
            if temp  and word[i] not in temp.children:
                return False 
            else:
                if i==n-1 and temp.children[word[i]].flag==1:
                    return 1
            temp=temp.children[word[i]] 
        return 0
        

    def startsWith(self, prefix: str) -> bool:
        n=len(prefix)
        temp=self.root
        for i in range(n): 
            if temp and prefix[i] not in temp.children:
                return 0 
            else:
                temp=temp.children[prefix[i]] 
        return 1


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)