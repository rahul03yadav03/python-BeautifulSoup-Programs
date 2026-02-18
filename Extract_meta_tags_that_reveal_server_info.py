#import required library
#beautifulsoup --> used to parse html content
#requests --> used to parse html content
import requests
from bs4 import BeautifulSoup


#ask user to enter url
url = input("Please enter your url: ")


#if url do not start with htttp or https then add htpps
if not url.startswith(("https://", "http://")):
    url = "https://" + url


#send http request to the website
response = requests.get(url)


#Extract htmp content from the response
txt = response.text


#Parse html using BeautifulSoup
soup = BeautifulSoup(txt , "html.parser")

print("\nInteresting Meta Tag:\n")


#Find all <meta> tags in the webpage
for tag in soup.find_all("meta"):

    #Get the 'name' attribute of the meta data
    name = tag.get("name")

    #get the  'content' attribut of the meta tag
    content = tag.get("content")

    
    #only print meta tags that conatin bot name and content
    if name and content:
        print(f"{name} ---> {content}")
