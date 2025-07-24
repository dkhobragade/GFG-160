class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node


class LinkedList:
    def __init__(self):
        self.head = None  # First node of the list

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node  # If list is empty, make new node the head
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Create the linked list
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)

# Print the list
ll.print_list()


def reverseList(self, head):
    # Code here
    curr = head
    prev = None

    while curr:
        next = curr.next
        curr.next = prev

        prev = curr
        curr = next
    head = prev

    return head


print(reverseList())
