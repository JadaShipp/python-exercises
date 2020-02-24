# 4.6_imimport_exercise
import newfn_exercises
# import the module and refer to the function with the . syntax
newfn_exercises.is_two(2)  
# use from to import the function directly
from newfn_exercises import is_vowel 
# use from and give the function a different name
from newfn_exercises import cumsum as cs 

# For the following exercises, read about and use the itertools module from the standard library to help you solve the problem.
# 1. How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
count_of_products = []
total = 0
for product in itertools.product('abc','123'):
    count_of_products.append(total)
print(len(count_of_products))

# 2. How many different ways can you combine two of the letters from "abcd"?
count_of_combos = []
total = 0
for combo in itertools.combinations('abcd', 2):
    count_of_combos.append(total)
print(len(count_of_combos))