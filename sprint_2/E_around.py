# Rename function as "solution" before submitting

def solution(head):
    node, new_head = head, head
    while node:
        node.prev, node.next = node.next, node.prev
        new_head = node if node else new_head
        node = node.prev
    return new_head
