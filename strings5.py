# Given an array of sorted page numbers, return a string of the page ranges. 
# Any consecutive numbers should be hyphenated. Don't forget your edge cases!

# Example Input: [1,3,5,6,7,9,10,12]
# Example Output: "1, 3, 5-7, 9-10, 12"

def page_ranges(pages_list):
    pages_string = ""
    index = 0
    while index < len(pages_list)-1:
        start_index = index
        current_index = index
        end_index = index+1
        while pages_list[end_index] - pages_list[current_index] == 1:
            current_index += 1
            end_index += 1
        if end_index-start_index>1:
            pages_string += str(pages_list[start_index]) + '-' + str(pages_list[current_index]) + ','
        else: 
            pages_string += str(pages_list[current_index]) + ','
        index = end_index
    pages_string += str(pages_list[len(pages_list)-1])
    return pages_string

#pages_list1 = [1,3,5,6,7,9,10,12]
#print(page_ranges(pages_list1))

############################################################################

# Given two arrays, return a dictionary using the first array as keys 
# and the second array as the values. Don't forget your edge cases!

# Example Input: 
# [ "name", 222, "moon" ], [ False, "abc", 123 ]
# Example Output: 
# {"name": False, 222: "abc", "moon": 123 }

# Example Input: 
# [ "name", 222, "moon" ], [ "abc", 123 ]
# Example Output: 
# {"name": "abc", 222: 123, "moon": None }

# Example Input: 
# [ "name", 222 ], [ False, "abc", 123 ]
# Example Output: 
# None

def arrays_to_dict(array1, array2):
    result_dict = {}
    if len(array1) < len(array2):
        return None
    elif len(array1)== len(array2):
        for index in range(len(array1)):
            result_dict[array1[index]] = array2[index]
    else:
        index = 0
        while index < len(array2):
            result_dict[array1[index]] = array2[index]
            index += 1
        while index < len(array1):
            result_dict[array1[index]] = None
            index += 1

    return result_dict

# array1 = [ "name", 222, "moon" ]
# array2 = [ False, "abc", 123 ]
# print(arrays_to_dict(array1, array2))
# array3 = [ "name", 222, "moon" ]
# array4 = [ "abc", 123 ]
# print(arrays_to_dict(array3, array4))
# array5 = [ "name", 222 ]
# array6 = [ False, "abc", 123 ]
# print(arrays_to_dict(array5, array6))
##############################################################################

# Given a dictionary, reverse the values and keys and return a new dictionary. 
# Don't forget your edge cases!

# Example Input: 
# {"name": False, 222: "abc", "moon": 123 }
# Example Output: 
# {False: "name", "abc": 222, 123: "moon" }

# def reverse_dict(input_dict):
#     for key, value in input_dict.items():
#         temp_key = key
#         key, value = value, key
#         input_dict[key] = value
#         input_dict.pop(temp_key)
#     return input_dict

def reverse_dict(input_dict):
    for key in list(input_dict.keys()):
        value = input_dict.pop(key)
        input_dict[value] = key
    return input_dict

def reverse_dict1(input_dict):
    return {value: key for key, value in input_dict.items()}

print(reverse_dict1({"name": False, 222: "abc", "moon": 123 }))
