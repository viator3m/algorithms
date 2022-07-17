def get_node_by_index(node, index: int):
    while index:
        node = node.next
        index -= 1
    return node


def solution(head, index: int):
    if index == 0:
        return head.next
    previous_node = get_node_by_index(head, index - 1)
    next_node = get_node_by_index(head, index + 1)
    previous_node.next = next_node
    return head
