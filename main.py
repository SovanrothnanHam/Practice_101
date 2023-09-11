# 1.
# s1 = "Welcome to Python programming"
# s2 = "Let's have fun"
# print((s2.lower()+s1[10:]).replace(" ","_"))
# output let's_have_fun_Python_programming
# s2 lower() converts s2 into lowercase: 'let's have some fun'.
# s1[10:] returns 'Python prgramming'
# from index 9 till end of string, which is then concatenated with the converted version of s2 
# in uppercase and separated by an underscore '_', resulting in a new variable called result containing all characters except 
# using replace(). The space between words in original sentence are replaced by underscores (_) and returned as final

# 
# seconds = eval(input("Enter an integer for seconds: "))
#  # Get minutes and remaining seconds
# minutes = seconds // 60 # Find minutes in seconds
# remainingSeconds = seconds % 60 # Seconds remaining
# print(seconds, "seconds is", minutes, "minutes and", remainingSeconds, "seconds")
