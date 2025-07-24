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


print(printLinkedList(node1))


def rotateByK(head, k):

    if k == 0 or head is None:
        return head

    len = 1
    cur = head
    while cur.next is not None:
        len += 1
        cur = cur.next

    k = k % len

    cur.next = head

    cur = head

    for i in range(1, k):
        cur = cur.next

    head = cur.next
    cur.next = None

    return head


print(printLinkedList(rotateByK(node1, 4)))
