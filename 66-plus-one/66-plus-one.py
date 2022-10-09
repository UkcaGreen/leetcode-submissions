class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        reversed_digits = digits[::-1]
        
        reversed_digits[0] += 1
        overflow = 0
        
        for i in range(len(reversed_digits)):
            reversed_digits[i] += overflow
            overflow = 0
            
            if reversed_digits[i] >= 10:
                reversed_digits[i] -= 10
                overflow = 1
                
        if overflow > 0:
            reversed_digits.append(overflow)
            
        return reversed_digits[::-1]