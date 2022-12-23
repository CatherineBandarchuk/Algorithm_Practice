# Create a function that will tell you whether or not a year is 
# a leap year! How can you tell? Well, if a year is divisible by 4, 
# then it's a leap year. But if it is also divisible by 100, 
# then it's not a leap year. Oh unless you are talking about being 
# divisible by 400, then it's a leap year again.

# Example Input: 1976
# Example Output: True

# Example Input: 2014
# Example output: False

def isLeapYear(year):
    if not isinstance( year, int):
        raise TypeError 
    if year <= 0:
        raise Exception("Please enter positive number bigger then 0 for year.") 
    
    if ( year % 400 == 0) or ( year % 4 ==0 and year % 100!= 0):
        return True
    else:
        return False

# Testing 
#print(isLeapYear(44))

###############################################################################
#A friend needs a function that will help them count the number of 
# values in an array/list greater than the third element.

#For every value in the array/list that is greater, print that number also. 
# Finally, return the number of values greater than.

#Example Input: [6,4,5,2,3,7,10,2]
#Examples Output: 6
#   			  7
#			      10
#			      3

def counter_bigger_third_element(list_of_numbers, element):
    if list_of_numbers == None:
        raise Exception("The list is empty!")
    if not all(isinstance(x, int) for x in list_of_numbers):
        raise TypeError
    max_index = len(list_of_numbers) - 1
    if element <= 0 or element > max_index-1:
        raise Exception(f"Please choose index from 0 to {max_index}")

    counter = 0
    the_element = list_of_numbers[element-1]
    for number in list_of_numbers:
        if number > the_element:
            counter += 1
            print(number)
    return counter

# Testing

#number_list1 = [6,4,5,2,3,7,10,2]
#element = 3
#element = -1
#element = 1
#number_list2 = [0,-5,-8, 9,4,2,-11]
#number_list3 = []
#number_list4 = ['g',9,0,5,'m']
#print(f"{counter_bigger_third_element(number_list1, element)} elements bigger then {number_list1[element-1]}.")
#print(f"{counter_bigger_third_element(number_list2, element)} elements bigger then {number_list2[element-1]}.")
#print(f"{counter_bigger_third_element(number_list3, element)} elements bigger then {number_list3[element-1]}.")
#print(f"{counter_bigger_third_element(number_list4, element)} elements bigger then {number_list4[element-1]}.")

################################################################################
# Oh dear! Someone at your company messed up the temperature converter app you 
# all sell. Your manager comes to you to fix it. You need to create a function 
# that correctly converts Celsius to Fahrenheit, and then returns the new 
# temperature.

#Chemistry has been a while for a lot of us, so let's review that formula:
#	fahrenheit = (9/5  * celsius) + 32

#Example Input: 30
#Example Output: 86

# Extra Challenge: How would you convert from Fahrenheit to Celsius then? 
# What if the customer wants to choose from which system to convert to?

def temperature_converter(convert_choice, temperature):
    if not isinstance(temperature, int):
        raise TypeError
    if convert_choice == 1:
        new_temperature = 9/5 * temperature + 32
    elif convert_choice == 2:
        new_temperature = temperature * 5/9 - 32
    else:
        raise Exception("Please choose:\n 1 - convert fahrenheit to celsius\n 2 - convert celsius to fahrenheit.") 
    return new_temperature

# Testing
#choice1 = 1
#choice2 = 2
#choice3 = "a"
#choice4 = 0 
#print(f"{temperature_converter(choice1, 30):.2f}")
#print(f"{temperature_converter(choice2, 28):.2f}")
#print(f"{temperature_converter(choice3, 30):.2f}")
#print(f"{temperature_converter(choice4, 5):.2f}")
#print(temperature_converter(choice1, "35"))