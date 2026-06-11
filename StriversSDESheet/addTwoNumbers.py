class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    dummy = ListNode()
    temp = dummy
    carry = 0

    while l1 is not None or l2 is not None or carry:

        total = 0

        if l1 is not None:
            total += l1.val
            l1 = l1.next

        if l2 is not None:
            total += l2.val
            l2 = l2.next

        total += carry

        carry = total // 10

        node = ListNode(total % 10)
        temp.next = node
        temp = temp.next

    return dummy.next
