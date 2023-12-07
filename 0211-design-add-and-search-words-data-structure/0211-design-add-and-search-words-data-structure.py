class TrieNode:

    def __init__(self) -> None:
        self.is_terminal = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        node = self.root

        for i, c in enumerate(word):

            if c not in node.children:
                node.children[c] = TrieNode()

            node = node.children[c]

            if i == len(word) - 1:
                node.is_terminal = True
        

    def search(self, word: str) -> bool:
        
        return self.search_util(self.root, word)
    
    def search_util(self, node, word):
        
        for i, c in enumerate(word):
            
            if c == ".":

                return any(
                    self.search_util(n, word[i+1:]) 
                    for k, n in node.children.items()
                )
            
            if c not in node.children:
                return False
            
            node = node.children[c]
        
        return node.is_terminal
        
        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)