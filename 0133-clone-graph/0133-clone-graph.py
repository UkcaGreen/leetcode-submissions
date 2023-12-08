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
        
        edges = {}
        
        visited = set()
        
        def dfs(node):
            
            if not node:
                return
            
            if node.val in visited:
                return
            
            visited.add(node.val)
            edges[node.val] = [n.val for n in node.neighbors]
            
            for n in node.neighbors:
                
                dfs(n)
                
        dfs(node)
        
        if not visited:
            return node
        
        new_nodes = {node_val: Node(node_val, []) for node_val in edges}
        
        for n, neighbor_vals in edges.items():
            
            for neighbor_val in neighbor_vals:
            
                new_nodes[n].neighbors.append(new_nodes[neighbor_val])
        
        return new_nodes[1]