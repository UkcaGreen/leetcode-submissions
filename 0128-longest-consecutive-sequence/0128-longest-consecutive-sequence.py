class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set(nums)
        
        longest_sequence_lenght = 0
        
        for n in nums:
            
            if (n - 1) in num_set:
                continue
                
            sequence_lenght = 0
            
            while (n + sequence_lenght) in num_set:
                sequence_lenght += 1
                
            if sequence_lenght > longest_sequence_lenght:
                longest_sequence_lenght = sequence_lenght
        
        return longest_sequence_lenght
                
                