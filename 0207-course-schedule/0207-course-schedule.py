class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        while prerequisites:
            
            source = {e[0] for e in prerequisites}
            target = {e[1] for e in prerequisites}
            
            nodes_to_prune = target.difference(source)
            
            if not nodes_to_prune:
                return False
            
            prerequisites = [p for p in prerequisites if p[1] not in nodes_to_prune]
        
        
        return True
        
        def dfs(n, s):
            
            if n in s:
                return False
            
            neighbors = [e[1] for e in prerequisites if e[0] == n]
            
            result = True
            
            for neighbor in neighbors:
                s.append(n)
                result = result and dfs(neighbor, s)
                s.pop()
            
            return result
        
        x = {e[0] for e in prerequisites}
    
        return all(dfs(i, []) for i in x)
            
            
            
            