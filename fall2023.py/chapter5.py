# 1.
# count = 0
# while count < 100:
#     print("Programming is fun!")   
#     count +=1
# 2.
# sum = 0
# i = 1
# while i < 10:
#     sum = sum + i
#     i = i + 1
# print("sum is", sum)

# import random

# # 1. Generate two random single-digit integers
# number1 = random.randint(0, 9)
# number2 = random.randint(0, 9)

# # 2. If number1 < number2, swap number1 with number2
# if number1 < number2:
#     number1, number2 = number2, number1
# # 3. Prompt the student to answer "What is number1 - number2?"

# answer = eval(input("What is " + str(number1) + " - "
# + str(number2) + "? "))

# # 4. Repeatedly ask the question until the answer is correct
# while number1 - number2 != answer:
#     answer = eval(input("Wrong answer. Try again. What is "+ str(number1) + " - " + str(number2) + "? "))
# print("You got it!")

# import random

# # Generate a random number between 0 and 100
# number = random.randint(0, 100)

# # Continuously prompt the user for a guess
# while True:
#     # Get the user's guess
#     guess = int(input("Guess a magic number between 0 and 100: "))

#     # Check if the guess is correct
#     if guess == number:
#         print("Yes, the number is", number)
#         break
#     elif guess > number:
#         print("Your guess is too high")
#     else:
#         print("Your guess is too low")

# import tkinter as tk
# from tkinter import messagebox
# import random

# # Function to generate a subtraction question
# def generate_question():
#     num1 = random.randint(1, 20)
#     num2 = random.randint(1, 20)
#     question = f"What is {num1} - {num2}?"
#     answer = num1 - num2
#     return question, answer

# # Function to check the user's answer
# def check_answer():
#     user_answer = answer_entry.get()
#     try:
#         user_answer = int(user_answer)
#     except ValueError:
#         messagebox.showerror("Error", "Please enter a valid number.")
#         return

#     if user_answer == current_question[1]:
#         messagebox.showinfo("Correct", "Congratulations! You got it right!")
#         window.quit()
#     else:
#         messagebox.showerror("Incorrect", "Try again!")

# # Create the main window

# window = tk.Tk()
# window.title("Subtraction Quiz")

# # Generate the initial question
# current_question = generate_question()

# # Create and configure widgets
# question_label = tk.Label(window, text=current_question[0])
# answer_entry = tk.Entry(window)
# submit_button = tk.Button(window, text="Submit", command=check_answer)

# # Pack widgets
# question_label.pack()
# answer_entry.pack()
# submit_button.pack()

# # Start the Tkinter main loop
# window.mainloop()

# print(" Multiplication Table")
# # Display the number title
# print("|", end = '')
# for j in range(1,10):
#     print(" ", j, end = '')
# print() # Jump to the new line
# print("——————————————————————————————————————————")

# #  Display table body
# for i in range(1,10):
#     print(i, "|", end = '')
#     for j in range(1,10):
# # Display the product and align properly
#         print(format(i * j, "4d"), end = '')
#     print() # Jump to the new line

for i in range(1, 5): 
    j = 0
    while j < i: 
        print(j, end = " ")
        j+=0
