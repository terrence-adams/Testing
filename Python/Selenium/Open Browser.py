import unittest
from selenium import webdriver
import time
import selenium


__author__ ="Terrence Adams"

#opens browser in Chrome
driver = webdriver.Chrome()
try:
    #Mayflower Homepage Test site
    driver.get("http://www.bellevuecollege.edu")

    mayflower = driver.title

    print(mayflower)

except ValueError:

    print("Unable to load requested browser.")

#keeps the browser open for 5 seconds
time.sleep(5)

# Validates Title of the Page is as expected
assert mayflower == "Bellevue College, Washington"

# Assert Bellevue College is in the Title
assert "Bellevue College" in driver.title

#Closes browser after time expires
driver.close()
