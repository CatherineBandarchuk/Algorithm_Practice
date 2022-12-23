# Imagine working on software that processes linked lists. 
# Create a function named rotate_list that accepts a linked 
# list and rotates it k places to the right. This function 
# should take in the head of a linked list which has at least 
# two nodes and a non-negative integer k. The function should 
# return the head of the rotated list.

# List	                    k	    Output
# a -> b -> c -> d -> e	    1	    e -> a -> b -> c -> d
# a -> b -> c -> d -> e	    2	    d -> e -> a -> b -> c
# 1 -> 2	                5	    2 -> 1

class Node:
    def __init__(self, value, next=None):
        self.value = value 
        # if next is None, this is the last element in the list
        self.next = next

    def __eq__(self, other):
        '''
        Understanding this function is NOT necessary for solving the problem;
        it is only used for the assertions.
        Feel free to explore your curiosity of how this works after the interview :)
        '''
        try:
            return (type(other) == Node and 
                    self.value == other.value and 
                    self.next == other.next)
        except RecursionError:
            raise Exception("Linked list has a cycle or is too large")

# example input 1
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
a.next = b
b.next = c
c.next = d
d.next = e
lst1 = a
k1 = 1
# expected output 1: lst1 = e

# example input 2:
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
a.next = b
b.next = c
c.next = d
d.next = e
lst2 = a
k2 = 8
# expected output 2: lst2 = c

# example input 3:
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
a.next = b
b.next = c
c.next = d
d.next = e
lst3 = a
k3 = 0
# expected output 3: lst3 = a

# example input 4:
a = Node('a')
b = Node('b')
c = Node('c')
a.next = b
b.next = c
lst4 = a
k4 = "7"
# expected output 4: TypeError raised

# example input 5:
a = Node('a')
a.next = None
lst5 = a
k5 = -7
# expected output 5: Attribute Error raised

# example input 6:
a = Node('a')
b = Node('b')
c = Node('c')
a.next = b
b.next = c
lst6 = a
k6 = -3
# expected output 4: Attribute Error raised

def rotate_list(head, k):
    if not isinstance(k, int): raise TypeError
    elif k == 0: return head
    elif k < 0: raise AttributeError
    else:       
        if not head or not head.next:
            return head
    current = head
    number_of_elements = 1
    while current.next != None:
        current = current.next
        number_of_elements += 1
    current.next = head
    current = current.next
    step = 0    
    while step < (number_of_elements - (k % number_of_elements) - 1):
        current = current.next
        step += 1
    head = current.next
    current.next = None
    return head

print(f"Linked List (head):{lst1.value} with rotation step(k): {k1} have new head: {rotate_list(lst1, k1).value}") 
print(f"Linked List (head):{lst2.value} with rotation step(k): {k2} have new head: {rotate_list(lst2, k2).value}")
print(f"Linked List (head):{lst3.value} with rotation step(k): {k3} have new head: {rotate_list(lst3, k3).value}") 
#print(f"Linked List (head):{lst5.value} with rotation step(k): {k5} have new head: {rotate_list(lst5, k5).value}") 
#print(f"Linked List (head):{lst6.value} with rotation step(k): {k6} have new head: {rotate_list(lst6, k6).value}")
#print(f"Linked List (head):{lst4.value} with rotation step(k): {k4} have new head: {rotate_list(lst4, k4).value}")