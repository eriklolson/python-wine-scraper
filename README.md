# Overview
This web scraper uses BeautifulSoup4 to collect wine product data from a wine merchant website. It does so for the purpose 
of supplying mock inventory to my eCommerce web-app, flask-wineshop (https://github.com/eriklolson/flask-wineshop).
This is a template that may be adapted to scrape product data from eCommerce websites. 

# Directions
### Run scraper.py: collect product data
1. To run scraper.py, you must first run Scrapy, which may be done by the following commands:
    ```angular2html
    $ docker pull scrapinghub/splash
    $ docker run -p 5023:5023 -p 8050:8050 -p 8051:8051 scrapinghub/splash
    ```
2. With Splash running in the background, run scraper.py via `anaconda-project run` or `python scraper.py` in terminal. 
   Product data will be scraped and saved in the output file 'wine-data.csv'.

### Run import.py: load data into Postgres table
1. As illustrated in .env.example, enter your Postgres DATABASE_URI in a .env file.
2. Run scraper.py by this command:
    ```angular2html
    $ python scraper.py
    ```