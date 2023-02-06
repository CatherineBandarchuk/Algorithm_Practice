# Given an array of random numbers, decide if one side's sum is equal 
# to the other's. This means it has a balance point between indices. 
# If so, return True, else return False. 
# Don't forget your edge cases!

#Example Input: [ 2, 4, 1, 7 ]
#Example Output: True (2+4+1 = 7)

#Example Input: [ 5, 3, 1, 7 ]
#Example Output: True (5+3 = 1+7)

#Example Input: [ 2, 4, 1, 3, 8 ]
#Example Output: False

def sides_sum_equal(numbers_list):
    left_i = 0
    right_i = len(numbers_list)-1
    sum_left = numbers_list[left_i]
    sum_right = numbers_list[right_i]
    while left_i < right_i and left_i < len(numbers_list) and right_i > 0 :
        if sum_left < sum_right:
            left_i+= 1
            sum_left += numbers_list[left_i]
        elif sum_left > sum_right:
            right_i-=1
            sum_right += numbers_list[right_i]
        else:
            left_i +=1 
            right_i -=1 
    if sum_left == sum_right:
        return True
    return False

numbers_list1 = [ 2, 4, 1, 7 ]
numbers_list2 = [ 5, 3, 1, 7 ]
numbers_list3 = [ 2, 4, 1, 3, 8 ]
print(sides_sum_equal(numbers_list1))
print(sides_sum_equal(numbers_list2))
print(sides_sum_equal(numbers_list3))

##########################################################################

# Given an array of random numbers, decide if one side's sum is equal 
# to the other's; however, the balance point is no longer between indices. 
# It's an index. If so, return the index position, else return -1. 
# Don't forget your edge cases!

#Example Input: [ 2, 4, 1, 5, 7 ]
#Example Output: 3 (2+4+1 = 7)

#Example Input: [ 5, 3, 1, 7 ]
#Example Output: None

#Example Input: [ 10, 10 ]
#Example Output: None

def sides_sum_equal_return_index(numbers_list):
    left_i = 0
    right_i = len(numbers_list)-1
    sum_left = numbers_list[left_i]
    sum_right = numbers_list[right_i]
    while left_i < right_i and left_i < len(numbers_list) and right_i > 0 :
        if sum_left < sum_right:
            left_i+= 1
            sum_left += numbers_list[left_i]
        elif sum_left > sum_right:
            right_i-=1
            sum_right += numbers_list[right_i]
        else:
            left_i +=1 
            right_i -=1 
    if sum_left == sum_right and left_i == right_i:
        return left_i
    return -1

numbers_list1 = [ 2, 4, 1, 5, 7 ]
numbers_list2 = [ 5, 3, 1, 7 ]
numbers_list3 = [ 10, 10 ]
print(sides_sum_equal_return_index(numbers_list1))
print(sides_sum_equal_return_index(numbers_list2))
print(sides_sum_equal_return_index(numbers_list3))