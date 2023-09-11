# Final Exam
# 1. Write a Python program to print the multiplication table of a given number using nested loops.
# take input from user
# num = int(input("Enter a number: "))
#  loop through each number from 1 to 10
# for i in range(1, 11):
#     # print the multiplication table of the given number
#     print(num, "x", i, "=", num*i)

# 2. Write a Python function to find the largest number in a given list using loops.
# def find_largest_number(numbers):
    # initialize the largest number to the first number in the list
    # largest_num = numbers[0]
    # loop through each number in the list
    # for num in numbers:
        # if the current number is greater than the largest number, update the largest number
        # if num > largest_num:
            # largest_num = num
    # return largest_num
# Example Usage
# numbers =[1, 2, 3, 4, 5]
# print(find_largest_number(numbers))

# 3.Write a Python function to reverse a given string using loops.
# def reverse_string(string):
    # initialize an empty string to store the reversed string
    # reversed_string = ""
    # loop through each character in the string in reverse order
    # for i in range(len(string)-1, -1, -1):
        # reversed_string += string[i]
    # return reversed_string
# Example Usage
# string = "bananpw"
# print(reverse_string(string))

# 4. Write a Python function to calculate the sum of all elements in a 2D list.
# def sum_2d_list(lst):
    # initialize the sum to zero
    # total = 0
    # loop through each row in the list
    # for row in lst:
        # loop through each element in the row
        # for elem in row:
            # add the element to the total
            # total += elem
    # return total
# Example usage
# lst = [
    # [1,2,3],
    # [4,5,6]
# ]
# print(sum_2d_list(lst))

# 5. Create a Python class representing a stack data structure with push, pop, and isEmpty methods.
# class Stack:
#     def __init__(self):
#         self.stack = []
#     def push(self, item):
#         self.stack.append(item)
#     def pop(self):
#         if not self.isEmpty():
#             return self.stack.pop()
#     def isEmpty(self):
#         return len(self.stack) == 0
# Example usage  
# stack = Stack()
# stack.push(5)
# stack.push(10)
# print(stack.pop())
# print(stack.isEmpty())

# 6. Write a Python function to check if a given string is a palindrome (reads the same forwards and backwards).
# def is_palindrome(string):
     # convert the string to lowercase
#     string = string.lower()
    # initialize two pointers, one at the beginning and one at the end of the string
#     left = 0
#     right = len(string) - 1
    # loop through the string while the pointers are not pointing to the same position
#     while left < right:
    # if the characters at the left and right pointers are not equal, the string is not a palindrome
#         if string[left] != string[right]:
#             return False
    # move the left pointer one position to the right and the right pointer one position to the left
#         left += 1
#         right -= 1
    # if the loop completes without returning False, the string is a palindrome
#     return True
# Example usage
# string = "nadan"
# print(is_palindrome(string))

# 7. Write a Python function to find all prime numbers within a given range.
# def find_primes(start, end):
    # initialize an empty list to store the prime numbers
    # primes = []
    # loop through each number in the range
    # for num in range(start, end+1):
        # check if the number is prime
        # is_prime = True
        # for i in range(2, int(num**0.5)+1):
            # if num % i == 0:
                # is_prime = False
                # break
        # if the number is prime, add it to the list of primes
        # if is_prime:
            # primes.append(num)
    # return primes
# Example usage 
# start = 2
# end = 22
# print(find_primes(start, end))

# 8. Write a Python function to generate the Fibonacci sequence up to a given number.
# def fibonacci_sequence(n):
#     fib_sequence = [0, 1]
#     for i in range(2, n):
#         fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
#     return fib_sequence
#  Example usage
# n = 10
# print(fibonacci_sequence(n))

# 9. Write a Python function that takes two lists as input and returns a new list containing common elements between the two lists
# def get_common_elements(list1, list2):
#     # Create a set of the elements in list1.
#     common_elements = set(list1)
#     # Intersect the set of elements in list1 with the set of elements in list2.
#     common_elements = common_elements.intersection(list2)
#     # Convert the set of common elements to a list.
#     common_elements = list(common_elements)
#     return common_elements
# Example usage
# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 6, 7, 8]
# common_elements = get_common_elements(list1, list2)
# print(common_elements)

# 10. Create a Python class representing a Tic-Tac-Toe game. Implement methods to check for a win, make a move, and display the board.
# class TicTacToe:
#     def __init__(self):
#         self.board = [[' ' for _ in range(3)] for _ in range(3)]

#     def check_win(self):
#         for i in range(3):
#             if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
#                 return self.board[i][0]
#             if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
#                 return self.board[0][i]
#         if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
#             return self.board[0][0]
#         if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
#             return self.board[0][2]
#         return None
#     def make_move(self, row, col, player):
#         self.board[row][col] = player

#     def display_board(self):
#         for row in self.board:
#             print(' '.join(row))
# Example usage
#ttt = TicTacToe()
#ttt.make_move(0, 0, 'X')
#ttt.make_move(1, 1, 'O')
#ttt.make_move(2, 2, 'X')
#print(ttt.check_win())
#ttt.display_board()
