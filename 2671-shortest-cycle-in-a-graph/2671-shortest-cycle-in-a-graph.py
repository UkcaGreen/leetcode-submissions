class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:

        graph = {x:[] for x in range(n)}
        for u, v in edges:
            graph[u].append(v) 
            graph[v].append(u) 

        min_path_len = float("inf")

        for source_node, target_node in edges:
            # calculate shortest path from source_node to target_node
            queue = [(source_node, target_node, 0)]
            visited = set()
            
            while queue:
                node, parent, level = queue.pop()

                if node in visited:
                    continue
                visited.add(node)

                if node == target_node:
                    min_path_len = min(min_path_len, level + 1)
                    break

                for neighbor in graph[node]:
                    if neighbor == parent:
                        continue
                    queue.insert(0, (neighbor, node, level + 1))
        
        return min_path_len if min_path_len != float("inf") else -1
