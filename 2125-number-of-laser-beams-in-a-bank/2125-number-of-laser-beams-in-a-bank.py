class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        
        device_counts_per_row = [r.count("1") for r in bank]
        non_zero_device_counts = [c for c in device_counts_per_row if c != 0]
        
        ans = 0
        
        for i in range(0, len(non_zero_device_counts) - 1):
            
            ans += non_zero_device_counts[i] * non_zero_device_counts[i+1]
        
        return ans
        
        