import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://himalayansolution.com/category/basic-electronics-components?page="

product_data = []

for page in range(1, 31):
    url = base_url + str(page)
    response = requests.get(url)
    
    if response.status_code != 200:
        continue

    soup = BeautifulSoup(response.content, "html.parser")

    products = soup.select("h2.product-name a")
    for product in products:
        product_name = product.text.strip()
        product_price = product.find_next("span", class_="price").text.strip()
        product_url = product["href"]
        product_data.append({
            "Product Name": product_name,
             "product_price": product_price,
            "Product URL": product_url
           

        })

df = pd.DataFrame(product_data)
df.to_csv("daraz_products.csv", index=False)
print("Data saved to daraz_products.csv")