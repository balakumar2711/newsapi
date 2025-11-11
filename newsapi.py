import requests as r
from send_email import send_email

#The API key from the News API
API_KEY= "976bffa6cc5c44a592e042fef57314c"

#The URL that needs to be checked
URL = ("https://newsapi.org/v2/everything?" \
       "q=tesla&" \
       "from=2025-10-11&" \
       "sortBy=publishedAt&" \
       "apiKey=976bffa6cc5c44a592e042fef57314ce&language=en")

#Make request
request = r.get(URL)

#Get a dictionary with data
content = request.json()

#print(content)

#Declaring an empty string that will be updated to the send_email function argument
message = ""

#Access the items inside the dictionary
for article in content["articles"]:
    #Update the message body with the updated message
    if article["title"] is not None and article["description"] is not None:
        message = message + article["title"] + "\n" + article["description"] + 2*"\n"

#To encode the value to prevent range errors
message = message.encode("utf-8")

#Use the send_email function to send the message
send_email(message)