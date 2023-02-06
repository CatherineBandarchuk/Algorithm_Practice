# Given a string with parentheses, determine if the sequence is valid. 
# Return true or false. Don't forget your edge cases!

# Example Input: "(In(The)(No(t)To)oDista)ntFuture"
# Example Output: True

# Example Input: "N(ext(Sun)da)yAD)"
# Example Output: False

def is_sequence_valid(string):
    counter = 0
    index_par_f = []
    index_par_s = []
    for index, char in enumerate(string):
        if char == '(':
            index_par_f.append(index)
            counter += 1
        elif char == ')':
            index_par_s.append(index)
            counter -= 1

    if counter == 0:
        for i in range(len(index_par_f)):
            if index_par_f[i]>index_par_s[i]:
                return False                
        return True

    return False

print(is_sequence_valid("(In(The)(No(t)To)oDista)ntFuture"))
print(is_sequence_valid("N(ext(Sun)da)yAD)"))
print(is_sequence_valid("(Satt(e(liteOfL(ove"))

#####################################################################

# Given a string with different brackets, determine if the sequence 
# is valid. Return true or false. Don't forget your edge cases!

# Example Input: "({In(The)}(No([t)To)oDista]ntFuture"
# Example Output: False

# Example Input: "N{ext([Sun]da)yAD}"
# Example Output: True

# Example Input: "(Satt]e[{lite}OfL(ove)"
# Example Output: False

def is_sequence_valid_2(string):
    braces_dict = {
        "(": ")",
        "{": "}",
        "[": "]" }

    braces_stack = []

    for char in string:
        if char in braces_dict.keys():
            braces_stack.append(char)
        elif char in braces_dict.values():
            if braces_stack and char == braces_dict[braces_stack[-1]]:
                braces_stack.pop()
    if len(braces_stack) == 0:
        return True

    return False

print(is_sequence_valid_2("N{ext([Sun]da)yAD}"))