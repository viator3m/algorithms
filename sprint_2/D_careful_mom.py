# Rename function as "solution" before submitting

def get_index_of_value(head, value):
    node = head
    index = 0
    while node is not None:
        if node.value == value:
            return index
        node = node.next_item
        index += 1
    return -1
