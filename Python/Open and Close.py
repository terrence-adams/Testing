myName = input("What's your name? ")
myFile = open("myName.txt", "a+")
myFile.write(myName)
myFile.close()