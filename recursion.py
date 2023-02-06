def is_counter_zero(counter):
    if counter == 0:
        return True
    return False

def is_nested_parens(string, counter):
    if len(string) == 0:
        return is_counter_zero(counter)
    else:
        if string[-1] == '(':
            counter +=1
        elif string[-1] == ')':
            counter -=1
        string = string[:-1]
        return is_nested_parens(string, counter)
        
def is_nested_parens_2(string):
    if len(string) == 0:
        return True
    else:
        if string[0] == '(':
            i = string.find(')')
            if i == -1:
                return False
            string1 = string[1:i]
            string2 = string[i+1:]
            string = string1 + string2 
        elif string[0] == ')':
            i = string.find('(')
            if i == -1:
                return False
        return is_nested_parens_2(string)

string1 = "((()))"
#print(is_nested_parens_2(string1))

string2 = "()(()()))()))"
#print(is_nested_parens(string2, 0))

string3 = "(())))"
#print(is_nested_parens_2(string3))


# returns True is query in array, False - otherwise
def search(array, query):
    if len(array) == 0:
        return False
    
    if array[0] == query:
        return True
    else:
        array = array[1:]
        return search(array, query)

array = ["b", "c", "a"]
#print(search(array, "a"))


#is palindrome
def is_palindrom(text):
    if len(text) == 0 or len(text) == 1:
        return True
    if text[0] == text[-1]:
        text = text[1:-1]
        return is_palindrom(text)
    else:
        return False


# text = "racecar"
# text1 = "raecar"
# print(is_palindrom(text))
# print(is_palindrom(text1))


# def digit_match(integer1, integer2):
#     if integer1 == 0 or integer2 == 0:
#         return counter

#     if integer1 % 10 == integer2 % 10:
#         counter += 1
#     integer1 = (integer1 - integer1 % 10) / 10
#     integer2 = (integer2 - integer2 % 10) / 10
#     return digit_match(integer1, integer2)

def add_count(integer1, integer2, counter):
    if integer1 == 0 or integer2 == 0:
        return counter

    if integer1 % 10 == integer2 % 10:
        counter += 1
    integer1 = (integer1 - integer1 % 10) / 10
    integer2 = (integer2 - integer2 % 10) / 10
    return add_count(integer1, integer2, counter)


def digit_match(integer1, integer2):
    counter = 0
    if integer1 == 0 and integer2 == 0:
        return 1
    if integer1!= 0 and integer2!=0:
        counter = add_count(integer1, integer2, counter)
    return counter

integer1 = 1072503891
integer2 = 62530841
print(digit_match(integer1, integer2))
