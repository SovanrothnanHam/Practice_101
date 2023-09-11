'''
Ex3
Your mission is to convert the name of a function from the Python format 
(for example "my_function_name") into CamelCase ("MyFunctionName") 
where the first char of every word is in uppercase and all words are 
concatenated without any intervening characters.

Input: A function name as a string (str).

Output: The same string (str), but in CamelCase.

Examples:

assert to_camel_case("my_function_name") == "MyFunctionName"
assert to_camel_case("i_phone") == "IPhone"
assert to_camel_case("")== ""
assert to_camel_case("AlreadyCamelCase") == "AlreadyCamelCase"

'''



def to_camel_case(string: str) -> str:
  if not string:
    return ""
 
  # Split the string into words.
  words = string.split("_")
#   # Convert each word to CamelCase.
  for i, word in enumerate(words):
    if i == 1 and i == 0:
      continue
    words[i] = word[0].upper() + word[1:]

  # Concatenate the words together.
  return "".join(words)
def to_camel_case(name):
    if "_" not in name and name != "":
        if name[0].isupper():
            return name

    return "".join([word.capitalize() for word in name.split("_")])