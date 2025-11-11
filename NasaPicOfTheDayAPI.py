import requests

import streamlit as st

API_KEY = "zGgqAfqzHw4ETABlY8eEaxhnrrROAxAc3R0JUYkZ"

URL = ("https://api.nasa.gov/planetary/apod?" \
       "api_key=zGgqAfqzHw4ETABlY8eEaxhnrrROAxAc3R0JUYkZ")

#Getting the URL
request1 = requests.get(URL)

#Converting the URL to data
data = request1.json()

print(data)

title = data["title"]
image_url = data["url"]
description = data["explanation"]

#Download the image
image_filepath = "img.png"
response2 = requests.get(image_url)
with open(image_filepath, 'wb') as file:
    file.write(response2.content)

st.title(title)
st.image(image_filepath)
st.write(description)