"""
# Definition for a Node.
class ≈:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return node
        
        old_to_new = {}
        
        def dfs(node):
            
            if node in old_to_new:
                return old_to_new[node]
            
            old_to_new[node] = Node(node.val)
            
            for n in node.neighbors:
                
                old_to_new[node].neighbors.append(dfs(n))
                
            return old_to_new[node]
                
        dfs(node)
        
        return old_to_new[node]