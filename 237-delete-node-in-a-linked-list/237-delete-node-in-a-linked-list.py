# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        def foo(root):
            if not root:
                return
            
            root.val = root.next.val

            if not root.next.next:
                root.next = None
            
            foo(root.next)
            
        foo(node)