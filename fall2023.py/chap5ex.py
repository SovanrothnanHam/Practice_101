"""5.1.(Count positive and negative numbers and compute the average of numbers)
Write a program that reads an unspecified number of integers, determines
how many positive and negative values have been read, and computes the total
and average of the input values (not counting zeros). Your program ends with the
input 0. Display the average as a floating-point number."""
def count_positive_negative_numbers(numbers):
  """Counts the number of positive and negative numbers in a list of numbers."""
  positive_count = 0
  negative_count = 0
  for number in numbers:
    if number > 0:
      positive_count += 1
    elif number < 0:
      negative_count += 1
  return positive_count, negative_count
def compute_average(numbers):
  """Computes the average of a list of numbers."""
  total = sum(numbers)
  count = len(numbers)
  return total / count
def main():
  """Prompts the user to enter a list of integers and prints the number of positive,
  negative, and total numbers, as well as the average of the positive and negative
  numbers."""
  numbers = []
  positive_count, negative_count = 0, 0
  while True:
    number = eval(input("Enter an integer (0 to quit): "))
    if number == 0:
      break
    numbers.append(number)
  positive_count, negative_count = count_positive_negative_numbers(numbers)
  total = compute_average(numbers)
  print("The number of positive numbers is", positive_count)
  print("The number of negative numbers is", negative_count)
  print("The total number of numbers is", positive_count + negative_count)
  print("The average of the positive and negative numbers is", total)
if __name__ == "__main__":
  main()

