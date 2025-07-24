class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


def insert_at_beginning(data, next):
    return Node(data, next)


node5 = insert_at_beginning(50, None)
node4 = insert_at_beginning(40, node5)
node3 = insert_at_beginning(30, node4)
node2 = insert_at_beginning(20, node3)
node1 = insert_at_beginning(10, node2)


def printLinkedList(head):

    cur = head
    while cur:
        print(cur.data, "-->", end=" ")
        cur = cur.next


def reverseLinkedList(head):
    prev = None
    cur = head

    while cur:
        next = cur.next
        cur.next = prev

        prev = cur
        cur = next

    return prev


print(printLinkedList(reverseLinkedList(node1)))
