import requests                             # To send HTTP requests
from bs4 import BeautifulSoup               # To parse HTML content

from urllib.parse import urlparse, urljoin  # To handle URLs


# Ask user for website URL
url = input("Please enter a url: ")


# If the URL does not start with http/https, add https automatically
if not url.startswith(("https://", "http://")):
    url = "https://" + url

# Extract the domain to follow only internal links
domain = urlparse(url).netloc

# Set to store visited URLs (avoid duplicates)
visited = set()

# List of URLs to visit (starting with the input URL)
to_visit = [url]


# Loop until all internal links are visited
while to_visit:
    url = to_visit.pop()

    # Skip URL if already visited
    if url in visited:
        continue

    visited.add(url)
    print("Visiting: ", url)

    try:

        # Send GET request and parse the HTML
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html , "html.parser")


        
        # Find all <a> tags with href
        for link in soup.find_all("a" , href=True):
            n_url = link["href"]
            full_link = urljoin(url , n_url)         # Convert relative URLs to full URLs


            # Only follow links within the same domain
            if urlparse(full_link).netloc == domain:
                if full_link not in visited:
                    to_visit.append(full_link)



    except:
        pass    # Ignore pages that cause errors


# Print all visited internal URLs
for n_visited in visited:
    print("Here is  all visited url: ", n_visited)

    
            
