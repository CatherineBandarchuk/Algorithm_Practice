# Imagine working on software that processes lists of numbers. 
# Create a function named pairs_with_given_sum It finds the number 
# of pairs of numbers in a list which add up to a given target. 
# This function should take in a list of whole numbers and a target 
# as parameters. This function should have a return value of the 
# integer of number of pairs.

# Pseudo code:
#- Check the valid input: all elements are int (raise TypeError if not)
#- Check if the list is empty (return 0 or massage about empty list?)
#- Sort the list
#- Create variable counter = 0
#- Use two pointer start_i = 0 and end_i = len(list)-1
#   to check if sum list[start_i] + list[end_i] = 100
#          * if sum == giver_target : start_i += 1 and end_i -=1 and counter +=0
#          * if sum > given_target : start_i = stay_the same and end_i -=1,  
#          * if sum < given_target: start_i +=1 and end_i = stay_the_same
#- Return counter

def pairs_with_given_sum(list_n, target):
    
    if not all(isinstance(item, int) for item in list_n):
        raise TypeError("The elements in the list are not integers")
    if not isinstance(target, int):
        raise TypeError("The targeted sum is integers")
    if not list_n:
        return 0 # return "Empty list!"
    
    list_of_numbers = sorted(list_n)    # Space complexity O(n)

    counter = 0
    start_i = 0
    end_i = len(list_of_numbers)-1
    while start_i != end_i:
        sum = list_of_numbers[start_i] + list_of_numbers[end_i]
        if sum == target:
            counter +=1
            start_i +1
            end_i -=1
        elif sum > target:
            end_i -=1
        else:
            start_i +=1
    
    return counter                      # Time complexity O(n + n/2) ~ O(n)

# Testing

target = 100
input1 = [34, 26, 50, 90, 67, 1, 74, 10, 50, 33, 66, 99] # result 6
input2 = [34, -15, 26, 50, 100, 67, 1, 0, 74, 10, 115, 33, 66, 99] # result 6
input3 = []  # result 0
input4 = [97, 51, 49, 35, 3, 65]  # result 3
input5 = ['g', 0, 0,'d'] # Raised TypeError 
input6 = [1, 1, 34, -15, 26, 50, 100, 67, 1, 0, 74, 10, 115, 33, 66, 66, 99] # result 7

print(pairs_with_given_sum(input1, target))
print(pairs_with_given_sum(input2, target))
print(pairs_with_given_sum(input3, target))
print(pairs_with_given_sum(input4, target))
#print(pairs_with_given_sum(input5, target))
print(pairs_with_given_sum(input6, target))