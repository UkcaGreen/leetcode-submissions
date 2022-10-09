# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sorted_list = sorted(self.linked_list_to_list(list1) + self.linked_list_to_list(list2))
        return self.list_to_linked_list(sorted_list)
        
    def linked_list_to_list(self, linked_list):
        itr = linked_list
        result = []
        while itr:
            result.append(itr.val)
            itr = itr.next
        return result
    
    def list_to_linked_list(self, _list):
        if not _list:
            return None
        
        head = ListNode(val=_list[0])
        
        itr = head
        
        for i in range(1, len(_list)):
            itr.next = ListNode(val=_list[i])
            itr = itr.next
        
        return head
        