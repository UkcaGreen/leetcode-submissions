# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # split
        fast = head.next
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        first = head
        second = slow.next
        slow.next = None
        
        # reverse 2nd list
        curr, prev = second, None
        while curr:
            temp = curr.next
            
            curr.next = prev
            
            prev = curr
            curr = temp
        
        second = prev
            
        # merge
        
        while second:
            
            first_tmp, second_tmp = first.next, second.next
            
            first.next = second
            second.next = first_tmp
            
            first, second = first_tmp, second_tmp
            
            

                
                
            
            
        
        