class TrieNode:

    def __init__(self) -> None:
        self.is_terminal = False
        self.children = {}
    

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        
        node = self.root
        
        for i, c in enumerate(word):
            
            if c not in node.children:
                node.children[c] = TrieNode()
                
            node = node.children[c]

            if i == len(word) - 1:
                node.is_terminal = True
    
        
    def search(self, word: str) -> bool:
        
        node = self.root
        
        for i, c in enumerate(word):
            
            if c not in node.children:
                return False
            
            node = node.children[c]
        
        return node.is_terminal

    def startsWith(self, prefix: str) -> bool:

        node = self.root
        
        for i, c in enumerate(prefix):
            
            if c not in node.children:
                return False
            
            node = node.children[c]
        
        return True
        
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)