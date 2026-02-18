# Import required libraries:
# requests      -> for sending HTTP requests to web pages
# BeautifulSoup -> for parsing HTML content
import requests
from bs4 import BeautifulSoup

# Ask user to enter the target URL
url = input("Please enter a url: ")


# Ensure URL has a scheme (http:// or https://)
if not url.startswith(("https://", "http://")):
    url = "https://" + url


# Send HTTP GET request to fetch the webpage content
get = requests.get(url)


# Extract the raw HTML text from the get
txt = get.text


# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(txt , "html.parser")


# Create a list to store all input field details
inputs = []


# Find all <input> tags on the page
for tag in soup.find_all("input"):

    # Extract useful attributes from the input field
    # 'type'   -> type of input (text, password, email, etc.)
    # 'name'   -> name attribute (used in forms to identify fields)
    # 'id'     -> id attribute (unique identifier in HTML)
    input_type = tag.get("type")
    input_name = tag.get("name")
    input_id = tag.get("id")


    # Store input field details in a dictionary and append to the list
    inputs.append({
        "type": input_type,
        "name": input_name,
        "id": input_id
        })

# Print all input fields found on the page
print("Input fields found: ")

for i in inputs:
    print(i)
