# Full-Stack eCommerce Project: python-wine-scraper
## Project Objective
To achieve my goal of creating my first eCommerce website, I made two applications: 
the web-app, [flask-wineshop](https://github.com/eriklolson/flask-wineshop), that produces the eCommerce website and
the web-scraper, python-wine-scraper, that supplies the back-end database with mock wine products. This is the repository
for the latter. I reduced the syntax particular to a certain website that I scrapped to a general template with dynamic 
values; it may be adapted to scrape product data from other eCommerce websites.

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