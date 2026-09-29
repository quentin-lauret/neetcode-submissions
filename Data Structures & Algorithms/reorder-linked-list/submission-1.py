# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        if head.next is None:
            return 
        last = head
        current = head
        l = []
        prev = {}
        while last.next:
            prev[last.next] = last
            last = last.next
            l.append(last)
        while current.next:
            curr_next = current.next
            prev[l[-1]].next = None
            current.next = l[-1]
            if l[-1] == curr_next:
                break
            l[-1].next = curr_next
            current = curr_next
            l.pop()