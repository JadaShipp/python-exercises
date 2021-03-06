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
for product in it.product('abc','123'):
    count_of_products.append(total)
print(len(count_of_products))

# 2. How many different ways can you combine two of the letters from "abcd"?
count_of_combos = []
total = 0
for combo in it.combinations('abcd',2):
    count_of_combos.append(total)
print(len(count_of_combos))

# 3. Save json file as a variable
profiles = json.load(open("profiles.json"))

# Total number of users
len(profiles)

# Number of active users
len([profile for profile in profiles if profile['isActive'] == True])

# You do not need the == True becuase the [] is already a boolean expression

len([profile for profile in profiles if profile['isActive'])

# Number of inactive users
len([profile for profile in profiles if profile['isActive'] == False])

# Alternative

len([profile for profile in profiles if not profile['isActive'])

# Grand total of balances for all users
balance_list = [profile['balance',] for profile in profiles]

float_balances = [float(profile['balance'].replace('$','').replace(',','')) for profile in profiles]

total = sum(float_balances)

# Alternative
def get_profile_balance(profile):
    return float(profile['balance'].replace('$','').replace(',',''))

balances = sum(get_profile_balance(profile) for profile in profiles)

# Average balance per user
import statistics

average_total = sum(float_balances)/len(profiles)

# Alternative

balances = sum(get_profile_balance)/len(profiles)

# User with the lowest balance
float_balances = [float(profile['balance'].replace('$','').replace(',','')) for profile in profiles]
    # Get the minimal number in this list
min(float_balances)
    # Create a new list with only the one minimal value
min_list[]
min_list = [n for n in range(len(float_balances)) if float_balances[n] == min(float_balances)]

    #give the name and balance at the index from the list of balances
name_with_min_balance = profiles[min_list[0]]['name'], profiles[min_list[0]]['balance']

# Alternatives

user_with_lowest_balance = profiles[0]

for user in profiles [1:]:
    if get_profile_balance(user) < get_profile_balance(user_with_lowest_balance):
        user_with_lowest_balance = user
user_with_lowest_balance

# Alternatives #2 

min(profiles, key = get_profile_balance)

# User with the highest balance
max(float_balances)

#create a new list with only one maximum value
max_list = []
max_list = [n for n in range(len(float_balances)) if float_balances[n] == max(float_balances)]

#give the name and balance at the index from the list of balances

name_with_max_balance = profiles[max_list[0]]['name'], profiles[max_list[0]]['balance']

# Most common favorite fruit
list_of_favfruits = [profile['favoriteFruit'] for profile in profiles]

from collections import Counter

most_popular_fruit = max(Counter([profile['favoriteFruit'] for profile in profiles]))

# If you want the name of the most popular fruit with the count of that fruit use:

Counter(list_of_favfruits)
x = 3
d = Counter(list_of_favfruits)

# You now have a list of tuples. Use .most_common() to put them in order from highest to lowest

top_fruit = d.most_common()

# Use indexing to find the most popular

top_fruit[0]

# Least most common favorite fruit
list_of_favfruits = [profile['favoriteFruit'] for profile in profiles]

from collections import Counter

least_popular_fruit = min(Counter([profile['favoriteFruit'] for profile in profiles]))

Counter(list_of_favfruits)
x = 3
d = Counter(list_of_favfruits)

top_fruit = d.most_common()

top_fruit[-1]

# Total number of unread messages for all users

list_of_unreadmessages_as_string = [profile['greeting'] for profile in profiles]



