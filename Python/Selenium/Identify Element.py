__author__ ="Terrence Adams"
import unittest
from selenium import webdriver
import time
from selenium import *
from selenium.webdriver.common.keys import Keys

#Opens browser to default homepage
driver = webdriver.Chrome()
driver.get("http://www.bellevuecollege.edu")

#Searches for my name
elem = driver.find_element_by_name("txtQuery")
elem.send_keys("Terrence Adams")
elem.send_keys(Keys.RETURN)


# prints body of the page in text with html stripped out
body = driver.find_element_by_tag_name("body").text

#opens a file and writes the results to the file for further review
my_name_results = open("myNameResults.txt", "w")
my_name_results.write(body)

#Asserts my name is in the returned results.
assert "Terrence Adams" in body
#ASSERTS the page doesn't return with no results found
assert "No results found." not in driver.page_source

time.sleep(3)
driver.close()
