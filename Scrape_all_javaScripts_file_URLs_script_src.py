#import required library:
#requests --> send http request to webpage
#BeautifulSoup -->parse html webpage
import requests
from bs4 import BeautifulSoup


#ask user to enter url
url = input("Please enter a url: ")


#if url do not start with https or http then dd https 
if not url.startswith(("https://", "http://")):
    url = "https://" + url


#send http requests to target url
response = requests.get(url)

#extarct raw text from the webpage
html = response.text


#parse the text by using beautifulsoup
soup = BeautifulSoup(html, "html.parser")

#make a list to store all the url
urls = []


# Find all <script> tags that contain a 'src' attribute
for url in soup.find_all("script", src = True):

    # Extract the value of the 'src' attribute
    scripts = url["src"]

    # Ensure the src attribute is not empty
    if scripts:
        urls.append(scripts)


# Print all discovered JavaScript file URLs
print("\nJavaScript Files Found:\n")
for js in urls:
    print(js)









        
