"""
Write code to remove duplicates from an unsorted linked list.
FOLLOW UP How would you solve this problem if a temporary buffer is not allowed?
"""


def remove_duplicates(head):
    if not head:
        return head
    current = head
    while current:
        running = current
        while running.next:
            if running.next.value == current.value:
                running.next = running.next.next
            else:
                running = running.next
        current = current.next
    return head
