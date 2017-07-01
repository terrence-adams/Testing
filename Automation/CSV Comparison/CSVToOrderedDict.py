#!/usr/bin/env python3
__author__ = "adam0954"
import csv
import collections

#Default definition for terms
terms_dict = collections.OrderedDict()
index = 0
suggested_list = []

#Populates the dictionary from the CSV file of Terms
with open('definitions.csv', 'r') as definitions:
    reader = csv.reader(definitions)
    for k,v1,v2 in reader:
        terms_dict[k] =(v1,v2)


#Creates a list of the suggested terms for comparisson
with open('suggested.csv', 'r') as suggested:
    suggested_reader = csv.reader(suggested)

    #Takes the iterated value and converts it to string from the default list value
    for term in suggested_reader:
        suggested_list.append(''.join(term))


#iterates over terms key and compares with suggested value
for k in terms_dict.keys():
    suggested_term = suggested_list[index]

    if k == suggested_term:
        print("My Terms value is",k)
        print("True")

    else:
        print("My Terms value is", k)
        print("False")

    index +=1  #advances the inxed value within the list