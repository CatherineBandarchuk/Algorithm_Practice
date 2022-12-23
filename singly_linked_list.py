# Defines a node in a singly linked list with only Head
class Node:
    def __init__(self, value):
        self.val = value
        self.next = None
    
    #def add_first(current_head, current_vallue):
    #    return new_node.__init__(current_head, current_vallue)

    #def get_last(head):
    #    if head == None:
    #        return None
    #    current = head
    #    while current.next != None:
    #        current = current.next 
    #    return current.val

    #def add_last(head, value):
    #    current = head
    #    while current.next != None:
    #        current = current.next
    #    new_node = Node(value)
    #    current.next = new_node

class LinkedList:
    def __init__(self):
        self.head = None

    def add_first(self, value):
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
        current = self.head
        while current.next != None:
            current = current.next
        return current.val

    def add_last(self, value):
        if self.head == None:
            new_node = Node(value)
            self.head = new_node
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node

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
