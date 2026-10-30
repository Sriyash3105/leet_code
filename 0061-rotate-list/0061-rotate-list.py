# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head or not head.next or k == 0:
            return head

        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        k %= length

        for _ in range(k):
            head = self.Onerot(head)

        return head

    def Onerot(self, head):
        curr = head
        while curr.next.next:
            curr = curr.next
        last = curr.next
        curr.next = None
        last.next = head
        return last 