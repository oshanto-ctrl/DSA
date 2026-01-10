# Typical doubly linked list representation
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None # Previous node
        self.next = None # Next node
# obj
head = Node(10)
# Create and link the second node
head.next = Node(20)
head.next.prev = head
# Create and link the thrid node
head.next.next = Node(30)
head.next.next.prev = head.next

# Traverse the doubly linked list
temp_head = head
while temp_head is not None:
    print(temp_head.data, end="")
    if temp_head.next is not None:
        print(" <=> ", end="")
    temp_head = temp_head.next