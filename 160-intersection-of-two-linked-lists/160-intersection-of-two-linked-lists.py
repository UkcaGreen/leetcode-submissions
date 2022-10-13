# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        visited = set()
        
        def foo(root):
            if not root:
                return None
            
            if id(root) in visited:
                return root
            
            visited.add(id(root))
            
            return foo(root.next)
        
        foo(headA)
        ans = foo(headB)
        return ans