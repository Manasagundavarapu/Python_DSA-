class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
head=Node(10)
head.next=Node(20)
head.next.next=Node(60)
temp=head
while temp.next.next is not None:
    temp=temp.next
temp.next=None
temp=head
while(temp!=None):
    print(temp.data,end="->")
    temp=temp.next
