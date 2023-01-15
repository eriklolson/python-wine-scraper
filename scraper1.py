import requests
from bs4 import BeautifulSoup
import regex as re
import pandas as pd
import numpy as np

# Using the np.arrange function, define start, stop, and step range for scrapping multiple pages
headers = {'Accept-Language': 'en-US, en;q=0.5'}

# Initialize Python dictionaries for the storing of desired product data
# product_names = []
# years = []
# volumes = []
# brands = []
# proofs = []
# countries = []
# regions = []
# product_links = []
# colors = []
# primary_grapes = []
# all_grapes = []
# prices = []
# images = []
# descriptions = []

# Loop through pages in the manner defined by np.arrange

URL = 'https://www.winedeals.com/wine.html'
page = requests.get(URL)
rendered_page = requests.get('http://localhost:8050/render.html', params={'url': URL}, headers=headers)
print(rendered_page)
soup = BeautifulSoup(rendered_page.content, "html.parser")
print(soup)
product_elements = soup.find_all('li', class_='product-item')
print(product_elements)
for product_element in product_elements:
    print(product_element)
    volume = product_element.find('p', class_='productsubtitle').text
    print(volumes)

    # print(soup)
