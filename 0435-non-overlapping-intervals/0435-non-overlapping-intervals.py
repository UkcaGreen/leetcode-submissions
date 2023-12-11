class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals = sorted(intervals)
        
        print(intervals)
        
        ans = [intervals[0]]
        count = 0
        
        for l, r in intervals[1:]:
            
            last_l, last_r = ans[-1]
            
            if l >= last_r:
                ans.append([l, r])
            else:
                ans.pop()
                
                if r > last_r:
                    ans.append([last_l, last_r])
                else:
                    ans.append([l, r])
                
                count += 1
        
        return count