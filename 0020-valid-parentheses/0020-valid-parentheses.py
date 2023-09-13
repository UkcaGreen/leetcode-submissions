class Solution:
    
    parentheses = {
        ")": "(",
        "]": "[",
        "}": "{",
    }
    
    def isValid(self, s: str) -> bool:
        
        stack = []
        
        for c in s:         
            if c in "([{":
                stack.append(c)
            if c in "}])":
                if len(stack) == 0:
                    return False
                
                if stack[-1] == self.parentheses[c]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0
                
                
                
                