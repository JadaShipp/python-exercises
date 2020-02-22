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
def cap_first(word):
    if is_consonant(word[0]) == True:
        return word.capitalize()
    else:
        return "Can not capitalize becuase input is not a consonant"
# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip(tip,bill_total):
    if type(tip) == float:
        return tip * bill_total
# 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.
def apply_discount(original_price, discount_percentage):
    if type(discount_percentage) == float:
        return f'Your price after discount is: {original_price - (original_price * discount_percentage)}'

# 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.
def handle_commas(numbers):
    numbers = numbers.replace(",", "")
    new = int(numbers)
    return new
# 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).
def get_letter_grade(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"