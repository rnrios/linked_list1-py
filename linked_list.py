class LinkedList:
    def __init__(self, nodes=None):
        node = Node(nodes.pop(0)) if nodes else None
        self.head = node
        while nodes:
            node.next = Node(nodes.pop(0))
            node = node.next

    def add_first(self, node):
        assert isinstance(node, Node)
        node.next = self.head
        self.head = node

    def add_last(self, node_to_add):
        assert isinstance(node_to_add, Node)
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = node_to_add

    def get_last(self):
        node = self.head
        while node.next is not None:
            node = node.next
        return node

    def delete(self, value):
        prev, node = None, self.head
        while node.next is not None:
            if node.data == value:
                if prev is not None:
                    prev.next = node.next
                else:
                    self.head = node.next
                del node
                print("Node deleted!")
                return
            prev = node
            node = node.next
        print("Node not found!")

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

    def __str__(self):
        return str(self.data)
