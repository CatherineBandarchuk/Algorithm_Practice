def binary_search(array, value):
    number_of_iterations = 0
    low = 0
    high = len(array) - 1
    while low <= high:
        number_of_iterations += 1
        mid = (low + high)//2
        if array[mid] > value:
            high = mid - 1
        elif array[mid] < value:
            low = mid + 1
        else:
            print(f" We did {number_of_iterations} iterations to find the element {value} in list.")
            return mid

        if array[low] == value:
            print(f" We did {number_of_iterations} iterations to find the element {value} in list.")
            return low
    return None

# Testing 
list_int = [1, 2, 3, 4, 5, 6, 7, 8]
sorted_list_int = sorted(list_int)
find_element = 2
print(" In sorted array : ", sorted_list_int)
print(f" Index of element {find_element}: ", binary_search(sorted_list_int, find_element))
