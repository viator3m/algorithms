class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return self.value


def print_linked_link(vertex):
    while vertex:
        print(vertex.value, end=' -> ')
        vertex = vertex.next
    print('None')


def get_node_by_index(node: Node, index: int) -> Node:
    while index:
        node = node.next
        index -= 1
    return node


def insert_node(head: Node, index: int, value: str) -> Node:
    new_node = Node(value)
    if index == 0:
        new_node.next = head
        return new_node
    previous_node = get_node_by_index(head, index - 1)
    new_node.next = previous_node.next
    previous_node.next = new_node
    return head


def delete_node(head: Node, index: int):
    if index == 0:
        return head.next
    previous_node = get_node_by_index(head, index - 1)
    next_node = get_node_by_index(head, index + 1)
    previous_node.next = next_node
    return head

node3 = Node('fourth')
node2 = Node('third', node3)
node1 = Node('second', node2)
node0 = Node('first', node1)

insert_node(node0, 1, 'new_node_2')

delete_node(node0, 0)


# print(get_node_by_index(node1, 2))

print_linked_link(node0)


