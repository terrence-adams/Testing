__author__ ="Terrence Adams"
#Tuple Data Structure and Methods

#empty Tuple
tupleOne = ()

print(type(tupleOne))

# non enclosed data object defaults to Tuple
tupleTwo = 5,6,89,23,56,999,10

print(tupleTwo)

# Tuple concantenation
tupleThree = tupleOne + tupleTwo

print(tupleThree)
# open file object
myTuple = open("MyTuples.txt","a")

#Loop through contents to file
for x in tupleThree:
    myTuple.write(str(x) +", ")

#close file
myTuple.close()

#smallest value in the tuple
small = min(tupleTwo)
print(small)

#largest value in tuple
big = max(tupleThree)
print(big)

tupleFour = tupleTwo * 5

print(tupleFour)