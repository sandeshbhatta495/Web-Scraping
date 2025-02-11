from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Initialize the WebDriver
driver = webdriver.Chrome()

# Define the base URL and search query
query = "l"
base_url = f"https://www.daraz.pk/catalog/?_keyori=ss&from=input&q={query}&spm=a2a0e.11994172.search.go.2e202f2517x520"

# Initialize an empty list to store the data
data = []

# Scrape multiple pages
for i in range(1, 6):  # Adjust the range as needed (currently set to scrape 5 pages)
    driver.get(f"{base_url}&page={i}")
    time.sleep(3)  # Wait for the page to load

    # Find all product containers on the page
    products = driver.find_elements(By.CLASS_NAME, "gridItem--Yd0sa")  # Update the class name based on Daraz's HTML structure

    print(f"{len(products)} items found on page {i}")
    for product in products:
        try:
            # Extract the product name
            name = product.find_element(By.CLASS_NAME, "title--wFj93").text
            
            # Extract the price
            price = product.find_element(By.CLASS_NAME, "price--NVB62").text
            
            # Extract the rating (if available)
            try:
                rating = product.find_element(By.CLASS_NAME, "rating--XnhZt").text
            except:
                rating = "No rating"

            # Append the data to the list
            data.append({"Name": name, "Price": price, "Rating": rating})
        except Exception as e:
            print(f"Error extracting data for a product: {e}")

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Save the data to a CSV file
df.to_csv("laptops_daraz.csv", index=False)

# Close the WebDriver
driver.quit()

print("Data scraping completed. Saved to laptops_daraz.csv")
