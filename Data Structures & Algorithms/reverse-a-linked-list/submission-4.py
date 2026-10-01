# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr_node = head
        prev_node = None
        temp = head
        while temp is not None:
            temp = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            print(prev_node.val)
            curr_node = temp
        head = prev_node
        return head
            
            
            
        