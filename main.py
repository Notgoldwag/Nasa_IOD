import requests
import streamlit as st
from PIL import Image

api_key = "0rHhAEmu0f6UGyAKj0Hd1h4CY5NbjgIopDeIhtFQ"

url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

request = requests.get(url)
content = request.json()


title = content["title"]
image_url = content["url"]
explanation = content["explanation"]

image_path = "iod.png"
response_img = requests.get(image_url)

with open(image_path, "wb") as file:
    file.write(response_img.content)

st.title(title)
st.image(image_path)
st.text(explanation)



