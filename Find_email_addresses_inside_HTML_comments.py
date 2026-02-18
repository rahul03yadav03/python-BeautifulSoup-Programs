# Import required libraries
# requests ---> For sending HTTP requests to the webpage
# BeautifulSoup, Comment ---> For parsing HTML and extracting HTML comments
# re --- > For using regular expressions to find email patterns
import requests
from bs4 import BeautifulSoup, Comment
import re


# Ask the user to enter a URL
url = input("Please enter a URL: ")


# Ensure the URL starts with "http://" or "https://"
if not url.startswith(("https://", "http://")):
    url = "https://" + url


# Send an HTTP GET request to fetch the webpage content
response = requests.get(url)


# Extract the raw HTML content from the response
html = response.text


# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html, "html.parser")


# Find all HTML comments in the page
# 'Comment' is a special object type in BeautifulSoup
comments = soup.find_all(string=lambda text: isinstance(text, Comment))
pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'


# Loop through each comment and search for email addresses
for comment in comments:

    # Find all emails in the comment
    matches = re.findall(pattern, comment)

    # Loop through all found emails
    for match in matches:

        # Print each email address
        print(match)






        
