# Tom Servo's been collecting pennies for years, but he's running out of 
# space in his room! Create a function for him that will turn his pennies 
# into the smallest number of coins. Think quarters, dimes, nickels, pennies. 
#
# Example Input: 174
# Example Output: 
# "Quarters: 6
# Dimes: 2
# Pennies: 4"

def pennies_to_bigger_coins(number_of_pennies):
    if not isinstance(number_of_pennies, int):
        raise TypeError("You can choose integer.")
    if number_of_pennies <= 0:
        raise Exception(f"You don't have pennies. I can't turn it into smaller amount of coins. It is : {number_of_pennies}")
    coins_dictionary = {
                        "Quarters" : 0,
                        "Dimes" : 0,
                        "Nickels" : 0,
                        "Pennies" : 0 
    }
    coins_dictionary["Quarters"] = number_of_pennies // 25
    rest_of_coins = number_of_pennies % 25
    coins_dictionary["Dimes"] = rest_of_coins // 10
    rest_of_coins = rest_of_coins % 10
    coins_dictionary["Nickels"] = rest_of_coins // 5
    rest_of_coins = rest_of_coins % 5
    coins_dictionary["Pennies"] = rest_of_coins

    return coins_dictionary

# Testing
# print( pennies_to_bigger_coins(174))
# print( pennies_to_bigger_coins(0))
# print( pennies_to_bigger_coins(-100))
# print( pennies_to_bigger_coins("o"))

##############################################################################

# Given a number, continuously sum that number until it is one digit.
#Example Input: 477
#Example Output: 9
#
#Example Input: 246
#Example Output: 3

def sum_of_digits(number):
    if not isinstance(number, int):
        raise TypeError("You can choose integer.")
    if number == 0:
        return 0
    if number < 0:
        number = abs(number)
    while len(str(number)) > 1:
        sum = 0
        for i in range(len(str(abs(number)))):
            result = number % 10
            sum += result 
            number = number // 10
        number = sum
    return sum

# Testing 
#print(sum_of_digits(134)) # 8
#print(sum_of_digits(477)) # 9
#print(sum_of_digits(-257)) # 5
#print(sum_of_digits(0)) # 0
#print(sum_of_digits("rty")) # TypeError

##############################################################################

# You work for a company that makes retro terminal games. Your job is to create
# title cards with text, spaces, and stars, like so:

#******************************
#||         WELCOME          ||
#******************************

# Given a "title" (a string), center it in the title card! There's some 
# limitations, though. You only have 75 characters per line. What happens if 
# the title is longer than 75? Well, get creative!

def title_card_creater(title):
    if not isinstance(title, str):
        title = str(title)
    
    print("*"*75)

    if len(title) > 70:
######### Implementation with spliting by sentences and words (if sentence too long)###################        
        title_list = title.split(".")
        for sentence in title_list:
            if len(sentence) < 70:
                white_spaces_left = (71 - len(sentence))//2
                white_spaces_right = (71 - len(sentence)) - white_spaces_left 
                spaces_left_message = " " * white_spaces_left
                spaces_right_message = " " * white_spaces_right
                print(f"||{spaces_left_message}{sentence}{spaces_right_message}||")
            else:
                word_list = sentence.split(" ")
                i = 0
                while i < len(word_list):
                    string = ""
                    while len(string) < 70 and i < len(word_list):
                        if len(word_list[i]) < 70 - len(string):
                            string +=word_list[i] + ' '
                        else:    
                            break
                        i+= 1
                    white_spaces_left = (71 - len(string))//2
                    white_spaces_right = (71 - len(string)) - white_spaces_left 
                    spaces_left_message = " " * white_spaces_left
                    spaces_right_message = " " * white_spaces_right
                    print(f"||{spaces_left_message}{string}{spaces_right_message}||")
        print("*"*75)
    else:
        white_spaces_left = (71 - len(title))//2
        white_spaces_right = (71 - len(title)) - white_spaces_left 
        spaces_left_message = " " * white_spaces_left
        spaces_right_message = " " * white_spaces_right
        print(f"||{spaces_left_message}{title}{spaces_right_message}||")
        print("*"*75)

# Testing 

title1 = "Hello World!"
title2 = ""
title3 = 123
title4 = "It is a great long title for the wonderful game. I can write about it for a long long long long long long long long long long long long long long long time of period!"
title_card_creater(title1)
title_card_creater(title2)
title_card_creater(title3)
title_card_creater(title4)

