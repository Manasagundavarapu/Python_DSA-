class Solution:

    def reverseLinkedList(self, head):
        prev = None
        temp = head

        while temp:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front

        return prev

    def getKthNode(self, temp, k):
        k -= 1

        while temp is not None and k > 0:
            k -= 1
            temp = temp.next

        return temp
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        prevLast = None

        while temp is not None:
            kThNode = self.getKthNode(temp, k)

            if kThNode is None:
                if prevLast:
                    prevLast.next = temp
                break

            nextNode = kThNode.next
            kThNode.next = None

            self.reverseLinkedList(temp)

            if temp == head:
                head = kThNode
            else:
                prevLast.next = kThNode

            prevLast = temp
            temp = nextNode

        return head
