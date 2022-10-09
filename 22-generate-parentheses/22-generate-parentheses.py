class Solution:
    result = []
    
    def generateParenthesis(self, n: int) -> List[str]:
        return self.util("", n, n, [])
        
    def util(self, current_str, remained_open, remained_close, result):
        if remained_open > 0:
            result = self.util(current_str + "(", remained_open - 1, remained_close, result)
        if remained_close > 0 and remained_close > remained_open:
            result = self.util(current_str + ")", remained_open, remained_close - 1, result)
        if remained_open == 0 and remained_close == 0:
            result.append(current_str)
        return result