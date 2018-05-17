
# Jiandan crawler

## Installation

1. Install dependencies
```bash
$ pip3 install -r requirements.txt
```

2. [Download ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)

3. Make sure it’s in your PATH, e. g., place it in /usr/bin or /usr/local/bin.

## Usage

```bash
$ scrapy crawl meizitu

# Support multiple pages.
# Modify maxPage in spiders/meizituList/MeizituListSpider to control the number of pages.
$ scrapy crawl meizituList 

$ scrapy crawl news 
```

## Documents
* [Scrapy](https://scrapy.org/)
* [Selenium](https://seleniumhq.github.io/selenium/docs/api/py/index.html)
