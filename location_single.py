from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
query = "laptop"
for i in range (1,102):
    driver.get(f"https://www.daraz.pk/catalog/?page=2&q={query}&spm=a2a0e.tm80335142.search.d_go")
