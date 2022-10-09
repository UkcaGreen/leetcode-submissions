class Solution:
    def isValid(self, s: str) -> bool:
        open_to_close = {"(":")", "[":"]", "{":"}"}
        stack = []
        for c in s:
            if c in open_to_close:
                stack.append(c)
                continue
            
            if stack and c == open_to_close[stack[-1]]:
                stack.pop()
                continue
                
            print(stack)
                
            return False
        
        return len(stack) == 0