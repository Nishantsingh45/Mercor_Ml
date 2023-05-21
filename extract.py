import requests
from bs4 import BeautifulSoup

# Get the HTML of the page
response = requests.get("https://www.snitch.co.in/collections/t-shirts")
soup = BeautifulSoup(response.content, "html.parser")

# Find all the t-shirt products
tshirts = soup.find_all("div", class_="product-wrap")

# Create a list to store the product information
product_info = []

# Loop through the t-shirt products
for t-shirt in tshirts:
    # Get the product name
    product_name = t-shirt.find("h3").text

    # Get the product description
    product_description = t-shirt.find("p").text

    # Get the product link
    product_link = t-shirt.find("a")["href"]

    # Add the product information to the list
    product_info.append({
        "name": product_name,
        "description": product_description,
        "link": product_link
    })

# Save the product information to a JSON file
with open("tshirts.json", "w") as f:
    json.dump(product_info, f, indent=4)
