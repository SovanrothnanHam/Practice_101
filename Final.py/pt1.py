'''
Ex1
In this mission you need to create a password verification function.

The verification conditions are:

the length should be bigger than 6;
should contain at least one digit, but cannot consist of just digits.
Input: A string (str).

Output: A logic value (bool).

Examples:

assert is_acceptable_password("short") == False
assert is_acceptable_password("muchlonger") == False
assert is_acceptable_password("ashort") == False
assert is_acceptable_password("muchlonger5") == True

'''


def is_acceptable_password(password):
  # Check if the password is longer than 6 characters.
  if len(password) < 7:
    return False
  # Check if the password contains at least one digit.
  if not any(c.isdigit() for c in password):
    return False
  # Check if the password does not consist of just digits.
  if all(c.isdigit() for c in password):
    return False
  # The password is acceptable.
  return True

def is_acceptable_password(password):
    if len(password) > 6 and any(char.isdigit() for char in password) and not password.isdigit():
        return True
    else:
        return False