# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head
        last_zero = None
        current_sum = 0

        dummy = ListNode()
        result_iter = dummy

        while curr:
            if curr.val == 0:
                if last_zero:
                    result_iter.next = ListNode(current_sum)
                    result_iter = result_iter.next
                    last_zero = curr
                    current_sum = 0
                else:
                    last_zero = curr
            
            current_sum += curr.val
            curr = curr.next
        
        return dummy.next