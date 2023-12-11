class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = sorted(intervals)
        
        ans = [intervals[0]]

        for l, r in intervals[1:]:
            
            print(l, r)
            
            last_l, last_r = ans[-1]
            
            if l > last_r:
                ans.append([l, r])
            else:
                ans.pop()
                ans.append([min(l, last_l), max(r, last_r)])
        
        return ans
                
                
            
                
            
            

        