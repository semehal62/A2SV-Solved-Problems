# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(head):
            prev = None
            curr = head
            nxt = curr.next
            while nxt:
                curr.next = prev
                prev = curr
                curr = nxt
                nxt = nxt.next
                
            curr.next = prev

            return curr
       

        curr = reverse(head)
        head = curr
        after = curr.next
        while after:
            if  curr.val <= after.val:
                curr.next = after
                curr = after
            after = after.next

        curr.next = after


            
        return reverse(head)