#import required libraries
#for sending http requests
#For parsing html
#for extracting domain from url
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

#ask user to enter a target url
url = input("Please enter your url: ")


# Send HTTP GET request to fetch webpage content
get = requests.get(url)


# Extract raw HTML from the response
html = get.text


# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html , "html.parser")


# Create a set to store unique domain names
domain = set()


# Find all <a> tags that contain an href attribute
for domains in soup.find_all("a", href=True):


    # Extract the href value
    href = domains["href"]

    # Parse the URL
    parse = urlparse(href)

    # Extract the domain name
    f_domain = parse.netloc


    # Add domain to set if it's not empty
    if f_domain:
        domain.add(f_domain)

# Print all unique domains found
print("Here is your domain: ",domain)
