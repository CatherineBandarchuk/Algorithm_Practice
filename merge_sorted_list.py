# Imagine working on software that processes lists of numbers. 
# Create a function named merge_lists that takes two sorted lists 
# and merges them into a single sorted list. This function 
# should take in two lists of whole numbers. 
# The function should return a new sorted list which consists 
# of the elements of the two arguments.

#   List 1	List 2	            Output
#[1, 2, 4, 5] &	[6]	  ->    [1, 2, 4, 5, 6]
#[-30, -10, 0, 15, 16]	& [-20, -5, 5]	->   [-30, -20, -10, -5, 0, 5, 15, 16]

# Check valid inputs( Both list needs to contain numbers)
#     - Raise TypeError if datatype is not integer
# Check if any or both lists empty:
#     - if one list empty return other list and exit the program
#     - if both lists empty return empty list
# Create merged_list to keep all elements of both lists in sorted way
# Create index_1 (index of elements in first list) = 0 
# Create index_2 (index of elements in second list) = 0 
# While loop until both of indexes < length of smaller list
#       Compare list1[index_1] and list2[index_2].
#       if list1[index_1] > list2[index_2]: 
#               merge_list.append(list2[index_2])
#               index2 +=1
#       if list1[index_1] < list2[index_2]: 
#               merge_list.append(list1[index_1])
#               index1 +=1
#       else: 
#               merge_list.append(list2[index_2])
#               merge_list.append(list1[index_1])
#               both_indexes +=1
# return merged_list

def merge_lists(list1, list2):
    if not all(isinstance(element, int) for element in list1) or \
        not all(isinstance(element, int) for element in list2):
        raise TypeError
    
    if len(list1) == 0 or len(list2)==0:
        return list1+list2

    merged_list = []
    index1 = 0
    index2 = 0
    while index1 < len(list1) and index2 < len(list2):
        if list1[index1] > list2[index2]:
            merged_list.append(list2[index2])
            index2 += 1
        elif list1[index1] < list2[index2]:
            merged_list.append(list1[index1])
            index1 += 1
        else:
            merged_list.append(list1[index1])
            merged_list.append(list2[index2])
            index1 += 1
            index2 += 1
    # Append extra elements 
    while index1 < len(list1):
        merged_list.append(list1[index1])
        index1 += 1
    while index2 < len(list2):
        merged_list.append(list2[index2])
        index2 += 1
    return merged_list

print(merge_lists([1, 2, 4, 5],[]))
print(merge_lists([-30, -10, 0, 15, 16], [-20, -5, 5]))
print(merge_lists([1, 2, 4, 5],[1, 2, 3, 4, 5]))
print(merge_lists([],[]))
print(merge_lists([1, 2, 4, 5],[True, '2', [4, 5]]))