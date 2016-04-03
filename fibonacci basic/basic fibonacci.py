__name__ = "fibonacci basic"
__author__ = "Terrence Adams"

a = 1;
b = 2;
c = 0;

#print initial numbers
print(a,b)

# print sequence in defined range
for x in range(0,25):
    c = a + b
    a = b
    b = c
    print(c)



