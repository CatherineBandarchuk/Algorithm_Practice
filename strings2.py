# Given a string, reverse it, and return a new string. 
# Do not use the built-in function reverse.  Don't forget your edge cases!

# Example Input: "pineapple"  Example Output: "elppaenip"
# Extra Challenge
# Remember, string concatenation is O(n^2). 
# Do some research and find a way to make it more efficient.

def reverse_string(my_string):
    if not my_string or not isinstance(my_string, str):
        return None

    string_list = list(my_string)
    last_letter_index = len(my_string)-1

    for letter_index in range(last_letter_index//2):
        string_list[letter_index], string_list[last_letter_index - letter_index] = \
            string_list[last_letter_index - letter_index], string_list[letter_index]
    
    return ''.join(string_list)
#Testing#
string1 = "pineapple"
#print(f"Input: {string1} Output: {reverse_string(string1)}")

##########################################################################
# Given an array of strings, remove any strings that are of equal length, 
# and return the original array. Work in-place. Don't forget your edge cases!
# Feel free to use remove since we've built something similar in the past.

# Example Input: [ "Somewhere", "in", "time", "and", "space" ]
# Example Output: [ "Somewhere", "in", "time", "and", "space" ]

# Example Input: [ "Hot", "blooded", "check", "it", "and", "see" ]
# Example Output: [ "blooded", "check", "it"]

# implement with dictionary
def remove_duplicates(word_list):
    if not isinstance(word_list, list) \
        or not all(isinstance(element, str) for element in word_list)\
        or not word_list:
        return []

    word_dict = {}
    new_word_list = []
    for element in word_list:
        if len(element) not in word_dict.keys():
            word_dict[len(element)] = [element]
        else:
            word_dict[len(element)].append(element)
    itterator = 0
    len_of_dict = len(word_dict)
    while itterator < len_of_dict:
        item = word_dict.popitem()
        itterator += 1
        if len(item[1]) == 1:
            new_word_list.insert(0, item[1])
    return new_word_list

print(remove_duplicates(["Somewhere", "in", "time", "and", "space"]))
print(remove_duplicates(["Hot", "blooded", "check", "it", "and", "see"]))
print(remove_duplicates([]))
print(remove_duplicates([True, "in", "time", "and", "space"]))