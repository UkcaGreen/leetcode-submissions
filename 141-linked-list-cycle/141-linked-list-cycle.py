# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        
        def foo(root):
            if not root:
                return False
            
            if id(root) in visited:
                return True
            
            visited.add(id(root))
            
            return foo(root.next)
        
        return foo(head)
        