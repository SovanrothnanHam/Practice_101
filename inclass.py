# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]

# ]
# print(matrix[0][2])

# ex1
# The function `find_element` takes two arguments: a matrix and a target value. 
# The function iterates over the rows and columns of the matrix, 
# and if the target value is found, the function returns the row and column indices of the target value. 
# If the target value is not found, the function returns `None`.
def find_element(matrix, target):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == target:
                return (i, j)
    return None
matrix =[
    [1,2,3],
    [4,5,6],
    [7,8,9]
    
]

target = 9
result=find_element(matrix, target )   #calling the function with arguments.
print (result)
target = 5
result=find_element(matrix, target )   #calling the function with arguments.
print (result)
# Explain ex1
# 1. The function first iterates through the rows of the matrix.
# 2. For each row, the function iterates through the columns of the row.
# 3. If the element at the current row and column is equal to the target, the function returns a tuple containing the indices of the element.
# 4. If the target is not found in the matrix, the function returns `None`.

# ex2
def matrix_transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]
    return result
matrix =[
    [1,2,3],
    [4,5,6],
    [7,8,9]
    
]
new_matrix = matrix_transpose(matrix)
for n in new_matrix:
    print (n)
# 1. We first get the number of rows and columns in the matrix.
# 2. We create a new matrix with the same number of columns and rows as the original matrix.
# 3. We iterate over each element in the original matrix and set the corresponding element in the new matrix to the transposed element.
# 4. We return the transposed matrix.
