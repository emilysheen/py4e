##########################################################
###### Python for Everybody Coursera Specialization ######
######  Course #3: Using Python to Access Web Data  ######
######                  Emily Sheen                 ######
##########################################################

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


### Example Code file: urllib1.py
import urllib.request

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())

### Example Code File: urlwords.py
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)

### Chapter 12.5: Parsing Web Pages
### We can write a Python program that pretends to be a browser and pulls web pages / data
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
url = input("Enter URL: ")  # http://www.dr-chuck.com/page1.htm
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))


### Example Code File: urllinks.py

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))


### Quiz Week 4
# 1)  Which of the following Python data structures is most similar to the value returned in this line of Python:
# Ans: file handle
x = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
type(x)

# 2) In this Python code, which line actually reads the data?
# mysock.recv()
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()

# 3) Which of the following regular expressions would extract the URL from this line of HTML:
# <p>Please click <a href="http://www.dr-chuck.com">here</a></p>
# Answer: href="(.+)"

# 4) In this Python code, which line is most like the open() call to read a file:
# Answer: mysock.connect()

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()

# 5) Which HTTP header tells the browser the kind of document that is being returned?
# Answer: Content-Type

# 6) What should you check before scraping a web site?
# Answer: That the website allows scraping

# 7) What is the purpose of the BeautifulSoup Python library?
# Answer: It repairs and parses HTML to make it easier for a program to understand

# 8) What ends up in the "x" variable in the following code:
# Answer:  A list of all the anchor tags (<a..) in the HTML from the URL
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
x = soup('a')
type(x)
print(x)

# 9) What is the most common Unicode encoding when moving data between systems?
# Answer: UTF-8

# 10) What is the decimal (Base-10) numeric value for the upper case letter "G" in the ASCII character set?
ord('G')
# Answer: 71

# 11) What word does the following sequence of numbers represent in ASCII:
# 108, 105, 110, 101

chr(108)
chr(105)
chr(110)
chr(101)

# Answer: line

# 12) How are strings stored internally in Python 3?
x = str("poo")
type(x)
type(str(u"poo"))
# Answer: Unicode

# 13) When reading data across the network (i.e. from a URL) in Python 3, what method must be used to convert it
# to the internal format used by strings?
# Answer: decode()


### Week 4 Assignment:
#  Based on the urllink2.py file, printed below:

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)


##### In this assignment you will write a Python program similar to http://www.py4e.com/code3/urllink2.py (above)
# The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers
# and compute the sum of the numbers in the file.

# We provide two files for this assignment. One is a sample file where we give you the sum for your testing
# and the other is the actual data you need to process for the assignment.

# Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_1804705.html (Sum ends with 79)
# You do not need to save these files to your folder since your program will read the data directly from the URL.
# Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.

### DATA FORMAT
# The file is a table of names and comment counts. You can ignore most of the data in the file except for
# lines like the following:

# <tr><td>Modu</td><td><span class="comments">90</span></td></tr>
# <tr><td>Kenzie</td><td><span class="comments">88</span></td></tr>
# <tr><td>Hubert</td><td><span class="comments">87</span></td></tr>

# You are to find all the <span> tags in the file and pull out the numbers from the tag and sum the numbers.
# Look at the sample code provided. It shows how to find all of a certain kind of tag,
# loop through the tags and extract the various aspects of the tags.
# You need to adjust this code to look for span tags and pull out the text content of the span tag,
# convert them to integers and add them up to complete the assignment.

# Sample Execution

# $ python3 solution.py
# Enter - http://py4e-data.dr-chuck.net/comments_42.html
# Count 50
# Sum 2...

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags

tags = soup('span')
num_comments = []
for tag in tags:
    # Look at the parts of a tag
    num_comments.append(int(tag.contents[0]))
# print(num_comments)
print("Count " + str(len(num_comments)))
print("Sum " + str(sum(num_comments)))


# Week 4 Assignment 2: Following Links in Python

# In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py.
# The program will use urllib to read the HTML from the data files below, extract the href= values from the anchor tags,
# scan for a tag that is in a particular position relative to the first name in the list,
# follow that link and repeat the process a number of times and report the last name you find.

# We provide two files for this assignment. One is a sample file where we give you the name for your testing
# and the other is the actual data you need to process for the assignment

# Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
# Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times.
# The answer is the last name that you retrieve.
# Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
# Last name in sequence: Anayah

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
links = [tags[2].get('href', None)]
names = [tags[2].contents[0]]
# for tag in tags:
#     print(tag.get('href', None))
#     print('TAG:', tag)
#     print('URL:', tag.get('href', None))
#     print('Contents:', tag.contents[0])
#     print('Attrs:', tag.attrs)

# Must click the link to get the next name 4 times
for i in range(3):
    print(i)
    url = links[i]
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    links.append(tags[2].get('href', None))
    names.append(tags[2].contents[0])
print(links)
print(names)
print(names[len(names)-1])

# Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Torran.html
# Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times.
# The answer is the last name that you retrieve.
# Hint: The first character of the name of the last page that you will load is: C
# Strategy:
# The web pages tweak the height between the links and hide the page after a few seconds to make it difficult
# for you to do the assignment without writing a Python program. But frankly with a little effort and patience
# you can overcome these attempts to make it a little harder to complete the assignment without writing a
# Python program. But that is not the point. The point is to write a clever Python program to solve the program.
#
# Sample execution
#
# Here is a sample execution of a solution:
#
# $ python3 solution.py
# Enter URL: http://py4e-data.dr-chuck.net/known_by_Fikret.html
# Enter count: 4
# Enter position: 3
# Retrieving: http://py4e-data.dr-chuck.net/known_by_Fikret.html
# Retrieving: http://py4e-data.dr-chuck.net/known_by_Montgomery.html
# Retrieving: http://py4e-data.dr-chuck.net/known_by_Mhairade.html
# Retrieving: http://py4e-data.dr-chuck.net/known_by_Butchi.html
# Retrieving: http://py4e-data.dr-chuck.net/known_by_Anayah.html
# The answer to the assignment for this execution is "Anayah".

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter URL: ')  # http://py4e-data.dr-chuck.net/known_by_Fikret.html
# count = int(input("Enter Count: "))  # Count = 7
# position = int(input("Enter position: ")) # Position = 18
url = "http://py4e-data.dr-chuck.net/known_by_Torran.html"
count = 7
position = 18
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
names = ["Fikret"]
links = [url]

for i in range(count):
# Retrieve all of the anchor tags
    new_url = links[i]
    new_html = urllib.request.urlopen(new_url, context=ctx).read()
    print("Retrieving: "+ new_url)
    soup = BeautifulSoup(new_html, 'html.parser')
    # print(i)
    tags = soup('a')
    links.append(tags[position - 1].get('href', None)) # links[i] = ith count of 18th link
    names.append(tags[position - 1].contents[0])  # names[i] = ith count of 18th name
    if i == count - 1:
        print("Retrieving: "+tags[position - 1].get('href', None))
print("The answer to the assignment for this execution is \"" + names[len(names)-1]+"\".")

