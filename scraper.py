import requests
from bs4 import BeautifulSoup
import regex
import pandas as pd
import numpy as np


# Loop through pages: start at page 1, stop at page 8, proceed by step 1.
pages = np.arange(1, 8, 1)
headers = {'Accept-Language': 'en-US, en;q=0.5'}

# Initialize Python dictionaries for the storing of desired product data
product_links = []
product_names = []
producers = []
wine_types = []
varietals = []
years = []
volumes = []
proofs = []
countries = []
regions = []
prices = []
images = []
descriptions = []

# Loop through pages in the manner defined by np.arrange
for page in pages:
    URL = {'yourUrL'}
    res = requests.get('http://localhost:8050/render.html', params={'url': URL}, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    product_elements = soup.find_all('div', {'data-hook': 'product-element'})

    for product_element in product_elements:
        # collect links to subpages from main page, one for each individual product
        product_link = product_element.find('a', {'data-hook': 'product-link'})['href']
        product_links.append([product_link])
        subpage = requests.get(product_link)
        subsoup = BeautifulSoup(subpage.text, 'html.parser')

        # scrape desired text from subpage and append to dict
        product_name = subsoup.find('i', {'data-hook': 'product-name'}).text.strip()
        product_names.append([product_name])

        producer = subsoup.find('div', {'data-hook': 'producer-name'}).text.strip()
        producers.append([producer])

        wine_types = subsoup.find('p', {'data-hook': 'wine-type'}).text.strip()
        wine_types.append([wine_types])

        varietal = subsoup.find('i', {'data-hook': 'varietal-name'}).text.strip()
        varietals.append([varietal])

        # extract year from a string within p tag via regex
        year = subsoup.find('p', {'data-hook': 'year'}).text.strip()
        year = regex.findall(r'\d+', year)
        years.append(year)

        # extract year from <p class="product-subtitle">2022 / 750 ml. | Item#83885</p>
        volume = product_element.find('p', 'product-subtitle').text.strip()
        # capture text between the '/' and '|' characters to get year
        volume = regex.findall(r"\/(.*?)\|", volume)
        volumes.append(volume)

        # scrape via regex method, as by matching text 'Proof' in li tags
        exp = regex.compile(r'\d*[^<]*')
        proof = subsoup.find('li', {'class': exp})
        proofs.append(proof)

        price = subsoup.find('span', {'data-hook': 'price'}).text.strip()
        prices.append([price])

        # extract country from '<p> New Zealand | South Island | Marlborough </p>'
        country = product_element.find('p', 'product-location').text.strip()
        country = regex.findall(r"([^\,\|]+)", country)
        countries.append(country)

        # extract region from '<p> New Zealand | South Island | Marlborough </p>'
        region = product_element.find('p', 'product-location').text.strip()
        region = regex.findall(r"\|(.*?)\|", region)
        regions.append(region)

        # extract src part from within image tag
        image = subsoup.findall('img')[0]['src']
        images.append(image)

        # only save if description present as it may not be for some products
        description = subsoup.find('span', 'description').text if subsoup.find('span', 'description') else 'Null'
        descriptions.append([description])

"""
Pandas Dataframe
"""
# Initialize dataframe
wine_data = pd.DataFrame({
    'product_name': product_names,
    'producers': producers,
    'wine_types': wine_types,
    'varietals': varietals,
    'year': years,
    'volume': volumes,
    'proofs': proofs,
    'country': countries,
    'region': regions,
    'price': prices,
    'image': images,
    'description': descriptions,
})

# Remove the rows if there are missing values in the following fields. Note: 'description' is not included here because
# a good proportion of products do not include one, yet I still want to retain these.
wine_data.dropna(subset=['product_name'], inplace=True)
wine_data.dropna(subset=['producer'], inplace=True)
wine_data.dropna(subset=['wine_type'], inplace=True)
wine_data.dropna(subset=['varietal'], inplace=True)
wine_data.dropna(subset=['year'], inplace=True)
wine_data.dropna(subset=['volume'], inplace=True)
wine_data.dropna(subset=['proof'], inplace=True)
wine_data.dropna(subset=['country'], inplace=True)
wine_data.dropna(subset=['region'], inplace=True)
wine_data.dropna(subset=['price'], inplace=True)
wine_data.dropna(subset=['image'], inplace=True)

# Save the dataframe to a cvs file
wine_data.to_csv('wine_data.csv')

# Print data types af dataframe fields (for troubleshooting)
dataTypeSeries = wine_data.dtypes
print(dataTypeSeries)
