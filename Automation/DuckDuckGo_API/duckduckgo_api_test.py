#!/usr/bin/env python3
__author__ = 'adams0954'
__version__ = '1.0.0'

import json
import _json
import requests
from requests import Request


#DuckDuckGo's api parameters
searh_term = 'wookies'
duck_url = 'http://api.duckduckgo.com/?q='
format = '&format=json'
prettify = '&pretty=1'
#q = 'q'
no_html = '&no_html'
format_xml='&format=xml'





#provides a data dump of the json file unfiltered
def duckduckgo_search():
    my_request = requests.get(duck_url + searh_term+format+prettify)

    #print to screen to verify correct url configuration
    #print(duck_url+ searh_term + format)

    jsonData = json.loads(my_request.text) #converts request to text to parse

    with open(searh_term + '.txt', 'a') as search_file:
        json.dump(jsonData,search_file,sort_keys=True, indent=2)



#filters the data in json format to the file based on
def duckduckgo_search_filtered():
    my_request = requests.get(duck_url + searh_term+format+prettify)

    jsonData = json.loads(my_request.text)
    filtered_results = jsonData['Infobox']['meta']


    with open(searh_term + '.txt', 'w+') as search_filtered_file:
        json.dump(filtered_results,search_filtered_file,sort_keys=True,indent=2)

    with open(searh_term +'_json_items.txt', 'w') as json_items_file:
        for items in jsonData.items():
            json_items_file.write(str(items)+'\n')


#function to allow for user provided term to search for
def duckduckgo_new_search(new_term):

    if new_term != None and isinstance(new_term,str):  #validate type and !None

        try:
            searh_term = new_term

            my_response = requests.get(duck_url + searh_term + format + prettify)

            # print to screen to verify correct url configuration
            #print(duck_url + searh_term + format)

            jsonData = json.loads(my_response.text)  #

            with open(new_term + '.txt', 'w+') as search_file:
                json.dump(jsonData, search_file, sort_keys=True, indent=2)

        except:
            print("Unable to complete your search as requested.")
    else:
        print("You did not provide a proper value to search for.")





if __name__ == '__main__':
    duckduckgo_search()
    duckduckgo_search_filtered()
    duckduckgo_new_search('trees')

