import requests                # To send HTTP requests
from bs4 import BeautifulSoup  # To parse HTML content


# Ask the user to enter the URL of the page to scan
url = input("Please enter a url: ")


# If the URL does not start with http or https, automatically add https
if not url.startswith(("https://", "http://")):
    url = "https://" + url


# Send an HTTP GET request to the URL
response = requests.get(url)


# Get the page content as a string
txt = response.text


# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(txt, "html.parser")


# List of common CSRF token keywords to search for in form inputs
csrf_token = ["csrf", "token", "authenticity"]


# Loop through all forms on the page
for  form in soup.find_all("form"):

    # Loop through all hidden input fields in the form
    for input_tag in form.find_all("input", type="hidden"):

        # Get the name of the input field and convert to lowercase
        name = input_tag.get("name", "").lower()

        # Get the value of the input field
        value = input_tag.get("value", "")


        # Check if the input name contains any CSRF-related keyword
        if any(word in name for word in csrf_token):

            # Print the token name and value if it matches
            print(f"Token name: {name}")
            print(f"Token value: {value}")
    
    
