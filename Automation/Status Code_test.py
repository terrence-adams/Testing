#! /usr/bin/env python3

__author__ ="adam0954"
import urllib
from urllib import request
import requests
import http.client


#allows input from user to dictate the url
#url = input("Enter the url including the http://)


# Using urllib to fetch status of server
url = "http://www.bellevuecollege.edu"

# page request
req = request.urlopen(url)

#reads content to html
html = req.read()

# print header
print(req.info())

#print Code using properties and method
print("The status code using UrlLib: " ,req.getcode())
print("The status code using UrlLib: ", req.code)
print("The status code using UrlLib: ", req.status)


"""
This shows two other ways to get the headers from a website in Python
using requests Module and the HTTPClient


"""

#Status code using Requests module
r = requests.get(url)

print("The status code using the Requests module: ", r.status_code)
#print(r.headers) prints the headers for the response object



# Status code using HttpClient
#Uses http:// by default
connection = http.client.HTTPConnection("www.bellevuecollege.edu:80")
connection.request("GET","/")

myResponse = connection.getresponse()

print("Status Code using HTTPClient",myResponse.status, myResponse.reason)

