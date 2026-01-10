# Linked list python implementation
# Singly linked list
class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

# Create first noe: Head of our linked list
head = Node(10)
# Link the second node with head
head.next = Node(20)
# Link the third node with second
head.next.next = Node(30)
# Link the fourth with third node
head.next.next.next = Node(40)

# traverse the linked list
temp_head = head
while temp_head is not None:
    print(temp_head.data, end="")
    if temp_head.next is not None:
        print(" -> ", end="")
    temp_head = temp_head.next

