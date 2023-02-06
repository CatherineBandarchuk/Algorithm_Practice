# Given an array arr of positive integers sorted in a strictly 
# increasing order, and an integer k.

# Find the kth positive integer that is missing from this array.

# Example 1:

# Input: arr = [2,3,4,7,11], k = 5
# Output: 9
# Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. 
# The 5th missing positive integer is 9.


def kth_missing_positive_number(list_of_numbers, k):
    if not isinstance(k, int) or k<=0 \
            or not isinstance(list_of_numbers, list) \
            or not all(isinstance(element, (int)) for element in list_of_numbers):
        return -1
    
    if len(list_of_numbers) == 0:
        return k

    number = 0
    index = 0

    while k > 0 and index < len(list_of_numbers):
        number += 1
        if list_of_numbers[index] == number \
                or (index + 1 < len(list_of_numbers) \
                    and list_of_numbers[index] == list_of_numbers[index+1]):
            index += 1
        else:
            k -= 1

    if k != 0 and index >= len(list_of_numbers):
        number += k
        
    return number

print(kth_missing_positive_number([2,3,4,7,11], 5))
# 9
print(kth_missing_positive_number([1,2,3,4], 2))
# 6
print(kth_missing_positive_number([2,3,4,7,11], -5))
# -1
print(kth_missing_positive_number([1,2,3,4], 0))
# -1
print(kth_missing_positive_number([ 2, 2, 3, 5, 6, 6, 7, 11, 13], 5))
# 10
print(kth_missing_positive_number([], 5))