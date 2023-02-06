# Given a string with capital letters, punctuation and spaces, 
# determine if the sequence is a palindrome. Return true or false. 
# Don't forget your edge cases!

# Example Input: "bl o lb"
# Example Output: True

# Example Input: "Hey ,sis, yeh"
# Example Output: False

# Example Input: "RacecaR"
# Example Output: True

# Do not store a new copy of the string. Try to do this with O(1) space complexity

def polindrom(input_string):
    last_index = len(input_string)-1
    for index in range((last_index+1)//2):
        if input_string[index] != input_string[last_index - index]:
            return False
    return True

#print(polindrom("RacecaR"))
print(polindrom("helloh"))
################################################################################
# Given a string with capital letters, punctuation and spaces, 
# return the longest palindrome sequence. Don't forget your edge cases!

# Example Input: "Hey ,sis, yeh"
# Example Output: "ey, sis, ye"

# Example Input: "racecars are great!"
# Example Output: "racecar"

# Example Input: "summer love"
# Example Output: "mm"

def max_polindrom(input_string):
    result = ""
    
    if len(input_string) == 1:
        return input_string
    
    max_len = 1
    for start_i in range(len(input_string)-1):
        for end_i in range(start_i+1, len(input_string)):
            substring = input_string[start_i:end_i]
            if polindrom(substring) and len(substring) > max_len:
                max_len = len(substring)
                result = substring
    return result

print(max_polindrom("Hey ,sis, yeh"))
print(max_polindrom("racecars are great!"))
print(max_polindrom("summer love"))