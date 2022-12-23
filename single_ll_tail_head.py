# Defines a node in a singly linked list with head and tail
class Node:
    def __init__(self, value, next = None):
        self.val = value
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail= None

    def add_first(self, value):
        if self.head == None:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            self.tail = self.head
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node

    def get_first(self):
        if self.head == None:
            return None
        return self.head.val
    
    def get_last(self):
        if self.head == None:
            return None
        return self.tail.val

    def add_last(self, value):
        if self.head == None:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            self.tail = self.head
        else:
            new_node = Node(value)
            self.tail = new_node

    def find_element(self, value):
        current = self.head
        while current != None:
            if current.val == value:
                return True
            current = current.next
        return False

    def print_all_element_in_ll(self):
        if self.head == None:
            return None
        current = self.head
        while current!= None:
            print(current.val)
            current = current.next

    def remove_last(self):
        if self.head == None:
            return None
        elif self.head == self.tail:
            data = self.tail.val
            self.head = None
            self.tail = None
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next

            data = self.tail.val
            self.tail = current
            self.tail.next = None
        return data

new_linked_list = LinkedList()
new_linked_list.add_first(1)
new_linked_list.add_first(2)
new_linked_list.add_first(3)
new_linked_list.add_first(4)
new_linked_list.add_first(5)
new_linked_list.add_first(6)
new_linked_list.add_last(0)

print(new_linked_list.find_element(0))
new_linked_list.print_all_element_in_ll()
print("Last element: ", new_linked_list.get_last())
print("First element: ", new_linked_list.get_first())
print("Removed last element: ", new_linked_list.remove_last())
print("Removed last element: ", new_linked_list.remove_last())

new_linked_list.print_all_element_in_ll()