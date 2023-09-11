'''
1.Instruction
-----------
You are given list of integers (int). Your task in this mission is to duplicate (..., 🍩, ... --> ..., 🍩, 🍩, ...) 
all zeros (think about donuts ;-P) and return the result as any Iterable. Let's look on the example:

[1, 0, 2, 0] -> [1, 0, 0, 2, 0, 0]

1pt
'''
numbers = [1, 0, 2, 0]


def duplicate_zeros(numbers):
    temp_list = []
    for num in numbers:
        if num == 0:
            temp_list.append(num)
            temp_list.append(0)
        else:
            temp_list.append(num)
    return temp_list
    ...

'''
2.Instruction
-----------
You are given a non-empty sequence of integers. For this task, you should return Iterable consisting of only the non-unique elements from the initial sequence. 
To do so you will need to remove all unique elements (elements which are contained in a given sequence only once). 
When solving this task, do not change the order of the elements. 

Example: in [1, 2, 3, 1, 3] elements 1, 3 are non-unique and result will be [1, 3, 1, 3].

1pt
'''


numbers = [1, 2, 3, 1, 3]

def checkio(numbers):
    temp_list = []
    for num in numbers:
        if numbers.count(num)>=2:
            temp_list.append(num)
    

    return temp_list
    ...

''' 
3.Instruction

You are given list of integers (int). You should find the sum of the elements with even indexes (0th, 2nd, 4th...). 
Then multiply this summed number and the final element of the list together. Don't forget that the first element has an index of 0.
For an empty list, the result will always be 0 (zero).

Input: List of integers (int).
Output: An integer (int). 

Example: [1, 2, 3, 4, 5, 6] -> 54

2pts
'''

list1 = [5, 20, 15, 20, 25, 50, 20]


def checkio(list1):
    if len(list1) == 0:
       return 0
    even_indexed_elements_sum = 0
    for i in range(0, len(list1), 2):
        even_indexed_elements_sum += list1[i]
    return even_indexed_elements_sum * list1[-1]


    ...

'''
5.Instruction
-----------

In a given text you need to sum the numbers while excluding any digits that form part of a word.
The text consists of numbers, spaces and letters from the English alphabet.

Input: A string (str).
Output: An integer (int).

Example: "1 2 three 4 five" -> 7

3pts

'''
text =  "1 2 three 4 five" 


def sum_numbers(text):
  numbers = [int(num) for num in text.split() if num.isdigit()]
  return sum(numbers)
...