import urllib.parse

lincoln = "Four score and seven years ago."
myUrl = "http://www.bellevuecollege.edu"
testEnv = "https://shoes.bellevuecollege.edu/wpm"
c = urllib.parse.urlsplit(myUrl)
d = urllib.parse.urlsplit(testEnv)
a = lincoln.split()
b = myUrl.split()


print(a)
print(b)
print(b * 4)
print(c)
print(d)
print(d[1])
print('www' in myUrl)