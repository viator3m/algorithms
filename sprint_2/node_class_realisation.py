from D_careful_mom import get_index_of_value


class Node:
    def __init__(self, value, next=None, previous=None):
        self.value = value
        self.next = next
        self.prev = previous

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


def list_reverse(head):
    node, new_head = head, head
    while node:
        node.prev, node.next = node.next, node.prev
        new_head = node if node else new_head
        node = node.prev
    return new_head


node3 = Node('fourth')
node2 = Node('third')
node1 = Node('second')
node0 = Node('first')

node0.next = node1

node1.prev = node0
node1.next = node2

node2.prev = node1
node2.next = node3

node3.prev = node2

# insert_node(node0, 1, 'new_node_2')

# delete_node(node0, 0)

# print(get_node_by_index(node1, 2))
# print(get_index_of_value(node0, 'second'))

print_linked_link(node0)

print(list_reverse(node0))

print_linked_link(node3)
