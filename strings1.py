import string
import re
# Given a sentence, return a new string that removes 
# all blanks in a sentence. Don't forget your edge cases!

#Example Input: " In     Th    eNo  tToo   Dist  an   tFu   tu  re"
#Example Output: "InTheNotTooDistantFuture"

#Example Input: " "
#Example Output: " "

def remove_blanks(string1):
    if not string1 or not isinstance(string1, str): return ""
    #string1 = string1.replace(" ", "")
    #string1 = "".join(string1.split())
    string1 = re.sub(r"\s+", "", string1)
    return string1

# Testing
input1 = "In     Th    eNo  tToo   Dist  an   tFu   tu  re"
print(f"Input: {input1} \nOutput: {remove_blanks(input1)}")
input2 = ""
print(f"Input: {input2} \nOutput: {remove_blanks(input2)}")
input3 = [1,3,5]
print(f"Input: {input3} \nOutput: {remove_blanks(input3)}")

################################################################

# Given a sentence, return a new string that turns the sentence 
# into an acronym. Don't forget your edge cases!

#Example Input: "Somewhere in time and space"
#Example Output: "SITAS"

#Example Input: "Hot blooded, check it and see"
#Example Output: "HBCIAS"

def StringToAcronym(string1):
    if not string1 or not isinstance(string1, str): return ""
    acronym = ""
    words_list= string1.split(' ')
    for word in words_list:
        acronym += word[0].upper()
    return acronym

print(StringToAcronym("Somewhere in time and space"))
print(StringToAcronym(""))
print(StringToAcronym("Hot blooded, check it and see"))
print(StringToAcronym(12345))

###################################################################
# Given a string, return an integer value of the numeric characters 
# from the string. Don't forget your edge cases!

# Example Input: "0?3af4([4m5HW7"
# Example Output: 34457

# Example Input: "abdfg[Bwk!f?"
# Example Output: None

def get_numbers_in_string(string1):
    if not string1 or not isinstance(string1, str): return None
    number_str = ""
    for letter in string1:
        if letter.isdigit():
            number_str += letter
    if not number_str:
        return None    
    return int(number_str)

print(get_numbers_in_string("0?3af4([4m5HW7"))
print(get_numbers_in_string("abdfg[Bwk!f?"))