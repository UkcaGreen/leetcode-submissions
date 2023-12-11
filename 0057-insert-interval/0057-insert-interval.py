class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        ans = []
        
        new_l, new_r = newInterval
        
        is_new_interval_inserted = False
        
        for l, r in intervals:
            
            if is_new_interval_inserted:
                ans.append([l,r])
            
            elif r < new_l:
                ans.append([l,r])
            
            elif (r >= new_l >= l) or (r >= new_r >= l):
                new_l, new_r = min(l, new_l), max(r, new_r)
            
            elif l > new_r:
                ans.append([new_l, new_r])
                ans.append([l, r])
                is_new_interval_inserted = True
        
        if not is_new_interval_inserted:
            ans.append([new_l, new_r])
            
        return ans
            
            
            
            
            
                
            
            