__author__ = "adam0954"
__version__ = "1.0.1"
import os
import selenium
import bs4


#Saves module attributes to a file with the module name.txt
def save_module_dir(module):

    the_module_name = get_module_name(module)

    with open(the_module_name + '.txt', 'w') as module_file:
        for line in dir(module):
            module_file.write(line + '\n')


#strips the module name from the object and returns it as a string
def get_module_name(module_name):
    try:
        raw_module = module_name.__str__()
        module_split = raw_module.split(sep=' ')
        module_string = module_split[1]
        my_module_name = module_string[1:-1]

        assert isinstance(my_module_name, str), "Did not convert successfully."  #Verify is a string type before returning

        return my_module_name

    except:
        print("Failed to convert the Module to a String Correctly.")




if __name__ == '__main__':
    save_module_dir(bs4)  #Pass in the actual module object not a string







