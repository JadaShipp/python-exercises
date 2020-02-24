#Conditional Basics --prompt the user for the day of the week, print out whether today is Monday or not
In [2]:

current_day_of_the_week = input('What is the day of the week? ')
if current_day_of_the_week.lower() == 'monday':
    print('Today is Monday')
else: 
    print ('Today is not Monday')
What is the day of the week? monday
Today is Monday
# --prompt the user for a day of the week, print out whether the day of the week is a weekday or weekend
In [4]:

day_of_the_week = input('What is the day of the week? ')
if day_of_the_week.lower() == 'saturday' or day_of_the_week == 'sunday':
    print('It is a weekend')
else:
    print('It a weekday')
What is the day of the week? sunday
It is a weekend
--create variables and make up values for
In [4]:

hours_worked_in_one_week = 51
hourly_rate = 50
​
if hours_worked_in_one_week <= 40:
    total = hourly_rate * hours_worked_in_one_week
else:
    overtime = hours_worked_in_one_week - 40
    overtime_pay = overtime * 1.5 * hourly_rate
    regular_pay = 40 * hourly_rate
    total = regular_pay + overtime_pay
    
print(f'Overtime pay is {total}')
​
    
​
Overtime pay is 2825.0
Loop Basics
While Loops:
# --Create an integer variable i with a value of 5.
# --Create a while loop that runs so long as i is less than or equal to 15 --Each loop iteration, output the current value of i, then increment i by one
In [8]:

i = 5
while i <= 15:
    print(i)
    i += 1 
5
6
7
8
9
10
11
12
13
14
15
# -Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
In [9]:

i = 0
while i <= 100:
    print(i)
    i += 2
0
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40
42
44
46
48
50
52
54
56
58
60
62
64
66
68
70
72
74
76
78
80
82
84
86
88
90
92
94
96
98
100
# -- Alter your loop to count backwards by 5's from 100 to -10.
In [15]:

i = 100
while i >= -10:
    print(i)
    i -= 5
100
95
90
85
80
75
70
65
60
55
50
45
40
35
30
25
20
15
10
5
0
-5
-10
# --Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:
# In [16]:

i = 2
while i < 1000000:
    print(i)
    i *= i
2
4
16
256
65536
# --Write a loop that uses print to create the output shown below.
In [17]:

i = 100
while i >= 5:
    print(i)
    i -= 5
100
95
90
85
80
75
70
65
60
55
50
45
40
35
30
25
20
15
10
5
# For Loops:
# Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.
# Create a list of integers from 1-10
# multipy the inpyt by the list one at a time
# In [33]:

user_input = input('Enter a number ')
user_input = int(user_input)
numbers = range(1,11)
for n in numbers:
    print(f'{user_input} x {n} = {n*user_input}')
​
​
    
​
Enter a number 7
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
In [29]:

pyramid = range(1,10)
​
for n in pyramid:
    print(f'{n}'*n)
1
22
333
4444
55555
666666
7777777
88888888
999999999
Break and Continue:
In [21]:

starting_point = -1
​
correct_number = input("Enter an odd number between 1 and 50: ")
correct_number = int(correct_number)
while correct_number < 1 or correct_number > 50 or correct_number % 2 == 0:
    print(f"{correct_number} is not a valid input, try again")
    correct_number = input("Enter an odd number between 1 and 50: ")
    correct_number = int(correct_number)
while starting_point <= 50:
    starting_point += 2
    if starting_point == correct_number:
        print(f"Yikes! Skipping number: {correct_number}")
        continue
    print(f" Here is an odd number: {starting_point}")
​
    
​
Enter an odd number between 1 and 50: 19
 Here is an odd number: 1
 Here is an odd number: 3
 Here is an odd number: 5
 Here is an odd number: 7
 Here is an odd number: 9
 Here is an odd number: 11
 Here is an odd number: 13
 Here is an odd number: 15
 Here is an odd number: 17
