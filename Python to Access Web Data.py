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



### Chapter 12: Networks and Sockets:  In this section we learn about the protocols that web browsers use to retrieve
# documents and web applications use to interact with Application Program Interfaces (APIs).

### HTTP: Hypertext Transfer Protocol: dominant "Application Layer Protocol" on the internet
#    Invented for the web to retrieve photos, HTML, documents, etc.
#    Extended to data in addition to documents: make a connection, request a document/data, retrieve it, close the connection
#    Retrieve web pages, e.g. http://www....
#    http://www.dr-chuck.com/page1.htm   http:// is protocol, www.dr-chuck.com is host, page1.htm is document
#    Hacking is usually done on the command line. With telnet software, you can use command line to send documents to a
#    server and hack in.  http://nmap.org.html

# Sockets allow you to "dial the phone" to connect to code or data stored on the internet
# HTTP request in Python:
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))  #data.pr4e.org is the host, and port is 80 (for internet)

cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while(True):
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())
mysock.close()

# I did not have telnet installed.  In order to install it, I used the following instructions:
# https://osxdaily.com/2018/07/18/get-telnet-macos/
# I first had to install homebrew by typing the following into Terminal:
# /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Typing "brew help" into Terminal provides some help
# ==> Next steps:
# - Run these two commands in your terminal to add Homebrew to your PATH:
#     (echo; echo 'eval "$(/usr/local/bin/brew shellenv)"') >> /Users/emilysheen/.zprofile
#     eval "$(/usr/local/bin/brew shellenv)"
# - Run brew help to get started
# - Further documentation:
#     https://docs.brew.sh

# NEXT, I typed "brew install telnet" to install telnet


### ONCE TELNET IS INSTALLED, DO THE FOLLOWING:
# In terminal on Mac, type:
# telnet data.pr4e.org 80

# Then, you must very quickly type:
# GET http://data.pr4e.org/romeo.txt HTTP/1.0

# This retrieves metadata for the requested page, and the txt file printed in Python as well.

###############################################################
#########          Networks and Sockets Quiz          #########
###############################################################

# 1.  What do we call it when a browser uses the HTTP protocol to load a file or
#     page from a server and display it in the browser?
# Answer: The request/Response Cycle

# 2.  What separates the HTTP headers from the body of the HTTP document?
# Answer: A blank line

# 3.  What must you do in Python before opening a socket?
# Answer: Import socket

# 4.  In a client-server application on the web using sockets, which must come up first?
# Answer: Client, I got this wrong by answering Server

# 5.  Which of the following is most like an open socket in an application?
# Answer: An "in-progress" phone conversation

# 6. What does the "H" of HTTP stand for?
# Answer: Hypertext

# 7. What is an important aspect of an Application Layer protocol like HTTP?
# Answer: Which application talks first?  The client or server?

# 8. What are the three parts of this URL (Uniform Resource Locator)?
# Answer: Protocol, host, and document

# 9. When you click on an anchor tag in a web page like below, what HTTP request is sent to the server?
# Answer: GET

# 10. Which organization publishes Internet Protocol Standards?
# Answer: IETF


##### Chapter 12 Assignment
# Welcome Emily Sheen from Using Python to Access Web Data
#
# Exploring the HyperText Transport Protocol
#
# You are to retrieve the following document using the HTTP protocol in a way that you can examine the HTTP Response headers.
#
# http://data.pr4e.org/intro-short.txt
# There are three ways that you might retrieve this web page and look at the response headers:
#
# Preferred: Modify the socket1.py program to retrieve the above URL and print out the headers and data.
# Make sure to change the code to retrieve the above URL - the values are different for each URL.
# Open the URL in a web browser with a developer console or FireBug and manually examine the headers that are returned.
# Enter the header values in each of the fields below and press "Submit".

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))  #data.pr4e.org is the host, and port is 80 (for internet)

cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while(True):
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())
mysock.close()

# HTTP/1.1 200 OK
# Date: Fri, 28 Apr 2023 09:01:57 GMT
# Server: Apache/2.4.18 (Ubuntu)
# Last-Modified: Sat, 13 May 2017 11:22:22 GMT
# ETag: "1d3-54f6609240717"
# Accept-Ranges: bytes
# Content-Length: 467
# Cache-Control: max-age=0, no-cache, no-store, must-revalidate
# Pragma: no-cache
# Expires: Wed, 11 Jan 1984 05:00:00 GMT
# Connection: close
# Content-Type: text/plain
# Why should you learn to write programs?
# Writing programs (or programming) is a very creative
# and rewarding activity.  You can write programs
#  for
# many reasons, ranging from making your living to solving
# a difficult data analysis problem to having fun to helping
# someone else solve a problem.  This book assumes that
# everyone needs to know how to program, and that once
# you know how to program you will figure out what you want
# to do with your newfound skills.


###############################################################
#########  12.3 - Unicode Characters and Strings      #########
###############################################################

# Characters are represented as numbers for the computer
# Different methods of converting characters to numbers, e.g. ASCII (American Standard Code for Information Interchange)
# Capital letters came first, so they are lower than lowercase
# ord function tells us the numerical code for the letter
# In the 60's and 70's, we assumed one byte was 1 character
print(ord("e"))
print(ord("E"))
print(ord("\n"))

# UNICODE: Universal way of representing thousands of characters in different languages

# UTF-16 = 2 bytes per character fixed width = more than 1 byte but still must choose
# UTF-32 = 4 bytes per character fixed width = can accommodate more characters but less total characters can fit in storage
# UTF-8 = 1-4 bytes per character = 1, 2, 3, or 4 bytes variable length per character, overlaps with ASCII
#      so for simple characters, it is the same as ASCII but you can flip if more complex characters are being used
# UTF-8 is the BEST coding for transferring data between international systems

# Python 2: Unicode and str were 2 different types in Python, so unicode type was denoted u'this_is_unicode' while
# str is "this is a string" without the "u" prefix
# Python 3 just has type str, so you don't need to switch between those types, all str are Unicode in Python 3

# Python 2: bytes and str were same, but unicode was different
# Python 3: bytes type is different, but unicode and str are both str
type(b"abc")
type("abc")
type(u"abc")

# When we receive data from the outside, we need to decode it properly. USUALLY, the data is ASCII or UTF-8.
# Since these are upwards compatible (old data is ASCII, newer data UTF-8), this is easy to deal with.

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))  #data.pr4e.org is the host, and port is 80 (for internet)

cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() # Assumes you are encoding byes to UTF-8
mysock.send(cmd)  # Sending the byes in the command

while(True):
    mydata = mysock.recv(512)
    if len(mydata) < 1:
        break
    mystring = data.decode()  ## <- in the decode() function, default is ASCII/UTF-8
    print(mystring)


# 12.4)  RETRIEVING WEB PAGES with urllib
# Since HTTP is so common, we have the urllib library to do the socket work for us and pull files from the internet
import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
for line in fhand:
    # print(line)
    print(line.decode().strip())

import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)