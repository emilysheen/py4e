##########################################################
###### Python for Everybody Coursera Specialization ######
######  Course #3: Using Python to Access Web Data  ######
######                  Emily Sheen                 ######
##########################################################

### Chapter 11: Regular Expressions
### MOST VALUABLE RESOURCE: https://regex101.com/  this website allows you to write a regex and double check
### the regex is correct using any example text

### REGULAR EXPRESSION KEY
#    ^         matches beginning of the line
#    $         matches end of the line
#    .         matches any character (occurring 1 time)
#    \s        matches whitespace
#    \S        matches any non-whitespace character (note this is capital S)
#    *         matches the previous token between 0 and inf times, as many times as possible, giving back as needed (greedy)
#    *?        matches the previous token between 0 and inf times, as few times as possible, expanding as needed (lazy)
#    +         matches the previous token between 1 and inf times, as many times as possible, giving back as needed (greedy)
#    +?        matches the previous token between 1 and inf times, as few times as possible, expanding as needed (lazy)
#    [aeiou]   matches a single character in the listed set (in this example, vowels)
#    [^XYZ]    matches a single character not in the listed set
#    [a-z0-9]  matches a character in the ranges of a-z or 0-9
#    (         indicates start of string extraction
#    )         indicates end of string extraction


import re   # this is the regular expression package in Python
fh = open('mbox-short.txt')
emails = list()
for line in fh:
    line = line.rstrip()
    if re.search("^From:", line):
        # print(line)
        email = re.search(r"From: (.*@.*)", line)[1]  # the [1] pulls the first group
        # print(email)
        emails.append(email)
print(emails)

fh = open('mbox-short.txt')
words = list()
for line in fh:
    line = line.rstrip().split()
    for word in line:
        words.append(word)
print(words)

emails = re.findall(r".*@.*", words)


x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)


#### Week 2 Assignment: Finding Numbers in a Haystack
# In this assignment you will read through and parse a file with text and numbers.
# You will extract all the numbers in the file and compute the sum of the numbers.

# Data Files:
# We provide two files for this assignment. One is a sample file where we give you the sum for your testing
# and the other is the actual data you need to process for the assignment.

# Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445,833)
# Actual data: http://py4e-data.dr-chuck.net/regex_sum_1804703.txt (There are 84 values and the sum ends with 256)
# These links open in a new window. Make sure to save the file into the same folder as you will be writing your
# Python program. Note: Each student will have a distinct data file for the assignment - so only use your own data
# file for analysis.

# Data Format
# The file contains much of the text from the introduction of the textbook except that random numbers are inserted
# throughout the text. Here is a sample of the output you might see:

# Why should you learn to write programs? 7746
# 12 1929 8827
# Writing programs (or programming) is a very creative
# 7 and rewarding activity.  You can write programs for
# many reasons, ranging from making your living to solving
# 8837 a difficult data analysis problem to having fun to helping 128
# someone else solve a problem.  This book assumes that
# everyone needs to know how to program ...

# Handling The Data
# The basic outline of this problem is to read the file, look for integers using the re.findall(),
# looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers
# and summing up the integers.

# Let's make sure we compute the correct sum for regex_sum_42.txt:
# Assume spaces separate different numbers
# hand = open("regex_sum_42.txt", "r")
import re
hand = open("regex_sum_42.txt", "r")
tot = 0
cnt = 0
for line in hand:
    ints = re.findall('[0-9]+', line)
    for i in ints:
        tot = tot + int(i)
        cnt = cnt + 1
print(cnt)  ### 90 count is correct
print(tot)  ### 445833 is correct

import re
hand = open("regex_sum_1804703.txt", "r")
tot = 0
for line in hand:
    ints = re.findall('[0-9]+', line)
    for i in ints:
        tot = tot + int(i)
print(tot)  ### 415256 ends in the right 3 digits

# THIS DOES NOT WORK AND SEEMS TO BE STUCK...I HAVE NO IDEA WHY
# import re
# hand = open("regex_ex1.txt", "r")
# ints = list()
# for line in hand:
#     ints = re.findall(r"[0-9]+", line)
#     # print(ints)
#     # The part below doesn't seem to be working
#     if len(ints) < 1:
#         continue
#     else:
#         for the_int in ints:
#             this_int = int(the_int)
#             ints.append(this_int)
# print(ints)

# THIS WORKS FOLLOWING SAME ATTEMPTED LOGIC AS ABOVE...SOMETHING IS MAKING THE COMPUTER SLOW IN THE ABOVE.
ints_list = list()
for i in ['12', '1929', '8827']:
    try:
        int_i = int(i)
    except ValueError:
        continue
    ints_list.append(int_i)
print(ints_list)
print(sum(ints_list))

# Optional: Just for Fun
# There are a number of different ways to approach this problem. While we don't recommend trying to write the most
# compact code possible, it can sometimes be a fun exercise. Here is a a redacted version of two-line version of this
# program using list comprehension:
#
# Python 2
# import re
# print sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] )
#
# Python 3:
# import re
# print( sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] ) )
# Please don't waste a lot of time trying to figure out the shortest solution until you have completed the homework.
# List comprehension is mentioned in Chapter 10 and the read() method is covered in Chapter 7.

import re
fhand = open("regex_sum_1804703.txt", "r")
inp = fhand.read() # concatenates all of the txt file into a single string
print(inp)
print(open("regex_sum_1804703.txt", "r").read()) # prints concatenation of the txt file, same as print(inp)
print(re.findall('[0-9]+', inp)) # finds all integer matches in the concatenated string of the text file
## newlist = [expression for item in iterable if condition == True]
print( sum( [ int(x) for x in re.findall('[0-9]+',open("regex_sum_1804703.txt", "r").read()) ] ) )
