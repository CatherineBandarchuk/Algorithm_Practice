# Given a number and another number that represents a digit's place, create a function that 
# isolates the value of the number at a specific place and returns it.

# 0 represents the ones place, 1 represents tens place, 2 represents the hundreds place, etc

# Example Input: 44154, 2       Example Output: 1
# Example Input: 251, 5         Example Output: None

def float_to_int(number, place):
    number_l = str(number).split('.')
    decimal_digits = len(number_l[1])
    new_place = place + decimal_digits
    new_number = int(number * ( 10**decimal_digits ))
    return new_number, new_place

def take_number_by_place(number, place):
    result = None
    if not isinstance(place, int):
        raise TypeError("Position of the digit needs to be integer.")
    if place < len(str(number)):
        if isinstance(number, int):
            if place >= 0:
                divider = 10**place
                result = (number // divider) % 10
            else:
                return None
        elif isinstance(number, float):
            number, place = float_to_int(number, place)
            divider = 10**place
            result = (number // divider) % 10
    return result

# Testing
#number1 = 44154
#place1 = 2    # result = 1
#print(f"The digit of {number1} in {place1} place = {take_number_by_place(number1, place1)}")
#number2 = 251
#place2 = 5    # result = None
#print(f"The digit of {number2} in {place2} place = {take_number_by_place(number2, place2)}")
#number3 = 567830.964
#place3 = 2    # result = 8
#print(f"The digit of {number3} in {place3} place = {take_number_by_place(number3, place3)}")
#number4 = 567830
#place4 =  - 2    # result = None
#print(f"The digit of {number4} in {place4} place = {take_number_by_place(number4, place4)}")
#number5 = 567830.964
#place5 = - 2    # result = 6
#print(f"The digit of {number5} in {place5} place = {take_number_by_place(number5, place5)}")
#number6 = 567839
#place6 = 0    # result = 9
#print(f"The digit of {number6} in {place6} place = {take_number_by_place(number6, place6)}")
#number7 = 567830.964
#place7 = 0    # result = 0
#print(f"The digit of {number7} in {place7} place = {take_number_by_place(number7, place7)}")

################################################################################

# GPC is the robot responsible for running her team's spaceship. She needs a way 
# to log her every movement on the ship, so that her teammates can find her using 
# a few simple computer functions.

#    - Starting at homebase [0,0] every morning, she logs her movements by 
#   increasing/decreasing her x and y coordinates by calling the function move_by(x,y)
#    - Every night before she powers off, she resets her location coordinates 
#   to [0,0] with the function reset()
#    - If a teammate wants to find her, they can use the functions y_location() 
#   and x_location() to find her current x and y coordinates
#           * Some of her teammates complain that calling two functions is a pain. 
#             How could GPC use these two functions to create a more user-friendly 
#             readout?


x_global = 0
y_global = 0

def move_by( x, y):
    global x_global
    global y_global
    x_global += x
    y_global += y

def y_location():
    global y_global
    return y_global

def x_location():
    global x_global
    return x_global

def location():
    global x_global
    global y_global
    return x_global, y_global

def reset():
    global x_global
    global y_global
    x_global = 0
    y_global = 0

# Testing
print(f"Starting x: {x_global} y: {y_global}")
move_by(-2,4)
move_by(0,2)
print(y_location()) # -> 6
print(x_location()) # -> -2
move_by(4,6)
print("New location: ", location()) # -> 2 , 12
reset()
print(f"Reseted x: {x_global} y: {y_global}")
#####################################################

