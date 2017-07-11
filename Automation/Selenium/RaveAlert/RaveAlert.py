__author__ = 'adam0954'
import urllib
from urllib import request
import selenium
from selenium import webdriver
from selenium.webdriver.common import keys
import os


#creates the static url for the site under test
url = "https://shoes.bellevuecollege.edu/wpm"
#mySite = urllib.request.urlopen("https://shoes.bellevuecollege.edu/wpm")

#creates instance of the driver and browser under test
driver = webdriver.Chrome()
driver.get(url)

raveAlertMsg = driver.find_element_by_id("ravealertmessage")
raveAlertHeader = driver.find_element_by_id("ravealertheader")
#raveAlertIcon = driver.find_element_by_class_name("glyphicon glyphicon-warning-sign")
messageTitle = raveAlertMsg.find_element_by_xpath("h2")
messageBody = raveAlertMsg.find_element_by_xpath("p")

#Test case Assertions
assert raveAlertMsg.is_displayed(), "Rave Alert Message is not Shown"
assert raveAlertHeader.is_displayed(), "Rave Alert Header is not Visible"
assert messageBody.is_displayed(), "Message Body is not displayed"
assert messageTitle.is_displayed(), "Message Title is not displayed"

driver.save_screenshot('RavealertChrome.png')


driver.close()


#creates instance of the driver and browser under test
#Firefox Test Instance
driver2 = webdriver.Firefox()
driver2.get(url)

raveAlertMsg = driver2.find_element_by_id("ravealertmessage")
raveAlertHeader = driver2.find_element_by_id("ravealertheader")
#raveAlertIcon = driver.find_element_by_class_name("glyphicon glyphicon-warning-sign")
messageTitle = raveAlertMsg.find_element_by_xpath("h2")
messageBody = raveAlertMsg.find_element_by_xpath("p")

#Test case Assertions
assert raveAlertMsg.is_displayed(), "Rave Alert Message is not Shown"
assert raveAlertHeader.is_displayed(), "Rave Alert Header is not Visible"
assert messageBody.is_displayed(), "Message Body is not displayed"
assert messageTitle.is_displayed(), "Message Title is not displayed"

driver2.save_screenshot('RavealertFirefox.png')


driver2.close()



#creates instance of the driver and browser under test
#IE Test Instance
#Must declare IE driver by file path
driver3 = webdriver.Ie("C:\Python34\Scripts\IEDriverServer.exe")
driver3.get(url)

raveAlertMsg = driver3.find_element_by_id("ravealertmessage")
raveAlertHeader = driver3.find_element_by_id("ravealertheader")
#raveAlertIcon = driver.find_element_by_class_name("glyphicon glyphicon-warning-sign")
messageTitle = raveAlertMsg.find_element_by_xpath("h2")
messageBody = raveAlertMsg.find_element_by_xpath("p")

#Test case Assertions
assert raveAlertMsg.is_displayed(), "Rave Alert Message is not Shown"
assert raveAlertHeader.is_displayed(), "Rave Alert Header is not Visible"
assert messageBody.is_displayed(), "Message Body is not displayed"
assert messageTitle.is_displayed(), "Message Title is not displayed"

driver3.save_screenshot('RavealertIE.png')


driver3.close()