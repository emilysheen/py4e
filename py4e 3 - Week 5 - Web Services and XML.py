##########################################################
###### Python for Everybody Coursera Specialization ######
######  Course #3: Using Python to Access Web Data  ######
######                  Emily Sheen                 ######
##########################################################


### Chapter 13: Web Services and XML

# 13.1) API's: Application Programming Interface: In order to send information across the web in an intelligible format
# Serialization: xml and json put data into intelligible format for interpretation by receiver
# De-serialization: decode the data into the desired format on the receiver end

# Java/Python people can argue about how to best code/decode data, but json and xml meet in the middle
# XML = eXtensible Markup Language, purpose to help information systems share structured data
#      subset of Standard Generalized Markup Language (SGML, more complex)

# XML Example: start tags and end tags for groups of info
# Start tag, e.g. <person>, <name>, <phone> is beginning of information, no forward slash (/)
# End tag: end of information, contains forward slash /, e.g. </name>, </phone>, </person>
# Text content: information contained within the tag, e.g. Emily, 987-123-4567
# Attribute: keyword/value tags on the opening tags of XML: e.g. type="intl", hide="yes", use double quotes here ""
# Self closing tag: e.g. <email hide=yes/>, empty text area
# <person>
#     <name>Emily</name>
#     <phone type="intl">+1 987-123-4567</phone>
#     <email hide="yes"/>
# </person>

# ~ Each Node can have many attributes, but only one text field
# Can think of the nodes as branches on a tree or folders on your computer (paths)

# XSD == XML Schemas from W3C (suffix .xsd) (but others exist)
# Can set min or max # occurrences of various tags, other constraints on data


## Parsing XML files, Example: xml1.py
import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))


## Parsing XML files, Example: xml2.py
# findall method gives all tags in a list (not a list of strings)

import xml.etree.ElementTree as ET

input = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))

for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get('x'))

### Quiz Chapter 13: eXtensible Markup Language

# 1) What is the name of the Python 2.x library to parse XML data?
# Answer: xml.etree.ElementTree

# 2) What is the method to cause Python to parse XML that is stored in a string?
# Answer: fromstring()

# 3) In this XML, which are the "complex elements"?
# <people>
#     <person>
#        <name>Chuck</name>
#        <phone>303 4456</phone>
#     </person>
#     <person>
#        <name>Noah</name>
#        <phone>622 7421</phone>
#     </person>
# </people>
# Answer: people, person

# 4) In the following XML, which are attributes?
# <person>
#   <name>Chuck</name>
#   <phone type="intl">
#      +1 734 303 4456
#   </phone>
#   <email hide="yes" />
# </person>
# Answer: type, hide

# 5) In the following XML, which node is the parent node of node e?
# <a>
#   <b>X</b>
#   <c>
#     <d>Y</d>
#     <e>Z</e>
#   </c>
# </a>
# Answer: node c

# 6) Looking at the following XML, what text value would we find at path "/a/c/e"
# <a>
#   <b>X</b>
#   <c>
#     <d>Y</d>
#     <e>Z</e>
#   </c>
# </a>
# Answer: Z

# 7) What is the purpose of XML Schema?
# Answer: To establish a contract as to what is valid XML

# 8) If you were building an XML Schema and wanted to limit the values allowed in an xs:string
# field to only those in a particular list, what XML tag would you use in your XML Schema definition?
# Answer: xs:enumeration

# 9) What does the "Z" mean in this representation of a time:
#  2002-05-30T09:30:10Z
# Answer: Z is UTC time, suffix of "-6:00" would indicate UTC - 6 hours

# 10) Which of the following dates is in ISO8601 format?
# Answer: 2002-05-30T09:11:55.678Z, basically just biggest to smallest time unit: year, to milliseconds

########################################################################################################################
### Chapter 13 Assignment: Extracting Data from XML
# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py.
# The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract
# the comment counts from the XML data, compute the sum of the numbers in the file.

# We provide two files for this assignment. One is a sample file where we give you the sum for your testing
# and the other is the actual data you need to process for the assignment.

# Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_1804707.xml (Sum ends with 60)
# You do not need to save these files to your folder since your program will read the data directly from the URL.
# Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.

# Data Format and Approach
# The data consists of a number of names and comment counts in XML as follows:
#
# <comment>
#   <name>Matthias</name>
#   <count>97</count>
# </comment>
# You are to look through all the <comment> tags and find the <count> values sum the numbers.
# The closest sample code that shows how to parse XML is geoxml.py. But since the nesting of the elements
# in our data is different than the data we are parsing in that sample code you will have to make
# real changes to the code.
# To make the code a little simpler, you can use an XPath selector string to look through the entire tree
# of XML for any tag named 'count' with the following line of code:
#
# counts = tree.findall('.//count')
# Take a look at the Python ElementTree documentation and look for the supported XPath syntax for details.
# You could also work from the top of the XML down to the comments node and then loop through the child nodes
# of the comments node.   https://docs.python.org/3/library/xml.etree.elementtree.html

# Sample Execution
# $ python3 solution.py
# Enter location: http://py4e-data.dr-chuck.net/comments_42.xml
# Retrieving http://py4e-data.dr-chuck.net/comments_42.xml
# Retrieved 4189 characters
# Count: 50
# Sum: 2...

import xml.etree.ElementTree as ET
# Let's try using urllib to pull all of the text in the .xml page
import urllib.request, urllib.parse, urllib.error

# url = input("Enter location: ")
# url = "http://py4e-data.dr-chuck.net/comments_42.xml"
url = "http://py4e-data.dr-chuck.net/comments_1804707.xml"
xml = urllib.request.urlopen(url).read()
print("Retrieved " + str(len(xml)) + " characters")
tree = ET.fromstring(xml)
counts = tree.findall('.//count')
print("Count: " + str(len(counts)))
counts_ints = []
for item in counts:
    counts_ints.append(int(item.text))
print("Sum: " + str(sum(counts_ints)))