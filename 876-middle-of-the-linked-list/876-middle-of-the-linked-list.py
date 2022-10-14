# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def foo(root):
            if not root:
                return 0
            
            return foo(root.next) + 1
        
        length = foo(head)
        middle_idx = length // 2
        
        curr = head
        for i in range(middle_idx):
            curr = curr.next
            
        return curr