class Node:
    def __init__(self, value):
        self.val = value
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_first(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_last(self, value):
        if self.head == None:
            self.add_first(value)
        else:
            new_node = Node(value)
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

# Removing a node at a specific index

    def remove(self, index):
        if not self.head:
            return None

        if index == 0:
            self.head = self.head.next
            return None

        current = self.head
        current_index = 0
        while current.next and current_index < index - 1:
            current = current.next
            current_index += 1

        if current.next:    
            current.next = current.next.next


DoubleLinkedList = LinkedList()
DoubleLinkedList.add_first(1)
DoubleLinkedList.add_first(2)
DoubleLinkedList.add_first(3)
DoubleLinkedList.add_first(4)
DoubleLinkedList.add_last(0)

DoubleLinkedList.remove(6)

