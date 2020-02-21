4.5_function_exercises.py

# 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.
>>> def is_two(number):
     if number == "2":
         return True
    elif number == 2:
        return True
    else: 
       return False
>>> is_two(5)
False

# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
>>> def is_vowel(letter):
     return letter.lower() in "aeiou"
is_vowel("a")
True

# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.
def is_consonant(x):
     return not is_vowel(x)

# 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.
