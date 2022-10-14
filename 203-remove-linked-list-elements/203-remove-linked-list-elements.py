# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        def foo(root, delete_value):
            if not root:
                return
                
            next_node = foo(root.next, delete_value)
            
            if next_node and next_node.val == delete_value:
                root.next = next_node.next

            return root
                
        temp_node = ListNode(next=head) 
            
        return foo(temp_node, val).next