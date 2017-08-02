# Web Scraping in Python
_________________________
Trey Brooks: <monroemasseybrooks@gmail.com>

### Getting setup
1. Install Anaconda with Python 3.6

+ Install environment from file

 ```$ conda env create -f environment.yml```

## TicketMaster Demos
1. In a console navigate to this directory

+ Execute
 ```$ jupyter notebook```

+ Launch <http://127.0.0.1:8888> in a browser.
+ Find and open the notebooks in your browser.

## Scrapy Demo
1. Check that crawler will work

 ```$ scrapy check```
+ Make sure mongod is running

 ```$ mongod```

+ running the crawler

 ```$ scrapy runspider quotes_spider/spiders/quotes_scraper.py```
