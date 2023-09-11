"""Name: Ham Sovanrothnan
Exercise No.22.(Display prime numbers between 2 and 1,000) Modify Listing 5.13 to display all
the prime numbers between 2 and 1,000, inclusive. Display eight prime numbers
per line. """
"""1.	Rewrite the problem in the form of algorithm:
        1. Initialize a variable `count` to 0.
        2. Iterate over the range from 2 to 1000 (inclusive) using the variable `num`.
        3. Set a Boolean variable `is_prime` to True.
        4. For each number, check if it is prime. A number is prime if it is only divisible by 1 and itself.
        5. Check if `num` is divisible by `i`. If it is, set `is_prime` to False and break out of the loop.
        6. If `is_prime` is still True after the inner loop, `num` is a prime number.
        7. Print `num` followed by a space, and increment `count` by 1.
        8. Check if `count` is divisible by 8. If it is, print a new line.
        9. Repeat steps 4-8 for all numbers in the range.
        10. The code will display all the prime numbers between 2 and 1000, with eight prime numbers per line.
"""
"""2.	Code the algorithm"""
count = 0
for num in range(2, 1001):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")
            count += 1
            if count % 8 == 0:
                print()


"""3.Optional: Develop your exercise with a User Interface (UI) """
import tkinter as tk
primes = []
count = 0
for num in range (2, 1001):
        is_prime = True
        for i in range (2, int (num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
            count += 1
root = tk.Tk()
root.title("Prime Numbers")
root.geometry("400x300")

text = tk.Text(root, height=50, width=50)
text.pack()
for i, prime in enumerate(primes):
        text.insert(tk.END, str(prime) + " ")
        if (i + 1) % 8 == 0:
            text.insert(tk.END, "\n")

root.mainloop()

