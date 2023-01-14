import requests
from bs4 import BeautifulSoup
import regex as re
import pandas as pd
import numpy as np

# Using the np.arrange function, define start, stop, and step range for scrapping multiple pages
pages = np.arange(1, 8, 1)
headers = {'Accept-Language': 'en-US, en;q=0.5'}

# Initialize Python dictionaries for the storing of desired product data
product_names = []
years = []
volumes = []
brands = []
proofs = []
countries = []
regions = []
product_links = []
colors = []
primary_grapes = []
all_grapes = []
prices = []
images = []
descriptions = []

# Loop through pages in the manner defined by np.arrange
for page in pages:

    # Define base URL from which to scrape
    url = 'https://www.winedeals.com/wine.html?p=' + str(page) + '.html'
    results = requests.get('http://localhost:8050/render.html', params={'url': url}, headers=headers)
    soup = BeautifulSoup(results.text, 'html.parser')
    products = soup.find_all('div', class_='productlistingtext')

    # Loop through each container
    for container in products:
        product_link = container.find('a', class_='product-item-link')['href']
        product_links.append([product_link])
        subpage = requests.get(product_link)
        subsoup = BeautifulSoup(subpage.text, 'html.parser')

        if subsoup.select('a[title="View other items with the same Color"]'):
            for color in subsoup.select('a[title="View other items with the same Color"]'):
                color = color.text
        colors.append([color])

        brand = subsoup.select_one("span[itemprop=brand]").text if subsoup.select_one(
            "span[itemprop=brand]") else 'Null'
        brands.append([brand])

        regex = re.compile('.*Proof.*')
        proof = subsoup.find("li", {"class": regex}) if subsoup.find("li", {"class": regex}) else 'Null'
        proof = re.findall(r'(?<=</label> ).*(?= </li>)', str(proof))
        proofs.append(proof)

        price = subsoup.find('span', class_='price').text
        prices.append([price])

        image = subsoup.find('div', class_='product media') if subsoup.find('div', class_='product media') else 'Null'
        image = re.findall(r'(?<=gallery-placeholder__image" src=").*(?="/)', str(image))
        images.append(image)

        description = subsoup.find('div', class_='shortdescription sdcustom').text.replace('\"', '') if subsoup.find(
            'div', class_='shortdescription sdcustom') else 'Null'
        descriptions.append([description])

        product_name = container.find('a', class_='product-item-link').text.strip() if container.find('a',
                                                                                                      class_='product-item-link') else 'Null'
        product_names.append([product_name])

        year = container.find('p', class_='productsubtitle').text.split('/', 1)[0].strip().replace('\"',
                                                                                                   '') if container.find(
            'p', class_='productsubtitle') else 'Null'
        year = re.findall(r"\d+", year) if re.findall(r"\d+", year) else 'Null'
        years.append(year)

        volume = container.find('p', class_='productsubtitle').text.replace('\"', '').replace(' ml',
                                                                                              'ml').strip() if container.find(
            'p', class_='productsubtitle') else 'Null'
        volume = re.findall(r"\/(.*?)\|", volume)
        volumes.append(volume)

        primary_grape = container.find('div', class_='winegrapes wmarker').text.split('|', 1)[
            0].strip() if container.find('div', class_='winegrapes wmarker') else 'Null'
        primary_grape = re.findall(r"(?<=: )[^\]]+", primary_grape)
        primary_grapes.append(primary_grape)

        all_grape = container.find('div', class_='winegrapes wmarker').text.replace('\"', '').strip() if container.find(
            'div', class_='winegrapes wmarker') else 'Null'
        all_grape = re.split(r"\:", all_grape, 2)[-1] if re.split(r"\:", all_grape, 2)[-1] else 'Null'
        all_grapes.append([all_grape])

        country = container.find('div', class_='productlocation wmarker').text.split('|', 1)[
            0].strip() if container.find('div', class_='productlocation wmarker') else 'Null'
        country = re.findall(r"([^\,\|]+)", country) if re.findall(r"([^\,\|]+)", country) else 'Null'
        countries.append(country)

        region = container.find('div', class_='productlocation wmarker').text.replace('\"',
                                                                                      '').strip() if container.find(
            'div', class_='productlocation wmarker') else 'Null'
        region = re.findall(r"\|(.*?)\|", region) if re.findall(r"\|(.*?)\|", region) else 'Null'
        regions.append(region)


