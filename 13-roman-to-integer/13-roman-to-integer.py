class Solution:
    def romanToInt(self, s: str) -> int:
        value = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        total_sum = 0
        
        for i in range(len(s)-1):
            current_letter, next_letter = s[i], s[i+1]
            
            if value[current_letter] < value[next_letter]:
                total_sum -= value[current_letter]
            else:
                total_sum += value[current_letter]
                
        total_sum += value[s[-1]]
                
        return total_sum