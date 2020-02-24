functions_exercises.py
# 4.5_function_exercises.py

# 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.
# >>> def is_two(number):
#      if number == "2":
#          return True
#     elif number == 2:
#         return True
#     else: 
#        return False
# >>> is_two(5)
# False

#Alterative
def is_two(x):
    return x == 2 or x == '2'

# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
# >>> def is_vowel(letter):
#      return letter.lower() in "aeiou"
# is_vowel("a")
# True

#Alernative
def is_vowel(letter):
     return letter.lower() in "aeiou" and len(letter) == 1

# #Second Alternative
# def is_vowel(letter):
#     vowel = 'aeiou'
# #is the letter in the list of vowels
#     for vowel in vowels:
#         if letter.lower() == vowel:
#             return True
# #since it's not a vowel tell me it's not a character
#     return False


# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.
# def is_consonant(x):
#      return not is_vowel(x)

# Alternative
def is_consonant(letter):
    letters = 'abcdefghijklmnopqrstuv'
    return len(letter) == 1 and letter.lower in letter and not is_vowel(letter)

#     # or
# def is_consonant(letter):
#     letters = 'abcdefghijklmnopqrstuv'
#     return len(letter) == 1 and letter.isalpha() and not is_vowel(letter)

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

#Alternative
# def calculate_tip(tip,bill_total):
#     #create a variable to hold the value so that you can just call the variable name in the return statement
#     amount_to_tip = bill_total * tip
#         return amount_to_tip

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

# 9 Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.
# def remove_vowels(words):
#     words_without_vowels = words
#     vowels = ['a','e','i','o','u']
#     for n in vowels:
#         words_without_vowels = words_without_vowels.replace(n,"")
#     return words_without_vowels
# Alternative
def remove_vowels(string):
    string_without_vowels = " "
    for c in string:
        if not is_vowel(c):
            string_without_vowel += c
    return string_without_vowels

# # Second Alternative
# def remove_vowels(string):
#     return ''.join([c for c in string if not is_vowel])

# 10 Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed, everything should be lowercase, spaces should be replaced with underscores


# def normalize_name(names):
#     names = names.lower()
#     names = names.replace(" ","_")
#     for x in names:
#         if x.isdigit() == True 
#             return "Enter a name without numbers"
#         else:
#             return names


#Alternative
def remove_special_characters(string):
    return ''.join([c for c in string if c.isalnum() or c == ' '])

def normalize_name(string):
    without_out_special_char = remove_special_characters(string)
    return without_out_special_char.lower.strip().replace(' ','_')
    


# Write a function named cumsum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.

def cumsum(number):
    total = 0
    cumsum = []
    for n in number:
       total += n
       cumsum.append(total)
    return cumsum

# Create a function named twelveto24. 
# It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. 
# Bonus write a function that does the opposite.

# Python program to convert time 
# from 12 hour to 24 hour format 
  
# Function to convert the date format 
# def convert24(time): 
      
#     # Checking if last two elements of time 
#     # is AM and first two elements are 12 
#     if time[-2:] == "AM" and time[:2] == "12": 
#         return "00" + time[2:-2]    
#     elif time[-2:] == "AM": 
#         return time[:-2]     
#     elif time[-2:] == "PM" and time[:2] == "12": 
#         return time[:-2]      
#     else: 
          
#         return str(int(time[:2]) + 12) + time[2:8]