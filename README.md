# Overview
This web scraper uses BeautifulSoup4 to collect wine product data from a wine merchant website, www.winedeals.com. 
It does so for the purpose of supplying mock inventory to my eCommerce web-app, flask-wineshop. The scraped product data
is used for demonstration purposes only.

# Directions
### Run 'scraper.py' to scrape data
1. To run scraper.py, you must first run Scrapy, which may be done by the following commands:
    ```angular2html
    $ docker pull scrapinghub/splash
    $ docker run -p 5023:5023 -p 8050:8050 -p 8051:8051 scrapinghub/splash
    ```
2. With Splash running in the background, run scraper.py via `anaconda-project run` or `python scraper.py` in terminal. 
   Product data will be scraped and saved in the output file 'wine-data.csv'.

### Run import.py to load data into Postgres database table
