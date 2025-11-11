import requests as r

#The API key from the News API
API_KEY= "976bffa6cc5c44a592e042fef57314c"

#The URL that needs to be checked
URL = ("https://newsapi.org/v2/everything?" \
       "q=tesla&from=2025-10-11&sortBy=publishedAt&" \
       "apiKey=976bffa6cc5c44a592e042fef57314ce")

#Make request
request = r.get(URL)

#Get a dictionary with data
content = request.json()

#Access the items inside the dictionary
for article in content["articles"]:
    print(article["title"])
    print(article["author"])