# Initialize Pandas dataframe
wine_data = pd.DataFrame({
    'product_name': product_names,
    'year': years,
    'volume': volumes,
    'proofs': proofs,
    'brand': brands,
    'country': countries,
    'region': regions,
    'color': colors,
    'primary_grape': primary_grapes,
    'all_grape': all_grapes,
    'price': prices,
    'image': images,
    'description': descriptions,
    'product_link': product_links
})

# Clean data; drop a row by condition
wine_data = wine_data[wine_data.image.astype(str).str.contains(r'(https)')]

wine_data.dropna(subset=["product_name"], inplace=True)
wine_data.dropna(subset=["year"], inplace=True)
wine_data.dropna(subset=["volume"], inplace=True)
wine_data.dropna(subset=["proofs"], inplace=True)
wine_data.dropna(subset=["country"], inplace=True)
wine_data.dropna(subset=["region"], inplace=True)
wine_data.dropna(subset=["color"], inplace=True)
wine_data.dropna(subset=["primary_grape"], inplace=True)
wine_data.dropna(subset=["price"], inplace=True)
wine_data.dropna(subset=["image"], inplace=True)
wine_data.dropna(subset=["product_link"], inplace=True)

# wine_data[wine_data["region"].str.contains("Null") == False]
# wine_data[wine_data["color"].str.contains("Null") == False]
wine_data.drop(wine_data[wine_data['region'] == 'Null'].index, inplace=True)
wine_data.drop(wine_data[wine_data['color'] == 'Null'].index, inplace=True)

# Remove any remaining unwanted characters from Pandas dataframe
wine_data['product_name'] = wine_data['product_name'].astype(str).str.replace(r"^[][\s]*$|(^'+|'+$|\'|\")",
                                                                              lambda m: '' if m.group(1) else np.nan)
wine_data['year'] = wine_data['year'].astype(str).str.replace(r"^[][\s]*$|(^'+|'+$|\'|\")",
                                                              lambda m: '' if m.group(1) else np.nan)
wine_data['volume'] = wine_data['volume'].astype(str).str.replace(r"^[][\s]*$|(^'+|'+$|\'|\")",
                                                                  lambda m: '' if m.group(1) else np.nan)
wine_data['proofs'] = wine_data['proofs'].astype(str).str.replace(r"^[][\s]*$|(^'+|'+$|\'|\")",
                                                                  lambda m: '' if m.group(1) else np.nan)
wine_data['brand'] = wine_data['brand'].astype(str).str.replace(r"^[][\s]*$|(^'+|'+$|\'|\")",
                                                                lambda m: '' if m.group(1) else np.nan)
wine_data['country'] = wine_data['country'].astype(str).str.replace(r"^[][\s]*$|(^'+|'+$|\')",
                                                                    lambda m: '' if m.group(1) else np.nan)
wine_data['region'] = wine_data['region'].astype(str).str.replace(r"^[][\s]*$|(^'+|'+$|\'|\")",
                                                                  lambda m: '' if m.group(1) else np.nan)
wine_data['color'] = wine_data['color'].astype(str).str.replace(r"^[][\s]*$|(^'+|'+$|\'|\")",
                                                                lambda m: '' if m.group(1) else np.nan)
wine_data['primary_grape'] = wine_data['primary_grape'].astype(str).str.replace(r"^[][\s]*$|(^'+|'+$|\'|\")",
                                                                                lambda m: '' if m.group(1) else np.nan)
wine_data['all_grape'] = wine_data['all_grape'].astype(str).str.replace(r"^[][\s]*$|(^'+|'+$|\'|\")",
                                                                        lambda m: '' if m.group(1) else np.nan)
wine_data['price'] = wine_data['price'].astype(str).str.replace(r"^[][\s]*$|(^'+|'+$|\'|\")",
                                                                lambda m: '' if m.group(1) else np.nan)
wine_data['image'] = wine_data['image'].astype(str).str.replace(r"^[][\s]*$|(^'+|'+$|\'|\")",
                                                                lambda m: '' if m.group(1) else np.nan)
wine_data['description'] = wine_data['description'].astype(str).str.replace(r"^[][\s]*$|(^'+|'+$|\'|\")",
                                                                            lambda m: '' if m.group(1) else np.nan)
wine_data['product_link'] = wine_data['product_link'].astype(str).str.replace(r"^[][\s]*$|(^'+|'+$|\'|\")",
                                                                              lambda m: '' if m.group(1) else np.nan)

# Add dataframe to CSV file
wine_data.to_csv('wine_data.csv')

# Print data types af dataframe fields for troubleshooting
dataTypeSeries = wine_data.dtypes
print(dataTypeSeries)
