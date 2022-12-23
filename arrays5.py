# Given an array and a number n, return the nth-largest 
# number in the array. Don't forget edge cases!

#Example Input: [5, 8, 1, 3, 7, 5, 6], 3
#Example Output: 6

#Example Input: [3, 1, 5], 5
#Example Output: None

def nth_large_number(list,number):
    if number > len(list):
        return None
    if not isinstance(number, int) or \
        not all(isinstance(item , int) for item in list):
        return TypeError("Numbers needs to be int type")
    print(list)
    list.sort() 
    print(list)
    return list[-number]

# Testing
#print(nth_large_number([5, 8, 1, 3, 7, 5, 6], 3))
#print(nth_large_number([3, 1, 5], 5))

#######################################################
# Given an array, a start position, and an end position, 
# remove the values within that start-end range "in-place,"
# then return the original array. Don't use slice. 
# Don't forget edge cases!

#Example Input: [5, 8, 1, 3, 7, 5, 6,10], 3, 6
#Example Output: [5, 8, 1, 10]

def remove_element(list, start, end):
    if start < 0 or start > len(list):
        return list

    if end > len(list):
        steps = (len(list) - start)
    else:
        steps = (end - start) + 1
    itterator = 0 
    while itterator < steps:
        list.pop(start)
        itterator += 1
    return list

#print(remove_element([5, 8, 1, 3, 7, 5, 6,10], 3, 6))
#print(remove_element([4, 5, 6, 7, 10, 11, 12, 13], 5,7))
print(remove_element([4, 5, 6, 7, 10, 11, 12, 13], 7, 11))
