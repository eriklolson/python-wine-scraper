# Overview
This web scraper uses BeautifulSoup4 to collect wine product data from a wine merchant website. It does so for the purpose 
of supplying mock inventory to my eCommerce web-app, flask-wineshop (https://github.com/eriklolson/flask-wineshop).
This is a template that may be adapted to scrape product data from eCommerce websites. 

# Directions
### Run scraper.py: collect product data
1. To ensure that scraper.py is able to scrape JavaScript rendered content, run Splash in the background first. The easiest 
   way is by the following commands:
    ```angular2htmlc
    $ docker pull scrapinghub/splash
    $ docker run -p 5023:5023 -p 8050:8050 -p 8051:8051 scrapinghub/splash
    ```
2. Run scraper.py via `anaconda-project run` or `python scraper.py` in terminal. 
   Product data will be scraped and saved in the output file 'wine-data.csv'.

### Run import.py: load data into Postgres table
1. As illustrated in .env.example, enter your Postgres DATABASE_URI in a .env file.
2. Run import.py by this command:
    ```angular2html
    $ python import.py
    ```