#Given an array, reverse the order of values without using 
# the built-in method reverse or slice, 
# ie. [: :-1]. Return the same array. Don't forget edge cases!

#Example Input: [1, 2, 3, 4, 5, 6]
#Example Output: [6, 5, 4, 3, 2, 1]

def reverse_array(list):
    last_index = len(list)-1
    for index in range(len(list)//2):
        temp = list[index] 
        list[index] = list[last_index-index]
        list[last_index-index] = temp
    return list

# Testing

#print(reverse_array([-1, 0, 3, 1, 4, 'a', True]))
#print(reverse_array([1, 2, 3, 4, 5, 6]))
#print(reverse_array([]))

#############################################################################
# Given an array and number, rotate the values of the array 
# to the right by that number. Don't use slice. Return the 
# same array. Don't forget edge cases!

def shift_list_right(list, shift_by):
    if len(list) < shift_by:
        shift_by = shift_by % len(list)
    step = len(list)
    i = 0
    temp_from = list[i]

    while step > 0:
        step -= 1       
        if i+shift_by > len(list)-1:
            i -= (len(list))

        temp_to = list[i + shift_by]
        list[i + shift_by] = temp_from
        i += shift_by
        temp_from = temp_to

    return list

print(shift_list_right([1, 2, 3, 4, 5], 2))
print(shift_list_right([1, 2, 3, 4, 5], 5))

#Example Input: [1, 2, 3, 4, 5], 2
#Example Output: [4, 5, 1, 2, 3]

#Example Input: [1, 2, 3, 4, 5], 5
#Example Output: [1, 2, 3, 4, 5]

#EXTRA CHALLENGE
#Try shifting to the left instead

def rotate_list_left(list, shift_by):
    if len(list) < shift_by:
        shift_by = shift_by % len(list)
    step = len(list)
    i = 0
    temp_from = list[i + shift_by-1]

    while step > 0:
        step -= 1       
        if i < 0:
            i += (len(list))

        temp_to = list[i]
        list[i] = temp_from
        i -= shift_by-1
        temp_from = temp_to

    return list

print(rotate_list_left([1, 2, 3, 4, 5], 4)) # [4, 5, 1, 2, 3]