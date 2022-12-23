# Given an array and a value, append the new value to the front of the array. 
# Do not use any built-in array methods, like insert, shift, slice [:], etc. 
# Do this manually. You can use len, pop, append. Return the same array. 
# Don't forget edge cases!

#Example Input: [1, 2, 3, 4, 5, 6], 10
#Example Output: [10,1, 2, 3, 4, 5, 6]

def add_to_front(list, element, shift = None):
    if shift == None:
        shift = 0
    if not list:
        return element
    last_index = len(list)
    list.append(element)
    itterator = 0
    while itterator < last_index - shift:
        removed_item = list.pop(0)
        list.append(removed_item)
        itterator +=1
    return list

# Testing
list1 = [1, 2, 3, 4, 5, 6]
element1 = 10
print(add_to_front(list1, element1))

###########################################################################

# Given an array, a value, and an index position, insert the new value at 
# the designated position. Do not use any built-in array methods. 
# Return the same array. Don't forget edge cases!

#Example Input1: [1, 2, 3], 4, 1
#Example Output1: [1, 4, 2, 3]

#Example Input2: [1, 2, 3, 4, 5], 6, 7
#Example Output2: [1, 2, 3, 4, 5, None, None, 6]

# if position > len(list) append None (position - len(list)) times 
# then append our element
# if position == len(list) append element
# if position < len(list) append element and use pop append times = len(list) + position - 1

def insert_at_position(list, element, position):
    last_index = len(list)
    if position > last_index:
        for i in range(position-last_index):
            list.append(None)
        list.append(element)
    elif position == last_index:
        list.append(element)
    else:
        list.append(element)
        itterator = 0
        while itterator < last_index - position:
            removed_item = list.pop(0)
            list.append(removed_item)
            itterator +=1
    return list

# Testing
list1 = [1, 2, 3]
print(insert_at_position(list1, 4, 1)) 
#list2 = [1, 2, 3, 4, 5]
#print(insert_at_position(list2, 6, 7))
#print(insert_at_position(list2, 6, 0))
#print(insert_at_position(list2, 6, -3))
###########################################################################

# Seems like a lot of duplicate code. How could we modify add_to_front so 
# we can use it as a helper function for insert? 

def insert_at_position_with_helper(list, element, position):
    last_index = len(list)
    if position > last_index:
        for i in range(position-last_index):
            list.append(None)
        list.append(element)
    elif position == last_index:
        list.append(element)
    else:
        list = add_to_front(list, element, position)
    return list
list1 = [1, 2, 3]
print(insert_at_position_with_helper(list1, 4, 1))
