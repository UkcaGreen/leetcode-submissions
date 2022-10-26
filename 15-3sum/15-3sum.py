class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        pos, neg, zero = [e for e in nums if e > 0], [e for e in nums if e < 0], [e for e in nums if e == 0]
        pos_set, neg_set = set(pos), set(neg)
        
        if len(zero) >= 1:
            for e in pos:
                if -e in neg:
                    trio = sorted([-e,0,e])
                    if trio not in ans:
                        ans.append(trio)
        
        if len(zero) >= 3:
            ans.append([0,0,0])
            
        for i, e1 in enumerate(pos):
            for e2 in pos[i+1:]:
                if -(e1 + e2) in neg_set:
                    trio = sorted([e1,e2, -(e1 + e2)])
                    if trio not in ans:
                        ans.append(trio)
        
        for i, e1 in enumerate(neg):
            for e2 in neg[i+1:]:
                if -(e1 + e2) in pos_set:
                    trio = sorted([e1,e2, -(e1 + e2)])
                    if trio not in ans:
                        ans.append(trio)     
        
        return ans
        
