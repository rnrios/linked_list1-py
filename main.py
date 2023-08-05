from linked_list import *
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    llist = LinkedList()

    n1 = Node(1)
    llist.head = n1

    n2 = Node(2)
    n1.next = n2

    n3 = Node(3)
    n2.next = n3

    print(llist)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
