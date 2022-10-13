# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        itr = None
        extra = 0
        while l1 or l2:
            
            val = getattr(l1, "val", 0) + getattr(l2, "val", 0) + extra
            
            node = ListNode(
                val=val%10
            )
            extra = val // 10
            
            if not head:
                head = node
                
            if itr:
                itr.next = node
                itr = itr.next
            else:
                itr = node
            
            l1, l2 = l1 and l1.next, l2 and l2.next
        
        if extra != 0:
            itr.next = ListNode(
                val=extra
            )
        
        return head
                
            