import requests                            # Used to send HTTP requests
from bs4 import BeautifulSoup              # Used to parse XML/HTML content



# Ask user to enter a website URL
url = input("Please enter a url: ")


# If user did not include http/https, automatically add https
if not url.startswith(("https://", "http://")):
    url = "https://" + url


# Send GET request to the provided URL
response = requests.get(url)


# Get the page content as text
text = response.text


# Parse the content as XML (used for sitemap files)
soup = BeautifulSoup(text, "xml")

# Create empty list to store discovered admin-related URLs
admin_panel = []

# Keywords we want to search for inside URLs
keywords = ["admin", "login" , "dashboard" , "pannel", "backend"]

# Find all <loc> tags 
for loc in soup.find_all("loc"):


    # Get the URL inside <loc> and convert to lowercase
    n_text = loc.text.lower()

    # Check if any keyword exists inside the URL
    if any(word in n_text for word in keywords):

        # If match found, add URL to list
        admin_panel.append(n_text)



# Print all found admin-related URLs
for panel in admin_panel:
    print("\nHere is all URL: ", panel)
            

    
