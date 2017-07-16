import os

#List all files in current directory and subfolders
def list_directory_files():
    current_directory = os.getcwd()

    for current, dir, files in os.walk(current_directory, topdown=True):
        print(files)

if __name__ == '__main__':
    list_directory_files()