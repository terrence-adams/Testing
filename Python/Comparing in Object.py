age = input("How old are you?: ")

# type verification
print(type(age))
# converts string to int for comparison
age = int(age)

#casting verification
print(type(age))

#checks age for membership in collection
if age in (4, 22, 18, 35):
    print("Congrats, you are the lucky winner.")
else:
    print("Sorry, you're not the winner.")

#if age is less than 20 and more than 0 conditional
if age in range (20):
    print("Sorry, you are definitely too young.")

else:
    print("Old enough to party!!")
