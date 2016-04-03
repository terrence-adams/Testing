class WebFetch:
    'Returns urls and data'
    import http.client
    import urllib.request
    from urllib import parse
    import random




    url = ''
    fileName = ""
    welcomeMessage = input("Please enter the url you wish returned: ")

    url = welcomeMessage.lower()
    fileName = url[11:17]+str(random.randint(1,9))+".txt"
    htmlCode = open(fileName, 'a+')





    response = urllib.request.urlopen(url)
    a = response.read()
    returned = urllib.request.Request(url)
    decoded = a.decode(encoding="UTF8")
    htmlCode.write(decoded)


    htmlCode.close()
