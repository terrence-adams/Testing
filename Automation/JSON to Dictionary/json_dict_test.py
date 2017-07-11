#!/usr/bin/env python3
__author__ = "adam0954"
import json
import collections
from collections import OrderedDict


#dictionary construction
book = {} #default dictionary type
book = OrderedDict(book) #Ordered Dict to maintain order of items and values


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

#Creates the file to be used for the other functions
def create_address_book():
    # converts dictionary to json formatted string
    data = json.dumps(book)

    # writes json to file, overwriting the file each call
    with open('addressbook.txt', 'w') as address_file:
        address_file.writelines(data)


#reads from the addressbook.txt file and creates unique files from the data
def write_address_book_to_file():

    try:
        # Read from File
        f = open('./addressbook.txt', 'r')
        address_file_read = f.read()

        # load the file
        if address_file_read is not None:  # verify file is not empty
            try:
                json_read = json.loads(address_file_read)
                if json_read is not None:
                    for people in json_read.items():
                        print(people)
                    print("\nNames:")
                    for names in json_read.keys():
                        print(str.capitalize(names))
                    print("\n")

                    print("Name and Number:")
                    with open('names and numbers.txt', 'w') as nan_file:
                        for value in json_read.values():
                            number = value['phone']
                            name = str.capitalize(value['name'])
                            entry = name + ": \n" + number + "\n"
                            print(entry)
                            nan_file.write(entry)


            except Exception as ex:
                print("Unable to read data from file.", ex) #if the file is unreadable, throw error
        else:
            create_address_book()
            print("We have created the file, please try again.")
    except Exception as ex:
        create_address_book()
        print("We have created the file, please try again.", ex)


def address_book_lookup(find_name):


    #Assertion test of contents
    try:
        assert (find_name in book), "Name not found."
        print("Entry Found:")
        for data in book[find_name].values():
            print(data)
            '''
            The current display is random due to the nature of built-in Python Dictionary objects.
            An upgrade to 3.6, will resolve this issue, the items will maintain their insertion order as of 3.6

            '''


    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    write_address_book_to_file()
    address_book_lookup("Taija")

