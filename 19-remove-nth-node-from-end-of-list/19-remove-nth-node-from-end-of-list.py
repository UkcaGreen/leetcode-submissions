# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        node = head
        count = 0
        
        while node:
            count += 1
            node = node.next
            
        node = head        
        del_idx = count - n
        
        if del_idx == 0:
            return head.next

        for i in range(del_idx - 1):
            node = node.next
            
        node.next = node.next.next
        
        return head
            