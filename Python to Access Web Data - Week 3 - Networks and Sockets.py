##########################################################
###### Python for Everybody Coursera Specialization ######
######  Course #3: Using Python to Access Web Data  ######
######                  Emily Sheen                 ######
##########################################################

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

