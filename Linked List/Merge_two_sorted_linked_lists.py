class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


def insert_at_beginning(data, next):
    return Node(data, next)


node4 = insert_at_beginning(40, None)
node3 = insert_at_beginning(15, node4)
node2 = insert_at_beginning(10, node3)
node1 = insert_at_beginning(5, node2)

node23 = insert_at_beginning(20, None)
node22 = insert_at_beginning(3, node23)
node21 = insert_at_beginning(2, node22)


def printLinkedList(head):

    cur = head
    while cur:
        print(cur.data, "-->", end=" ")
        cur = cur.next


print(printLinkedList(node1))
print(printLinkedList(node21))


def mergeList(head1, head2):

    dummy = Node(-1, None)
    curr = dummy

    while head1 and head2:
        if head1.data <= head2.data:
            curr.next = head1
            head1 = head1.next
        else:
            curr.next = head2
            head2 = head2.next
        curr = curr.next

    if head1:
        curr.next = head1

    if head2:
        curr.next = head2

    return dummy.next


print(printLinkedList(mergeList(node1, node21)))
