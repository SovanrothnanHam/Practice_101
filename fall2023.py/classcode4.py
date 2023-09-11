import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100  # Convert height to meters
        bmi = weight / (height * height)
        bmi_result.set(f"Your BMI: {bmi:.2f}") 
    except ValueError:
        messagebox.showerror("Error", "Please enter valid weight and height.")
root = tk.Tk()
root.title("BMI Calculator")

# Create and place widgets
weight_label = tk.Label(root, text="Enter Weight (kg):")
weight_label.pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

height_label = tk.Label(root, text="Enter Height (cm):")
height_label.pack()
height_entry = tk.Entry(root)
height_entry.pack()

calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack()

bmi_result = tk.StringVar()
bmi_label = tk.Label(root, textvariable=bmi_result)
bmi_label.pack()

# Start the GUI event loop
root.mainloop()
# number1, number2, number3 = eval(input(
#   "Enter three numbers separated by commas: "))

# # Compute average
# average = (number1 + number2 + number3) / 3

# # Display result
# print("The average of", number1, number2, number3,
#     "is", average)
# number1 = eval(input("Enter the first number: "))
# number2 = eval(input("Enter the second number: "))
# number3 = eval(input("Enter the third number: "))

# # Compute average
# average = (number1 + number2 + number3) / 3

# # Display result
# print("The average of", number1, number2, number3, 
#     "is", average)