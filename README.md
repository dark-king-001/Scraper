# Scraper
this is a web scraper i build using aria2c moduleand sub process module

every file uses subprocess and is multi threaded to process large amounts of data 
Worker.py       is responsible for multi threading
download.py     is responsible for downloading links
link_extract.py is responsible for creating single link bundle
scrape.py       is resposible to download every link from link bundle
site_call.py    is used to check status code of a link
sitemap_loader.py used to check for the site map using site_call.py of a website
