
### Starting with Python...Steps
### 1) Create a new conda environment for Python for Everyone course, called py4e, "conda create --name py4e" in Terminal
### 2) "conda activate py4e", "conda info --envs"
### 3) In PyCharm, Create a new project using the conda environment you created, py4e.


x = 1
print(x)

x = x+2
print(x)

# RESERVED WORDS: "and", "as", "assert", "break", "class", "continue", "def", "del"
# "elif", "else", "except", "False", "finally", "for", "from", "global", "if",
# "import", "in", "is", "lambda", "None", "nonlocal", "not", "or", "pass", "raise",
# "return", "True", "try", "while", "with", "yield"

print("hello world")

print("42 % 10 is: " + str(42%10))

print(int(98.6))

name = input("Enter your name: ")
print("Hello "+name)

if{x > 1}:
    print("x is "+ str(x))

# To run only a highlighted selection of code, use ⌥ ⇧ E (Option Shift E)
x = 6
if x == 6 :
    print('Is 6')
    print('Is Still 6')
    print('Third 6')


x = 0
if x < 2 :
    print('Small')
elif x < 10 :
    print('Medium')
else :
    print('LARGE')
print('All done')


astr = 'Hello Bob'
istr = int(astr)
print('First', istr)
astr = '123'
istr = int(astr)
print('Second', istr)

astr = 'Hello Bob'
istr = 0
try:
    istr = int(astr)
except:
    istr = -1

print(istr)

hrs = input("Enter Hours:")
h = float(hrs)

rate = input("Enter Rate:")
r = float(rate)

if h > 40:
    pay = 40 * r + (h - 40) * 1.5 * r
elif h <= 40 & h > 0:
    pay = 40 * 4
else:
    pay = 0

print(pay)

# To make a block comment in Pycharm, highlight the text and press ⌘ / (Command /)

# 3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error.
# If the score is between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.

score = float(input("Enter Score: "))
if (score > 1 or score < 0):
    print("Error.  Enter score in range [0,1]")
    exit()
elif(score >= 0.9):
    print("A")
elif(score >= 0.8):
    print("B")
elif(score >= 0.7):
    print("C")
elif(score >= 0.6):
    print("D")
elif(score < 0.6):
    print("F")


###  Chapter 4: Functions
def thing():
    print("the thing is: ")
    print("Sponge")

thing()

import math
def circumference(radius):
    return(radius*math.pi*2)

print(circumference(4))

# 4.6 Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
# Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours
# worked above 40 hours. Put the logic to do the computation of pay in a function called computepay() and
# use the function to do the computation. The function should return a value. Use 45 hours and a rate of
# 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and
# float() to convert the string to a number. Do not worry about error checking the user input unless you
# want to - you can assume the user types numbers properly. Do not name your variable sum or use the sum() function.

def computepay(h, r):
    if (h > 40 and r > 0):
        pay = 40*r + (h-40)*1.5*r
        return pay
    elif(h > 0 and h <= 40 and r > 0):
        pay = 40*r
        return pay
    else:
        print("Error: Hours and pay rate must be positive.")
        exit()

hrs = float(input("Enter Hours: "))
rate = float(input("Enter Hourly Pay Rate: "))
p = computepay(hrs, rate)
print("Pay", p)


### Chapter 5: Loops and Iteration
# While Loop: indefinite, need condition to eventually become false
n = 5
while (n > 0):
    print(n)
    n = n-1
print("Blast off!")
print(n)

### STOP AN INFINITE LOOP WITH CTRL + C

# "break" statement ends the current loop and jumps to the statement immediately following the loop
# "continue" statement skips the current iteration but goes back to the top of the loop at the next iteration

# For loop = definite loops, iterate over all numbers in a sequence, all characters in a text, etc.
for i in [5, 4, 3, 2, 1]:
    print(i)
print("Blast Off!")


# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything
# other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.
# Enter 7, 2, bob, 10, and 4 and match the output below.

largest = None
smallest = None
while True:
    num = input("Enter an integer or 'done' to finish: ")
    if num == "done":
        break
    else:
        try:
            num = int(num)
        except ValueError:
            print("Oops! Enter a valid integer.")
            continue
    if largest == None:
        largest = num
    elif largest != None and num > largest:
        largest = num
    if smallest == None:
        smallest = num
    elif smallest != None and num < smallest:
        smallest = num

print("Maximum", largest)
print("Minimum", smallest)

def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

print(greet('fr'),'Michael')

def addtwo(a, b):
    added = a + b
    return a

x = addtwo(2, 7)
print(x)