# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = []
        curr = head
        if curr == None:
            return
        while curr is not None:
            seen.append(curr)
            curr = curr.next
        new_head = seen.pop()
        curr = new_head
        while seen:
            curr.next = seen.pop()
            curr = curr.next
        curr.next = None
        return new_head



            
        