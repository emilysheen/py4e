
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


### Manipulating strings and lists
abc = "With three words"
stuff = abc.split()
print(stuff)
print(stuff[0])
print(len(stuff))

# Try using this with the txt file examples
fhand = open("words2.txt", "r")
# Lets make a single list of all the words in the file:
allWords = list()
for line in fhand:
    line = line.rstrip()  #Removes new lines at end of line
    newListWords = line.split()
    allWords.append(newListWords[:len(newListWords)])
print(allWords)
# This is a list of lists, where each inner list is a line in words2.txt

# Let's say we just want one big list of all the words without separate inner lists for the lines of words
# This is easy for me in R, but I'm not used to how Python loops over lists

fhand = open("words2.txt", "r")
# Lets make a single list of all the words in the file:
allWords = list()
for line in fhand:
    line = line.rstrip()  #Removes new lines at end of line
    newListWords = line.split()
    i = 0
    while i < len(newListWords):
        allWords.append(newListWords[i])
        i = i+1
print(allWords)

# Now allWords is just one big list of words, instead of a list of lists of words

# Instead of splitting into words by whitespace (the default for str.split()), we can split by any other character

email = "emilymsheen@gmail.com"
chunks = email.split('@')
print(email)
print(chunks)

# Chapter 8 quiz double checking... 100% score
fruit = 'Banana'
fruit[0] = 'b'
print(fruit)

x = list(range(5))
print(x)

### Exercise 8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list
# of words using the split() method. The program should build a list of words. For each word on each line
# check to see if the word is already in the list and if not append it to the list. When the program completes,
# sort and print the resulting words in python sort() order as shown in the desired output.
# You can download the sample data at http://www.py4e.com/code3/romeo.txt
fname = input("Enter file name: ")
fh = open(fname, "r")
word_list = list()
for line in fh:
    line = line.rstrip()
    line_words = line.split()
    # print(line_words)
    i = 0
    while i < len(line_words):
        if line_words[i] not in word_list:
            word_list.append(line_words[i])
            # print(word_list)
            i = i+1
        else:
            i = i+1

word_list.sort()  # This function both sorts and overwrites word_list to the sorted list
print(word_list)

### Exercise 8.5 Open the file mbox-short.txt and read it line by line. When you find a line that
# starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line
# (i.e. the entire address of the person who sent the message). Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'. Also look at the last line
# of the sample output to see how to print the count.

# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt

fname = input("Enter file name: ")  # Input "mbox-short.txt"
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    line = line.rstrip()
    words = line.split()
    if len(words) > 0 and words[0] == "From":
        print(words[1])
        count = count + 1
    else:
        continue
print("There were", count, "lines in the file with From as the first word")


### Chapter 9: Python Dictionaries
# Many people fall in love with Python dictionaries
# lists and dictionaries are the 2 most important data structures in Python
# Key idea is the "associative array": https://en.wikipedia.org/wiki/Associative_array
# In Java: dictionaries are called properties or map or hashmap
# In C#/.Net: they are called Property Bag

# Example Dictionary
# Labeling value 'Kim' as the 'mother' of the family
# Unsorted bag of values, but the value can be found by the lookup tag:
# Order of dictionaries is not predictable, does not necessarily follow the order you add things to the dictionary
family = dict()
family['mother'] = "Kim"
family['father'] = 'Dan'
family['brother'] = 'Peter'
family['self'] = 'Emily'
print(family)
print(family['self'])
print(family['Emily'])  # Emily is not the tag
# mother, father, etc. are the "lookup tags" for the dictionary
# Kim, Dan etc are the values associated with the tags

# Counting with Dictionaries
# The method explained in the course was pretty dumb.
# When a second instance was encountered, 1 is added to the prior dictionary key value

'mother' in family  #True
'father' in family #True
'grandmother' in family #False

#Creating a histogram of names using dictionary
name_counts = dict()
names = ['Emily', 'Peter', 'Kim', 'Dan', 'Kim', 'Emily', 'Emily', 'Shelby', 'Shirley', 'Peter']
for name in names:
    if name in name_counts:
        name_counts[name] = name_counts[name] + 1
    else:
        name_counts[name] = 1
print(name_counts)

# Get the key value for a dictionary tag name, get a default value if the key doesn't exist, rather than error traceback
name_counts.get('Kim', 0)

# Simpler loop using get
name_counts = dict()
print(name_counts)
for name in names:
    name_counts[name] = name_counts.get(name, 0) + 1
print(name_counts)
#Get function removes the if/else in the for loop

