# Return missing numbers in the list in the range from low to high : O(n^2)
def get_missing_numbers_in_range_with_list(numbers, low, high):
    number_present_dict = {}
    for i in range(low, high):
        if i in numbers:
            number_present_dict[i] = True
        else:
            number_present_dict[i] = False 
    
    complited_numbers = [key for key in number_present_dict if number_present_dict[key] == False]
    return complited_numbers

# Uses dictionary to increase time effitiency: O(n+m)
def get_missing_numbers_in_range(numbers, low, high):
    missing_numbers = []
    number_present_dict = {}
    
    for number in numbers:
        number_present_dict[number] = True

    for number in range(low, high):
        if not number_present_dict.get(number):
            missing_numbers.append(number)
    
    return missing_numbers
# Testing
#print(get_missing_numbers_in_range_with_list([1,2,3,5,7,10],1,10))
#print(get_missing_numbers_in_range([1,2,3,5,7,10],1,10))


def get_symetric_pairs(pairs):
    symetric_pairs = []
    pair_dict = {}
    
    for pair in pairs:
        first = pair[0]
        second = pair[1]
        pair_dict[first] = second
    
    for pair in pairs:
        first = pair[0]
        second = pair[1]
        if pair_dict.get(second) == first:
            symetric_pairs.append([first,second])
            pair_dict[first] = None
            pair_dict[second] = None

    return symetric_pairs
# Testing
#print(get_symetric_pairs([[11, 20], [30, 40], [5, 10], [40, 30], [10, 5]])) # [[30, 40], [5, 10]]

############################################################################
# Return intersecton of two list in new list
def get_intersection(first_num_list, second_num_list):
    inum_list = []
    dict_numbers_first = {}
    
    for number in first_num_list:
        dict_numbers_first[number] = True

    for number in second_num_list:
        if dict_numbers_first.get(number):
            inum_list.append(number)
    
    return inum_list
# Testing
#print(get_intersection([50, 43, 25, 72],[25, 36, 43, 50, 80]))
############################################################################
def is_permutation(string1, string2):
    dict_first = {}
    if len(string1) != len(string2):
        return False

    for letter in string1:
        if letter not in dict_first:
            dict_first[letter] = 1
        else:
            dict_first[letter] += 1

    for letter in string2:
        if not dict_first.get(letter):
            return False
        else:
            if dict_first[letter] > 1:
                dict_first[letter] -= 1
                string2 = string2.replace(letter,"")
            else:
                del dict_first[letter]
                string2 = string2.replace(letter,"")

    return True
# Testing
#print(is_permutation("hello","ehlo"))
#########################################################################
def is_palindrome_permutation(my_string):
    dict_letters = {}
    for letter in my_string:
        if letter not in dict_letters:
            dict_letters[letter] = 1
        else:
            dict_letters[letter] += 1

    have_odd_flag = 0
    for value in dict_letters.values():
        if value % 2 == 1:
            have_odd_flag += 1

    if have_odd_flag > 1:
        return False 

    return True
# Testing 
print(is_palindrome_permutation("racecac"))

##############################################################################
def calc_type_time(keyboard_list, word):
    type_time = 0
    letter_dict = {}
    for letter, index in keyboard_list:
        letter_dict[letter] = index
    
    start_index = letter_dict[word[0]]
    for letter in word:
        type_time += word
        start_index = letter_dict[letter]


## In the class ##
def typing_time(layout, word):
    typed_time = 0
    location = 0
    positions = {letter: pos for pos, letter in enumerate(layout)}
    
    for letter in word:
        next_location = positions[letter]
        typed_time +=abs(next_location - location)
        location = next_location

    return typed_time

#################################################################################

#helper function mapping the sentence:

def map_sentence(sentence):
    mapped = {}
    for word in sentence.split(" "):
        count = mapped.get(word, 0)
        mapped[word] = count + 1
    return mapped

def two_sentences(one, two):
    mapped_words = map_sentence(" ".join([one, two]))
    return [wrd for wrd,count in mapped_words.items() if count ==1]