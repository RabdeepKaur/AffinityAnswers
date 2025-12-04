## We are give a url for Oxl webpage and we have to scrape the webpage and genreate a table 
## to scrape from the webpage  we are using data attribute  because i found them to be commmon for all the  title desc and price
## title of the ad : - the id for the title in the webpage html is  data-aut-id="itemTitle"
## the  description :- the id for the description in the webpage html is data-aut-id="itemDetails"
## the price :- the id for the price in the webpage html is data-aut-id="itemPrice"
## here I am not creating a spearate mainpy all the code will be present in one file 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from tabulate import tabulate 


driver = webdriver.Chrome()
driver.get("https://www.olx.in/items/q-car-cover?isSearchCall=true")

# Wait for content to load sinces it a dynamic webpage
time.sleep(2)

#locate elements by their data attributes preset in the html
titles = driver.find_elements(By.CSS_SELECTOR, '[data-aut-id="itemTitle"]')
descriptions = driver.find_elements(By.CSS_SELECTOR, '[data-aut-id="itemDetails"]')
prices = driver.find_elements(By.CSS_SELECTOR, '[data-aut-id="itemPrice"]')

# Extract text immediately to avoid stale element issues 
title_texts = [title.text for title in titles]
description_texts = [desc.text for desc in descriptions]
price_texts = [price.text for price in prices]

## print result in table format using tabulate
table_data = []
for i in range(len(title_texts)):
    table_data.append([
        i+1,
        title_texts[i] if i < len(title_texts) else "",
        description_texts[i] if i < len(description_texts) else "",
        price_texts[i] if i < len(price_texts) else ""
    ])

# Print table
print(tabulate(table_data, headers=["#", "Title", "Description", "Price"], tablefmt="grid"))

driver.quit()