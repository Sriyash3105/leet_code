
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        if not l1 :
            return l2
        if not l2 :
            return l1
        carryOver = 0
        node = ListNode()
        curr = node
        while l1 or l2 or carryOver:
            if l1 is None:
                first = 0
            else:
                first = l1.val
            if l2 is None:
                second = 0
            else:
                second = l2.val
            add = first + second +carryOver
            curr.next = ListNode(add%10)
            carryOver = add//10
            curr = curr.next
            if l1:
                l1 = l1.next 
            else:
                l1 = None
            if l2:
                l2 = l2.next 
            else:
                l2 = None
        return node.next    

        