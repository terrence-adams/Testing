#! /usr/bin/env python3
__author__ = 'adam0954'

#Write format strings to file
def write_to_string_file(my_string):

	with open('./myStrings.txt','a') as string_file:
		string_file.write(my_string + '\n')


def string_to_cap(my_string):  #To Capital
	cap_string = my_string.capitalize()
	write_to_string_file(cap_string)


def string_to_center(my_string, padding, character):  #Centers Text, based on padding and extra characters
	center_string = my_string.center(padding,character)
	write_to_string_file(center_string)


def string_swapcase(my_string):  #Case Swap
	swapped_string = my_string.swapcase()
	write_to_string_file(swapped_string)


def string_upper(my_string):  #Converts to Upper
	upper_string = str.upper(my_string)
	write_to_string_file(upper_string)


def string_lower(my_string):  #Converts to Lower
	lower_string = my_string.lower()
	write_to_string_file(lower_string)


def string_to_title(my_string):  #Converts to Title format
	title_string = str.title(my_string)
	write_to_string_file(title_string)


# Function calls
if __name__ == "__main__":
	string_to_cap("words")
	string_to_center("Hour is nigh", 40, '!')
	string_swapcase("WelComETheN")
	string_swapcase("WELCOME home")
	string_upper("babyboy")
	string_lower("MAMA's boy")
	string_to_title("life goes on")
