from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
import os

# Set up the Selenium WebDriver
driver = webdriver.Chrome()

# Define the URL
url = "https://www.amazon.in/s?k=laptops&page=1"

# Open the URL
driver.get(url)
time.sleep(50)  # Wait for the page to load

# Find all product containers
products = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")

# List to store data
data = []

# Extract details
for product in products:
    try:
        # Title
        title = product.find_element(By.XPATH, ".//span[@class='a-size-medium a-color-base a-text-normal']").text

        # Price
        price = product.find_element(By.XPATH, ".//span[@class='a-price-whole']").text

        # Link
        link = product.find_element(By.XPATH, ".//a[@class='a-link-normal a-text-normal']").get_attribute("href")

        # Rating
        rating = product.find_element(By.XPATH, ".//span[@class='a-icon-alt']").text

        # Append to data
        data.append({"Title": title, "Price": price, "Link": link, "Rating": rating})
    except Exception as e:print(driver.page_source)  # Prints the HTML content of the page

print(f"Error extracting product: {e}")



# Close the browser
driver.quit()

# Convert to DataFrame and save as CSV
df = pd.DataFrame(data)
output_file = os.path.join(os.getcwd(), "amazon_laptops_new.csv")
df.to_csv(output_file, index=False)

print(f"Data saved to {output_file}")
