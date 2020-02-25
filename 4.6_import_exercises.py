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
for combo in itertools.combinations('abcd',2):
    count_of_combos.append(total)
print(len(count_of_combos))

# 3. Save json file as a variable
profiles = json.load(open("profiles.json"))

# Total number of users
len(profiles)

# Number of active users
len([profile for profile in profiles if profile['isActive'] == True])

# Number of inactive users
len([profile for profile in profiles if profile['isActive'] == False])

# Grand total of balances for all users
balance_list = [profile['balance',] for profile in profiles]

float_balances = [float(profile['balance'].replace('$','').replace(',','')) for profile in profiles]

total = sum(float_balances)

# Average balance per user
import statistics

average_total = sum(float_balances)/len(profiles)

# User with the lowest balance
float_balances = [float(profile['balance'].replace('$','').replace(',','')) for profile in profiles]
min(float_balances)
min_list[]
min_list = [n for n in range(len(float_balances)) if float_balances[n] == min(float_balances)]

name_with_min_balance = profiles[min_list[0]]['name'], profiles[min_list[0]]['balance']