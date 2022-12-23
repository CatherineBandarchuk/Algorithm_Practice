# Given two arrays, create your own concatenation function. 
# Return a new array containing the first array's values, 
# then the second array's values. Try not to use built-in 
# methods (append, pop, len are all ok).  
# Don't forget edge cases!

# Example Input: ["a", "b", "c"], [1, 2, 3]
# Example Output: ["a", "b", "c", 1, 2, 3]

def concatenated_list(list1, list2):
    number_of_elements = 0
    while number_of_elements < len(list2):
        list1.append(list2[0])
        list2.remove(list2[0])

    return list1

# Testing
#print(concatenated_list(["a", "b", "c"], [1, 2, 3]))
#print(concatenated_list([True, False], [1 ,3 ,5 ,4 ]))

##################################################################################
# Given an array, find the smallest value and move it to 
# the front of the array. Return the same array. Try not to use 
# built-in methods. Don't forget edge cases!

#Example Input: [3, 4, 2, 9, 1, 8, 7, 6]
#Example Output: [1, 3, 4, 2, 9, 8, 7, 6]

#Example Input: [3, 4, 2, 9, 1, 8, 1, 7, 6]
#Example Output: [1, 3, 4, 2, 9, 8, 1, 7, 6]

def minimum_first_element(my_list):
    minimum = my_list[0]
    min_index = 0
    for index in range(len(my_list)):
        if my_list[index] < minimum:
            minimum = my_list[index]
            min_index = index
    
    temp_from = my_list[0]
    my_list[0] = minimum
    step = min_index
    i = 0
    

    while step > 0:
        step -= 1       
        temp_to = my_list[i + 1]
        my_list[i + 1] = temp_from
        i += 1
        temp_from = temp_to
    return my_list

print(minimum_first_element([3, 4, 2, 9, 1, 8, 7, 6]))
print(minimum_first_element([3, 4, 2, 9, 1, 8, 1, 7, 6]))