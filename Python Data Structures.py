
##########################################################
###### Python for Everybody Coursera Specialization ######
######      Course #2: Python Data Structures       ######
######                  Emily Sheen                 ######
##########################################################

### Chapter 6: Strings

x = 'From marquard@uct.ac.za'
# How would you use the inndex operator [] to print out the q from the string x
x[8]

# How would you use string slicing [:] to print out 'uct' from the following string?
x = 'From marquard@uct.ac.za'
x[14:17]

for letter in 'banana' :
    print(letter)

print(len('banana')*7)

greet = 'Hello Bob'
# How would you print greet in all uppercase
greet.upper()

greet.join(" Johnson")

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(pos)
print(data[pos:pos+3])

y = "     Poopy butt     "
print(y.strip())

# 6.5 Write code using find() and string slicing (see section 6.10) to extract the number
# at the end of the line below. Convert the extracted value to a floating point number and
# print it out.

# Use https://regex101.com/ to check regular expressions
import re
text = "X-DSPAM-Confidence:    0.8475"

print(re.findall(r"\d+\.\d+", text))

# Using regular find() function
float(text[text.find("0"):len(text)])
float(text[text.find(":")+1:len(text)].strip())

### Chapter 7: Files
### open function creates a handle to handle the file, step before actually reading the file
file_handle = open("words.txt", "r")
for cheese in file_handle:
    print(cheese)
    # prints each line in the txt file

file_handle = open("words.txt", "r")
inp = file_handle.read()
print(inp)
print(len(inp))

file_handle = open("words.txt", "r")
for line in file_handle:
    if line.startswith("I"):
        print(line)

file_handle = open("words.txt", "r")
for line in file_handle:
    line = line.rstrip()
    if line.startswith("I"):
        print(line)

file_handle = open("words.txt", "r")
for line in file_handle:
    line = line.rstrip()
    if not line.startswith("I"):
        continue
    else:
        print(line)

file_handle = open("words2.txt", "r")
for line in file_handle:
    line = line.rstrip()
    print(line.upper())

# 7.2 Write a program that prompts for a file name, then opens that file and reads
# through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines
# and compute the average of those values and produce an output as shown below.
# Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
# when you are testing below enter mbox-short.txt as the file name.

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
cnt = 0
tot = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        cnt = cnt + 1
        tot = tot + float(line[line.find(":")+1:len(line)].strip())
the_avg = tot/cnt
# print(the_avg)
the_avg = str(the_avg)
print("Average spam confidence:" + the_avg)



### Chapter 8: Lists, Dictionaries and Tuples

# Collection: A list is a collection: one variable for several things

# E.g. a list of strings:
friends = ["Joey", "Alex", "Willa", "Ashley", "Kaelyn"]

# E.g. a list of integers
ints = [1, 2, 3, 4, 5]

# e.g. a list of lists
my_lists = [1, [5,6], 7, [8,9,10]]

#e.g. an empty list
empty_list = []

print(friends[0])
print(friends[2])

# Lists are not mutable, for example, we can change the friends list to replace Willa with Carmela:
friends[2] = "Carmela"
print(friends)

# Strings are immutable...we cannot change parts of the string
best_friend = "Willa"
best_friend[0] = "K"
print(best_friend)

# Length function len works the same for lists and strings
print(len(friends))
print(len(best_friend))

# Range function returns the integers corresponding to positions in a list of size n
n = 7
# According to class, print(range(n)) should return [0, 1, 2, 3, 4, 5, 6]
print(range(n))
# actually returns "range(0,7)"

# Counted loop
for i in range(n):
    print(i)

# List Manipulation

# Concatenating lists works the same way as concatenating strings:
# For example
int_list = [1, 2, 3] + [4, 5, 6]
print(int_list)

mixed_list = [1, 2, 3] + ["alpha", "bravo", "charlie"]
print(mixed_list)
print(mixed_list[2:4])
print(mixed_list[:6])
print(mixed_list[:5])
print(mixed_list[2:])
print(mixed_list[:])  # prints everything, same as print(mixed_list)

# Functions with lists
type(mixed_list)
dir(mixed_list)  # Gives a directory of functions you can perform on your list

# Constructing lists from scratch
stuff = list() # empty list
stuff.append("book")
stuff.append(99)
stuff.append("cookie")
print(stuff)

# Using "in"
print("book" in stuff)
print(98 in stuff)
print(99 in stuff)
print(20 not in stuff)
print("99" not in stuff) # because 99 int is in list, not string version
print(99 not in stuff)

# print(stuff.sort()) # We cannot sort a mixed list with integers and strings

friends.sort()  #Sorts the list friends in alphabetical order and saves it back into "friends"
print(friends)
# Note that print(friends.sort()) does not work...must apply the function to friends and then print.

nums = [3, 41, 12, 9, 74, 15]
print(len(nums))
print(min(nums))
print(max(nums))
print(sum(nums))
print(sum(nums)/len(nums))


# A different way to do exercise similar to Exercises 5.2 and 7.2:
# Instead of tallying count and total of additional numbers each step of the while loop,
# We append each new input number into a list and then take the average funtion (or other function) after 'done' is input.
numList = list()
while(True):
    inp = input("Enter a number: ")
    if inp == "done":
        break
    else:
        try:
            value = float(inp)
        except ValueError:
            print("Oops! Enter a valid floating number.")
            continue
        numList.append(value)

average = sum(numList)/len(numList)
print(average)
print(numList)
print(max(numList))
print(min(numList))