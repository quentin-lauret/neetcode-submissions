# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = []
        head_root = head
        count = 0
        while head:
            head = head.next
            count += 1
        head = head_root
        target = count - n
        if target == 0:
            return head_root.next
        i = 1
        while i < target:
            i += 1
            head = head.next
        if head.next:
            head.next = head.next.next

        return head_root
        