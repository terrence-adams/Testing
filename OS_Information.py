__author__ = "adam0954"
__version__ = "1.0.1"
import os
from pathlib import Path
from os import path
import shutil

#Clean up your code and make the necessary functions



environ_variables = dict(os.environ) # creates a dictionary of the environment variables

path = os.path.expanduser(os.getcwd())#current path to build file path string

directory_path = os.path.join(path, 'os_information') #creates directory path string


#Used for shutil.move function
#src = os.path.join(path, 'OS_Information.txt')
#destination = os.path.join(path, os.path.basename(src))



def where_am_i():
	print('Your current working directory is : ' + os.getcwd())
	print('Your home directory is at : ' + os.path.expanduser('~'))


def find_my_environment(): # single function call to generate system information
	where_am_i()
	make_os_info_dir()
	get_os_information()


def return_home(): # When lost always return home
	os.chdir(os.path.expanduser("~"))


def go_to_root(): # Go to the Source
	os.chdir('/')


def get_os_information():#Get the OS information and write it the OS_Information text file.


	with open(os.path.join(directory_path,'OS_Information.txt'), 'w') as my_os_file:
		for info in os.uname():
			my_os_file.writelines('OS Information: \n' + info + '\n')

		my_os_file.writelines('\n' + "Environment Variables:" + '\n')
		for k ,v in environ_variables.items():
			line = "{} : {}".format(k,v)
			my_os_file.write(line)
			my_os_file.write('\n')

	print("Your Operating System information can be found in the os_information directory.")


def make_os_info_dir():
	current_path = os.path.abspath(os.getcwd())  # find the current path

	absolute_path = current_path + "/os_information"  # get the full path to create the directory

	my_directory = Path(absolute_path)  # Used to verify if the directory exists already

	if my_directory.exists():

		pass

	else:
		os.mkdir(absolute_path, 0o777) #Must be in Python 3.x Friendly format to set permissions


if __name__	== '__main__':
	find_my_environment()



