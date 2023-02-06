# Given a nested array, "flatten" the array, so that all values are 
# in a one-dimensional array. Feel free to return a new array. 
# Don't forget your edge cases!

# Example Input: [ 1, [ 2, 3 ], 4, [ ] ]
# Example Output: [ 1, 2, 3, 4 ]

# Example Input: [ 1, [ 2, 3 ], 4, [ 5, 6, 7 ] , [ 8 ] ]
# Example Output: [ 1, 2, 3, 4, 5, 6, 7, 8 ]

def flatten_list(list_of_lists):
    flatten = []
    for row in range(len(list_of_lists)):
        index = 0
        if isinstance(list_of_lists[row], list):
            while index < len(list_of_lists[row]):
                flatten.append(list_of_lists[row][index]) 
                index+=1
        else: 
            flatten.append(list_of_lists[row])
    return flatten

# Now, try "flattening" in-place
def flatten_list_in_place(list_of_lists):
    iter = len(list_of_lists)
    while iter > 0:
        if isinstance(list_of_lists[0], list):
            for index in range(len(list_of_lists[0])):
                list_of_lists.append(list_of_lists[0][index])
        else: 
            list_of_lists.append(list_of_lists[0])
        list_of_lists.pop(0)
        iter-=1
    return list_of_lists


#list_of_lists1 = [ 1, [ 2, 3 ], 4, [ ] ]
#list_of_lists2 = [ 1, [ 2, 3 ], 4, [ 5, 6, 7 ] , [ 8 ] ]
#list_of_lists3 = [ ]
#print(flatten_list(list_of_lists3))
#print(flatten_list_in_place(list_of_lists3))

#################################################################################

# Given an array with random numbers, remove duplicates. Return a new array. 
# Don't forget your edge cases!

# Example Input: [ 1, 2, 1, 5, 1, 1, 3 ]
# Example Output: [ 1, 2, 5, 3 ]

def remove_duplicates(numbers_list):
    new_list = []
    for element in numbers_list:
        if element not in new_list:
            new_list.append(element)
    return new_list
# Now, try removing duplicates in-place
def remove_duplicates_in_place(number_list):
    index = 0
    max_index = len(number_list)
    while index < max_index:
        if number_list[index] in number_list[:index]:
            number_list.pop(index)
            max_index-=1
        else:
            index+= 1
    return number_list

num_list = [ 1, 2, 1, 5, 1, 1, 3 ]
print(remove_duplicates(num_list))
print(remove_duplicates_in_place(num_list))