Yikes! Skipping number: 19
 Here is an odd number: 21
 Here is an odd number: 23
 Here is an odd number: 25
 Here is an odd number: 27
 Here is an odd number: 29
 Here is an odd number: 31
 Here is an odd number: 33
 Here is an odd number: 35
 Here is an odd number: 37
 Here is an odd number: 39
 Here is an odd number: 41
 Here is an odd number: 43
 Here is an odd number: 45
 Here is an odd number: 47
 Here is an odd number: 49
 Here is an odd number: 51
# -The input function can be used to prompt for input and use that input in your python code. Prompt the user to enter a positive number and write a loop that counts from 0 to that number. (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, so you'll need to convert this to a numeric type.)
# In [35]:

starting_point = 0
​
pos_num = input("Enter a positive number: ")
pos_num = int(pos_num)
while starting_point < pos_num+1:
    print(starting_point)
    starting_point += 1
​
Enter a positive number: 9
0
1
2
3
4
5
6
7
8
9
# -Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1
# In [47]:

# pos_int = input("Enter a positive integer ")
# pos_int = int(pos_int)
​
# starting_point = pos_int
# while pos_int == starting_point and pos_int >= 1:
#     print(starting_point)
#     starting_point -= 1
​
user_choice = input("Input a positive number ")
while (user_choice.isdigit() == False 
       or int(user_choice) <= 0):
    print(f'{user_choice} is not a positive integer')
    user_choice = input('please input a positive number')
user_choice = int(user_choice)
while user_choice >= 1:
    print(user_choice)
    user_choice -= 1
​
​
Input a positive number 8
8
7
6
5
4
3
2
1
# Fizz Buzz
# In [50]:

for i in range(1,100):
    if i % 5 == 0 and i % 3 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else: 
        print(i)
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
26
Fizz
28
29
FizzBuzz
31
32
Fizz
34
Buzz
Fizz
37
38
Fizz
Buzz
41
Fizz
43
44
FizzBuzz
46
47
Fizz
49
Buzz
Fizz
52
53
Fizz
Buzz
56
Fizz
58
59
FizzBuzz
61
62
Fizz
64
Buzz
Fizz
67
68
Fizz
Buzz
71
Fizz
73
74
FizzBuzz
76
77
Fizz
79
Buzz
Fizz
82
83
Fizz
Buzz
86
Fizz
88
89
FizzBuzz
91
92
Fizz
94
Buzz
Fizz
97
98
Fizz
# -Display a table of powers. -Prompt the user to enter an integer. -Display a table of squares and cubes from 1 to the value entered. -Ask if the user wants to continue. -Assume that the user will enter valid data. -Only continue if the user agrees to.
# In [63]:

while True:
    user_choice = input("Input a positive number ")
    while (user_choice.isdigit() == False 
           or int(user_choice) <= 1):
        print(f'{user_choice} is not a positive integer')
        user_choice = input('please input a positive number')
    user_choice = int(user_choice)
​
    print(' number| squared | cubed|')
    for i in range(1, user_choice +1):
        print(f'{i} | {i**2}  | {i**3} ')
    choice = input('Do you want to continue? Type y or yes ')
    choice = choice.lower()
    if chioce not in ['y','yes']:
         break
​
Input a positive number 7
 number| squared | cubed|
1 | 1  | 1 
2 | 4  | 8 
3 | 9  | 27 
4 | 16  | 64 
5 | 25  | 125 
6 | 36  | 216 
7 | 49  | 343 
Do you want to continue? Type y or yes y
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-63-7c6ac3fe157d> in <module>
     12     choice = input('Do you want to continue? Type y or yes ')
     13     choice = choice.lower()
---> 14     if chioce not in ['y','yes']:
     15          break

NameError: name 'chioce' is not defined

# Convert given number grades into letter grades. Prompt the user for a numerical grade from 0 to 100. Display the corresponding letter grade. Prompt the user to continue. Assume that the user will enter valid integers for the grades. The application should only continue if the user agrees to. Grade Ranges: A : 100 - 88 B : 87 - 80 C : 79 - 67 D : 66 - 60 F : 59 - 0