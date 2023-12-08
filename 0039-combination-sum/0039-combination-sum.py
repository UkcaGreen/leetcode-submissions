class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        results = []
        
        current = []
        
        candidates = sorted(candidates)
        
        def foo(target, prev_value):
            
            nonlocal current, results
            
            if target == 0:
                return results.append(current)
            
            for c in candidates:
                
                if c > target:
                    continue
                    
                if c < prev_value:
                    continue
                    
                current.append(c)
                
                foo(target - c, c)
                
                current = current[:-1]
        
        foo(target, -1)
        
        return results
            
            
            