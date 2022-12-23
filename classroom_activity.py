#Given a list [1, 2, 3, 4, 5] and a number 3, rotate the items in 
#the list 3 places over to the right. The output would be: [3, 4, 5, 1, 2].

# Version 1: with additional list
def rotate_list_left_v1(list, shift_by):
    temp_list = [0] * (len(list))
    if len(list) < shift_by:
        shift_by = shift_by % len(list)
    
    for index in range(len(list)):
        if index + shift_by < len(list):
            temp_list[index] = list[index + shift_by - 1]
        else:
            temp_list[index] = list[index + shift_by - 1 - len(list)]
    list = temp_list
    return list

# Version 2: without additional list
def rotate_list_left_v2(list, shift_by):
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

# Testing

#input_list = [1, 2, 3, 4, 5]
#shift_by = 8
#print("Input list: ", input_list)
#print("shift left by: ", shift_by)
#print("Shifted_list(Version 1): ", rotate_list_left_v1(input_list, shift_by))
#print("Shifted_list(Version 2): ", rotate_list_left_v2(input_list, shift_by))

################################################################################

# Imagine a skyline of buildings and you were standing in front of them 
# at ground level 0. How many of these buildings could you see?

# Given a list [-1, 1, 3, 7, 7, 3], determine which values could be "seen."
# Output: [1,3,7]

building_list = [-1, 1, 3, 7, 7, 3]
def skyline(building_list):
    result_list = []
    max = building_list[0]
    for element in building_list:
        if element > max:
            result_list.append(element)
            max = element
    return result_list

# Testing
#print("Building list: ", building_list)
#print("We see buildings: ", skyline(building_list))
#################################################################################