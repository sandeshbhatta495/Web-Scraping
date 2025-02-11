import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the base URL and search query
query = "laptop"
base_url = f"https://www.daraz.pk/catalog/?_keyori=ss&from=input&q={query}&spm=a2a0e.11994172.search.go.2e202f2517x520"

# Initialize an empty list to store the data
data = []

# Scrape multiple pages
for i in range(1, 6):  # Adjust the range to scrape more pages
    url = f"{base_url}&page={i}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all product containers
    products = soup.find_all('div', class_='gridItem--Yd0sa')  # Update this class based on the site's HTML

    print(f"{len(products)} items found on page {i}")
    for product in products:
        try:
            # Extract the product name
            name = product.find('div', class_='title--wFj93').text.strip()
            
            # Extract the price
            price = product.find('span', class_='price--NVB62').text.strip()
            
            # Extract the rating (if available)
            rating_tag = product.find('span', class_='rating--XnhZt')
            rating = rating_tag.text.strip() if rating_tag else "No rating"

            # Append the data to the list
            data.append({"Name": name, "Price": price, "Rating": rating})
        except Exception as e:
            print(f"Error extracting data for a product: {e}")

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Save the data to a CSV file
df.to_csv("laptops_daraz_bs4.csv", index=False)

print("Data scraping completed. Saved to laptops_daraz_bs4.csv")
