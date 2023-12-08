class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        results = set()
        
        current = []
        
        def foo(target):
            
            nonlocal current, results
            
            if target == 0:
                return results.add(tuple(sorted(current)))
            
            for c in candidates:
                
                if c > target:
                    continue
                    
                current.append(c)
                
                foo(target - c)
                
                current = current[:-1]
        
        foo(target)
        
        return results
            
            
            