# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        lists = [e for e in lists if e is not None]
        
        if not lists:
            return None

        result = None
        sorted_list = None
        
        while any(lists):
             
            min_val_idx = 0
            for i, node in enumerate(lists):
                if node.val <= lists[min_val_idx].val:
                    min_val_idx = i
                    
            c = lists[min_val_idx]
            lists[min_val_idx] = lists[min_val_idx].next
            c.next = None
            
            lists = [e for e in lists if e is not None]
            
            if sorted_list is None:
                sorted_list = c
                result = c
            else:
                sorted_list.next = c
                sorted_list = sorted_list.next
        
        return result