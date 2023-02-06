# example input 1: [[1,2], [3,4], [5,6], [7,8]]
#                  r = 2, c = 4
# expected output 1: [[1, 2, 3, 4]], [5, 6, 7, 8]]

# example input 2: [[1,2], [3,4], [5,6], [7,8]]
#                  r = 3, c = 3
# expected output 2: ErrorMessage:"Not enouph element in providing matrix to reshape."

def reshape_matrix(user_matrix, r, c):
# 1. Validate the input:
#       - Input matrix need to be not empty => return empty matrix if input matrix is empty
#       - number of raws r needs to integer and >= 0
#       - number of columns c needs to integer and >= 0
# 2. Calculate how many total elements(total_el).
# 3. Create additional result_matrix, result_row, index variables
# 4. Check if c or r == 1 => add each element to result matrix and return it
#  
# 5. Using for-loop with enumerate(user_matrix) go through matrix
#     - if index_r < r => added element to list_one_row
#     - if index_r >= r => append list_one_row to result_matrix 
    
    if not isinstance(user_matrix, list):
        raise TypeError("User matrix is not the right type")
    
    if r <= 0 or c <= 0:
        raise ValueError("New row and column parameters need to be positive integers.")
    
    user_rows = len(user_matrix)
    user_columns = len(user_matrix[0])
    total_elements = user_rows * user_columns

    result_matrix= []
    result_row = []
    index = 0

    if c == 1 or r == 1:
        while index < total_elements:
            old_r_index = index // user_columns
            old_c_index = index % user_columns
            result_matrix.append(user_matrix[old_r_index][old_c_index])
            index += 1
        return result_matrix
    
    while index < total_elements:
        new_c_index = index % c
        while new_c_index < c - 1 and index < total_elements:
            old_r_index = index // user_columns
            old_c_index = index % user_columns
            new_c_index = index % c
            result_row.append(user_matrix[old_r_index][old_c_index])
            index+= 1
        
        if len(result_row)!=0:
            result_matrix.append(result_row)
            result_row = []
    
    return result_matrix


print(reshape_matrix([[1,2], [3,4], [5,6], [7,8]], 2, 4))

print(reshape_matrix([[1,2], [3,4], [5,6], [7,8]], 3, 3))

print(reshape_matrix([[1,2], [3,4], [5,6], [7,8]], 1, 8))