from linked_list import *

if __name__ == '__main__':

    print("First way of populating:")
    llist = LinkedList()
    n1 = Node(1)
    llist.head = n1
    n2 = Node(2)
    n1.next = n2
    n3 = Node(3)
    n2.next = n3
    print(llist)
    print("=======================")

    print("Second way of populating:")
    llist = LinkedList([1, 2, 3])
    print(llist)

    print("Traversing linked list:")
    for i, node in enumerate(llist):
        print(f'Node {i+1}: {node}')
    print("=====================")

    print("Adding element in 1st position:")
    llist.add_first(Node(0))
    print(f'First element: {llist.head}')
    print("=====================")

    print("Adding element in last position:")
    llist.add_last(Node(4))
    print(f'Last element: {llist.get_last()}')
    print("=====================")

    print("Deleting element")
    llist.delete(0)
    print(llist)
