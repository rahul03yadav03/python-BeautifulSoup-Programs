import requests                      # Used to send HTTP requests to websites

from bs4 import BeautifulSoup       # Used to parse and navigate HTML content



# Ask user to enter a website URL
url = input("Please Enter a URL: ")


# If user does not include http/https, automatically add https
if not url.startswith(("https://", "http://")):
    url = "https://" + url

# Send GET request to the provided URL
response = requests.get(url)


# Store the HTML content of the page
txt = response.text


# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(txt, "html.parser")

# Loop through all form elements on the page
for form in soup.find_all("form"):

    # Print message when a form is found
    print("\n---Form Found---")

    # Inside each form, find all hidden input fields
    for input_tag in form.find_all("input", type="hidden"):


        # Get the name attribute of the hidden input
        # If it does not exist, return an empty string to avoid errors
        name = input_tag.get("name","")

        # Get the value attribute of the hidden input
        # If it does not exist, return an empty string
        value = input_tag.get("value","")

        # Print the hidden field name
        print(f"Hidden field name: ", name)


        # Print the hidden field value
        print(f"Hidden field value: ", value)



# Why hidden fields matter:

#  They store important data that users cannot see.
#  They often contain security tokens like CSRF tokens.
#  They help the website remember user information.
#  They are required for proper form submission.
#  Hidden does not mean secure — they can be viewed and changed.


















        
