#!/usr/bin/env python3
__author__ = "adam0954"
import json


#dictionary construction
book = {}

#sample data to verify functionality
book['Tom'] = {
    'name': 'tom',
    'address':'2120 Main Street',
    'phone' : '425-564-9999'
               }
book['Aldo'] = {
    'name': 'Aldo',
    'address':'2100 Main Street N.',
    'phone' : '206-563-9999'
               }

book['Sarah'] = {
    'name': 'Sarah',
    'address':'2112 Mockingbird Lane',
    'phone' : '425-555-9999'
               }

book['Whitney'] = {
    'name': 'Whitney',
    'address':'2006 Mockingbird Lane',
    'phone' : '425-444-9999'
               }

book['Jasmine'] = {
    'name': 'Jasmine',
    'address':'2112 Red Rd',
    'phone' : '422-555-9999'
               }


book['Taija'] = {
    'name': 'Taija',
    'address':'21122 Blue Drive N.',
    'phone' : '555-555-5555'
               }


#converts dictionary to json formatted string
data = json.dumps(book)


#writes json to file, overwriting the file each call
with open('addressbook.txt', 'w') as address_file:
    address_file.writelines(data)


#Read from File
f = open('./addressbook.txt', 'r')
address_file_read = f.read()


#load the file
if address_file_read is not None: #verify file is not empty
    try:
        json_read = json.loads(address_file_read)
        if json_read is not None:
            for people in json_read.items():
                print(people)
            print("\nNames:")
            for names in json_read.keys():
                print(names)

    except:
        "Unable to read data from file."
else:
    print("Execute the function to create the file.")


