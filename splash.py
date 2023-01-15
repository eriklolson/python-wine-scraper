from dotenv import load_dotenv, find_dotenv
import requests
from bs4 import BeautifulSoup
headers = {'Accept-Language': 'en-US, en;q=0.5'}

url = 'https://www.winedeals.com/marlborough-vines-sauvignon-blanc-2022-750-ml-83885.html'
res = requests.get("http://localhost:8050/render.html", params={"url": url, "wait": 2}, headers=headers)
soup = BeautifulSoup(res.content, "html.parser")
print(soup)
# title = soup.find('h1', 'page-title').text
# print(title)
# product_elements = soup.find_all('li', class_='product-item')
# print(product_elements)

# list_names = []
#
# for product_element in product_elements:
#
#
#   name = product_element.find('i', {'data-hook': 'review-star-rating'}).text
#   body = item.find('span', {'data-hook': 'review-body'}).find('span').text
#
#   review = {
#     'rating': rating,
#     'body': body
#   }
#
#   list_names.append(product_data)