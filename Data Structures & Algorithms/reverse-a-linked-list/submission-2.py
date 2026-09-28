# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        temp = head
        while temp is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            if temp != None:
                curr = temp
        head = curr
        return head



        