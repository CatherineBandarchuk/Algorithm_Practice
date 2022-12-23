#From 0 to and including 300, print out any numbers that are multiples of of 3; 
# however, don't print numbers 10, 15, and 21 even if they are.
#What if a user wanted to choose the multiple herself instead of 
# always using 3? How would you change your code?

def printing_numbers(start, end, multiple):
    if not isinstance(start, int) or not isinstance( end, int) or not isinstance( multiple, int):
        raise TypeError 
    
    if start > end:
        raise Exception("Starting number needs to be less the last number.") 
    
    if multiple == 0:
        raise ZeroDivisionError

    exception_list = [10, 15, 21]
    for i in range( start, end+1):
        if i not in exception_list and i % multiple == 0:
            print(i)

# Testing
#printing_numbers(start = 0, end = 300, multiple = 3)

#####################################################################################

# Crow T. Robot needs a way to count how many clusters of tally marks he has. 
# Create a function for him that takes in the number of "tallies" and prints 
# the number of clusters (a grouping of 5 tallies), as well as any remainder.
# Example Input: 23
# Example Output: "4 clusters and a remainder of 3 tallies"

def tally_mark_counter(tallies):
    if not isinstance(tallies, int):
        raise TypeError 
    
    if tallies <= 0:
        raise Exception("Please enter positive number bigger then 0.") 

    cluster = tallies // 5
    remainder = tallies % 5

    if remainder == 0:
        print(f"{cluster} clusters")
    elif cluster == 0:
        print(f"{remainder} tallies")
    else:
        print(f"{cluster} clusters and a remainder of {remainder} tallies")

# Testing
#tally_mark_counter(51)

###################################################################################
# You work for a company that sells a countdown clock, but customers are asking 
# for a few additional features and flexibility. Your manager asks you to create 
# a function that would let a customer decide what number the countdown starts at, 
# printing out each number as it counts down.
#
# But customers also want to select what number to increment the countdown by. 
# Then when it hits 0, customers wish the clock to alert them that, "TIME'S UP!"
#
# Example Input: start=5, increment=2
# Example Output:   5
#		        	3
#	    		    1
#   			    TIME'S UP

def countdown_clock(start_timer, step):
    
    if not isinstance(start_timer, int) or not isinstance(step, int):
        raise TypeError 
    if start_timer<=0:
        raise Exception("Please enter positive number bigger then 0 for start point( Timer).") 
    if step <=0:
        raise Exception("Please enter positive increment number bigger then 0.") 
    if step > start_timer:
        raise Exception("Please enter increment number less then start point( Timer).") 
    
    current_time = start_timer
    while current_time > 0:
        print(current_time)
        current_time -= step
    print("TIME'S UP")

# Testing 
countdown_clock (start_timer = 790, step = 12)
#####################################################################################
