# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        seen = set()
        if not head:
            return head
        curr = head
        seen.add(curr.val)
        while curr.next:
            if curr.next.val in seen:
                curr.next = curr.next.next
            else:
                seen.add(curr.next.val)
                curr = curr.next        
        return head
        