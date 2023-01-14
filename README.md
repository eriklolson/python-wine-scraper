# Overview
This is a web scraper that collects wine product data from the website www.winedeals.com. It does so for the purpose of supplying mock inventory 
to my eCommerce web-app, flask-wineshop. The scraped product data is used for demonstration purposes only.

# Directions
I. Run Splash

In order to run scraper.py, you must first run Scrapy via Docker:
```angular2html
$ docker pull scrapinghub/splash
$ docker run -p 5023:5023 -p 8050:8050 -p 8051:8051 scrapinghub/splash
```
Splash will now be running on `localhost:8050`
```angular2html
http://localhost:8050/
```
II. Run Scraper.py

Run scraper.py via `anaconda-project run` in the command line. The app will collect the product data from the website and save it in a csv file.