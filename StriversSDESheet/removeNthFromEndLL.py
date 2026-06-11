class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


def removeKthNode(head, k):
    fast = head
    slow = head

    # Move fast pointer k steps ahead
    for i in range(k):
        fast = fast.next

    # If the first node needs to be removed
    if fast is None:
        return head.next

    # Move both pointers
    while fast.next is not None:
        fast = fast.next
        slow = slow.next

    # Delete the kth node from the end
    delNode = slow.next
    slow.next = slow.next.next

    return head
