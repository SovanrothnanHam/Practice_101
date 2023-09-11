# 1. Detect and add element in the list
list_a = [1, 2, 3, 4, 5]

# detect if an element in the list is even,
# add 10 on the right index of the detected element
# example: [1, 2, 3, 4, 5] -> [1, 2, 10, 3, 4, 10, 5]


def add_if_even(list_a):
    temp_list = []
    for a in list_a:
        if a % 2 == 0:
            temp_list.append(a)
            temp_list.append(10)
        else:
            temp_list.append(a)
    return temp_list


# 2. Remove all duplicate elements in the list
list_b = [1, 2, 3, 5, 1, 2, 4, 5]
# tip: use count() method https://www.w3schools.com/python/ref_list_count.asp
# example: [1, 2, 3, 5, 1, 2, 4, 5] -> [3, 4]


def remove_duplicate(list_b):
    temp_list = []
    for b in list_b:
        if list_b.count(b) == 1:
            temp_list.append(b)
    return temp_list


# 3. Sum all the odd numbers in the list
list_c = [1, 2, 3, 4, 5]
# example: [1, 2, 3, 4, 5] -> 9


def sum_odd(list_c):
    sum = 0
    for c in list_c:
        if c % 2 != 0:
            sum += c
    return sum


# 4. Reverse the list
list_d = [1, 2, 3, 4, 5]
# example: [1, 2, 3, 4, 5] -> [5, 4, 3, 2, 1]


def reverse_list(list_d):
    return list_d[::-1]


# 5. Count the number of time f appear in the below text
text = "f is a letter in the alphabet f and it is use in friendship"
# example: f -> 3


def count_f(text):
    return text.count("f")


# 6. Find and replace "o" with "0" in the below text
text = "Hello World"
# example: "Hello World" -> "Hell0 W0rld"


def replace_o(text):
    return text.replace("o", "0")

