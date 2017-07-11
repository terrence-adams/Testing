#! /usr/bin/env python3
import selenium
import unittest
from selenium import webdriver
import time
__author__ ="adam0954"


class MyUnitTest(unittest.TestCase):


    root_url ="http://www.bellevuecollege.edu"
    driver = webdriver.Chrome()

    myTitle = ""
    current_url = ""
    myUrls = [root_url]


    #Set up of Browser
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.root_url)
        self.myTitle = self.driver.title
        self.assertEquals(self.myTitle, "Bellevue College, Washington", "Failed")
        self.driver.close()





    #class method
    @classmethod
    def visit(self, path):
        self.driver.get(self.root_url + path)
        current_url = self.driver.current_url
        self.myUrls.append(current_url)


    @classmethod
    def test_multiple_site_visits(self):
        time.sleep(3)
        self.driver.refresh()
        self.visit("/classes")
        time.sleep(3)
        self.driver.refresh()
        self.visit("/programs")
        time.sleep(3)
        self.driver.refresh()
        self.visit("/enrollment")
        time.sleep(3)
        self.driver.refresh()
        self.visit("/resources")
        time.sleep(3)
        self.driver.refresh()
        self.visit("/campuslife")
        time.sleep(3)
        self.driver.refresh()
        self.visit("/about")
        time.sleep(3)
        self.driver.refresh()
        self.driver.close()










#provides a command-line interface to the test script
if __name__ == '__main__':
    unittest.main()

