import requests                        # To send HTTP requests to websites
from bs4 import BeautifulSoup          # To parse and navigate HTML content


# Ask user to enter a website URL
url = input("Please enter url: ")


# If user does not include http/https, automatically add https
if not url.startswith(("https://", "http://")):
    url = "https://" +url


# Send GET request to the provided URL
response = requests.get(url)


# Store the HTML content of the page
txt = response.text


# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(txt, "html.parser")

# List of keywords to detect possible sensitive images
keyword = ["admin", "backup", "secret", "private", "db"]

# List to store image URLs that match keywords
image = []

# Loop through all <img> tags with a 'src' attribute
for img in soup.find_all("img", src=True):

    # Get image URL and convert to lowercase
    src = img["src"].lower()

    # Check if the image filename contains any keyword
    if any(word in src for word in keyword):

        image.append(src)


# Print all sensitive images found
for sensitive_image in image:
    print("Sensitive image found: ",sensitive_image)
        
    
