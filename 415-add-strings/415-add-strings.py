class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans = ""
        
        num1, num2 = (num1, num2) if len(num1) > len(num2) else (num2, num1)
        num1, num2 = num1[::-1], num2[::-1]
        
        carry = 0
        for i in range(len(num1)):
            digit1, digit2 = (num1[i], num2[i]) if len(num2) > i else (num1[i], 0)
            
            intermediate_sum = int(digit1) + int(digit2) + carry
            
            ans += str(intermediate_sum % 10)
            carry = intermediate_sum // 10
            
        if carry != 0:
            ans += str(carry)
            
        return ans[::-1]