# Full-Stack eCommerce Project: python-wine-scraper
## Project Objective
To create my first eCommerce website, I made two applications:
the web app—<em>[flask-wineshop](https://github.com/eriklolson/flask-wineshop)</em>—that produces the eCommerce website and the
web scraper—<em>python-wine-scraper</em>—that supplies the back-end database with mock wine products.  For this repository I 
reduced the syntax that was particular to the website I scrapped and replace it with a template format with dynamic 
values, which can be adapted to scrape product data from other eCommerce websites.

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