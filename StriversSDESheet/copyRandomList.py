class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        # If list is empty
        if not head:
            return None

        # HashMap to store original node -> copied node
        mpp = {}

        temp = head

        # Step 1: Create copy nodes
        while temp:
            newNode = Node(temp.val)
            mpp[temp] = newNode
            temp = temp.next

        temp = head

        # Step 2: Connect next and random pointers
        while temp:
            copyNode = mpp[temp]

            # Set next pointer
            copyNode.next = mpp.get(temp.next)

            # Set random pointer
            copyNode.random = mpp.get(temp.random)

            temp = temp.next

        # Return copied head
        return mpp[head]
