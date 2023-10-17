class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def has_cycle(head):
    if not head or not head.next:
        return False

    slow = head
    fast = head.next

    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next

    return False
head = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = head

result = has_cycle(head)
print(result)
