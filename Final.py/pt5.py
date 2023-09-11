'''
Ex5
Exercise: 3-Dimensional List Manipulation

Create a Python exercise to work with a 3-dimensional list. 
The task is to implement a function called `sum_of_elements` that 
takes a 3-dimensional list as input and returns the sum of all the elements in the list.

Example:

# Sample 3-dimensional list
sample_list = [
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]],
    [[13, 14, 15], [16, 17, 18]]
]

# Call the sum_of_elements function with the sample_list
result = sum_of_elements(sample_list)
print(result)  # Output: 171

'''


def sum_of_elements(lst):
  # Initialize the sum variable.
  sum = 0
  # Iterate over the 3-dimensional list.
  for i in range(len(lst)):
    for j in range(len(lst[i])):
      for k in range(len(lst[i][j])):
        sum += lst[i][j][k]
  # Return the sum.
  return sum
# Sample 3-dimensional list
sample_list = [
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]],
    [[13, 14, 15], [16, 17, 18]]
]

def sum_of_elements(lst):
    total_sum = 0
    for sublist_2d in lst:
        for sublist_1d in sublist_2d:
            total_sum += sum(sublist_1d)
    return total_sum