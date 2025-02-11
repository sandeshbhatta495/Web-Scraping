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

   
   
df = pd.DataFrame(product_data)
df.to_csv("himalayan_products.csv", index=False)
print("Data saved to himalayan_products.csv")