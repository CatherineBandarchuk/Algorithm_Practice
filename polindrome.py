# example inputs:
input1 = "Cigar? Toss it in a can. It is so tragic." # polindrome with punctuation
input2 = "taco cat" # polindrome with spaces
input3 = "Racecar" # polindrome with uppercase letter
input4 = "NotPolindrome" # not polimdrom
input5 = "level" # easy polindrome
input6 = "Defenetly not a polindrome!" # not-polindrome with space, Upercase letter and Punctuation

# expected outputs:
output1 = True
output2 = True
output3 = True
output4 = False
output5 = True
output6 = False

# version 1
def palindrome(s):
    if not isinstance(s, str):
        raise TypeError("It is not string!")
    if len(s) == 0:
        raise Exception("The string is empty!")
    
    working_str = ""
    for char in s:
        if char.isalpha():
            working_str += char
    working_str = working_str.lower()
    
    for i in range(len(working_str)//2):
        if working_str[i]!= working_str[-i-1]:
            return False
    
    return True

# version 2    
def palindrome_2(s):
    
    if not isinstance(s, str):
        raise TypeError("It is not string!")
    if len(s) == 0:
        raise Exception("The string is empty!")
    
    s = ''.join(filter(str.isalpha, s))
    s = s.lower()

# Implementation 1 - better for runtime, but it worse for memory efficiency s[::1] does create a copy of a string
#    if s == s[::-1]:
#        return True

# Implementation 2 - reversed does not copy the string, it iterates in reverse. But it's slower.
    if s == "".join(reversed(s)):
        return True
    return False


print(palindrome(input1))
print(palindrome_2(input1))
print(palindrome(input2))
print(palindrome_2(input2))
print(palindrome(input3))
print(palindrome_2(input3))
print(palindrome(input4))
print(palindrome_2(input4))
print(palindrome(input5))
print(palindrome_2(input5))
print(palindrome(input6))
print(palindrome_2(input6))