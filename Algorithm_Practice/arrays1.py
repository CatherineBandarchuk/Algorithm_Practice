# Given an array, swap every pair of successive values 
# and return the array. Don't forget your edge cases!

# Example Input: [1, 2, 3, 4, 5, 6]
# Example Output: [2, 1, 4, 3, 6, 5]

# Example Input: [True, "a", 1]
# Example Output: ["a", True, 1]

def swap_pair_in_array(list):
    if len(list) % 2 == 0:
        max_idex = len(list)-1
    else:
        max_idex = len(list)-2
    index = 0
    
    while index < max_idex:
        temp = list[index]
        list[index] = list[index+1]
        list[index+1] = temp
        index += 2
    
    return list


# Testing 
list1 = [1, 2, 3, 4, 5, 6]
#print(swap_pair_in_array(list1))
list2 = []
#print(swap_pair_in_array(list2))
list3 = [True, "a", 1]
#print(swap_pair_in_array(list3))
list4 = [1, 2, 3, 4, -7, 9, -30, 0, 4.7]
#print(swap_pair_in_array(list4))

#########################################################################

# Someone accidentally duplicated the data found in an array. 
# We need you to remove all duplicate values in a sorted array, 
# then return the array. Don't forget your edge cases! 
# TRY TO MODIFY THE ORIGINAL ARRAY

# Example Input: [1, 2, 2, 3, 5, 6, 6, 6, 8]
# Example Output: [1, 2, 3, 5, 6, 8]

# Extra Challenge

# Example Input: ["a", "a", "b", "c", "c", "c", "d", "d"]
# Example output: ["a", "b", "c", "d"]

def remove_duplicates_in_sorted_array(list):
    # we can use return [*set(list)] but it is not fun ;)
    # if we allowed to sort the list 
    # it work only for one-type data list 
    # space&time complexity = O(n)
    list = sorted(list)
    index = 0
    while index < len(list)-1:
        following_index = index+1
        if list[index] == list[following_index]:
            del list[index]
        else:
            index = following_index 
    return list

def remove_duplicates_in_array(list):
# if we need to return list in the same order
# spacecomplexity = O(n) & time complexity = O(n^2)
    index1 = 0 
    while index1< len(list) - 1:
        index2 = index1 + 1
        while index2 < len(list):
            if list[index1] == list[index2]:
                del list[index2]
            else:
                index2 += 1
        index1 += 1
    return list 
    

# Testing
list1 = ["a", "a", "b", "c", "c", "c", "d", "d"]
list2 = [1, 2, 2, 3, 5, 6, 6, 6, 8]
list3 = [1, 8, 6, 7, 4, 5, 6, 7, 2, 1, 9, 8, 7, 8, 7]
list4 = ["a", 2, "a", 1, "b", "c", "c", 1, "b", "c", 1, 2]
list5 = []
print(remove_duplicates_in_sorted_array(list1))
print(remove_duplicates_in_sorted_array(list2))
print(remove_duplicates_in_sorted_array(list3))
# list4 can't use this function because it contain mixed data type (int,str) 
print(remove_duplicates_in_sorted_array(list5))

print(remove_duplicates_in_array(list1))
print(remove_duplicates_in_array(list2))
print(remove_duplicates_in_array(list3))
print(remove_duplicates_in_array(list4))
print(remove_duplicates_in_array(list5))