# For an input file (words2.txt), make a dictionary that counts each word's occurrence in the text
fhand = open("words2.txt", "r")

word_counts = dict()
for line in fhand:
    line_words = line.rstrip().lower().split()  #This works, so you can sequentially apply these functions to the string
    for word in line_words:
        word_counts[word] = word_counts.get(word, 0) + 1

print(word_counts)

for word in word_counts:
    print(word)

print(word_counts.values())

### Exercise 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number
# of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person
# who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count
# of the number of times they appear in the file. After the dictionary is produced, the program reads through
# the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

email_counts = dict()
for line in handle:
    line = line.rstrip()
    words = line.split()
    if len(words) < 1 or words[0] != "From":
        continue
    else:
        email = words[1]
        email_counts[email] = email_counts.get(email, 0) + 1

# print(email_counts)
max = 0
email_of_max = "none"
for email in email_counts:
    if email_counts.get(email, 0) > max:
        max = email_counts.get(email, 0)
        email_of_max = email
    else:
        continue

print(email_of_max + " " + str(max))


### Chapter 10: Tuples (a.k.a unmodifiable lists)
### LISTS EXCEPT () INSTEAD OF []
# I encountered errors earlier because I accidentally used () instead of [] when I intended to make a list
# Tuples can be overwritten, but not changed (immutable)

tuple1 = (1, 2, 4)
tuple1[0]
# tuple1[0] = 2  # this errors because we can't change the tuple
tuple1 = (2, 2, 4) ## this works because we can overwrite it

# We can assign multiple variables using the tuple notation (simultaneous variable assignment):
(x, y) = (4, 'fred')
print(x)
print(y)

(a, b) = (90, 80)
print(a)
print(b)

# The items() method in dictionaries returns a list of (key, value) tuples
print(email_counts.items()) # This is a list of tuple pairs

for (k,v) in email_counts.items():
    print(k, v)

# Tuples are comparable like digits, from left to right:
(1, 2, 3) < (4, 5, 6) # True, only checks 1 < 4, true

(1, 2, 3) < (1, 4, 1) # first elements, 1 = 1, so checks 2nd element, 2 < 4, so statement is True

(1, 1, 1) < (1, 1, 0) #1st and 2nd elements are equal, but 3rd element: 1 < 0 is False, so statement is False

print(sorted(email_counts.items()))
# Tuples are sorted based on the same pairwise comparison, so the 2nd element will only be compared when the first elements in two tuples are equal
# In dictionaries, each key is unique, so the sorting is only done from the first element

# Sort by value in a dictionary instead?
# Create a list of (value, key) tuples, instead of (key, value) given by dict.items()
counts_email = list()
for key, value in email_counts.items():
    counts_email.append((value, key))
print(counts_email)
counts_email = sorted(counts_email, reverse=True)
print(counts_email)
# Now we can see the 2nd element is used for sorting the emails alphabetically when their counts are the same

#### Quicker way of sorting dictionaries by value, key instead of key, value
# Above, we created a whole second list of tuples with reversed order, then sorted that list in default tuple order (left > right)

print(sorted([(v, k) for k, v in email_counts.items()], reverse = True))
# This is called list comprehension: we create a "dynamic list" of reversed tuples and sort it from highest to lowest


### LIST COMPREHENSION: https://www.w3schools.com/python/python_lists_comprehension.asp  ###

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
## List comprehension syntax:
## newlist = [expression for item in iterable if condition == True]

print(email_counts)
# Let's try to use list expression to make a new list of only the emails with counts > 1

email_counts_2plus = [(email, count) for email, count in email_counts.items() if count > 1]
print(email_counts_2plus) # this gives a list of tuples of (email, count) where count > 1

print([email for email, count in email_counts.items() if count > 1]) # now only emails are printed without counts

tup = (1, 3, 2)
sorted(tup)

data = ["armadillo", "baboon", "corn", "bobcat"]
data.sort(reverse=True)
print(data)

days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
print(days[2])


### Exercise 10.2:  Write a program to read through the mbox-short.txt and figure out the distribution by
# hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time
# and then splitting the string a second time using a colon.
# In this line, the hour is 09:  "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

hour_counts = dict()
for line in handle:
    line_words = line.rstrip().split()
    if len(line_words) < 1 or line_words[0] != "From":
        continue
    else:
        # Let's find the first colon and take the 2 numbers before the colon
        hour = line_words[5].split(":")[0]
        hour_counts[hour] = hour_counts.get(hour, 0) + 1
# print(sorted(hour_counts.items()))
for hour, count in sorted(hour_counts.items()):
    print(hour, count)