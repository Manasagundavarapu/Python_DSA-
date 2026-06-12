class Solution:
    def reverse(self, head):
        prev = None
        temp = head

        while temp:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front

        return prev
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True

        slow = head
        fast = head

        # Find middle
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        newHead = self.reverse(slow.next)

        first = head
        second = newHead

        # Compare both halves
        while second is not None:
            if first.val != second.val:
                self.reverse(newHead)   # restore list
                return False

            first = first.next
            second = second.next

        # Restore list
        self.reverse(newHead)

        return True
