import Worker as wk
import sys 
site = sys.argv[1]
url_list = [
    f'{site}/sitemap.xml',
    f'{site}/sitemap.php',
    f'{site}/sitemap.txt',
    f'{site}/sitemap.xml.gz',
    f'{site}/sitemap1.xml',
    f'{site}/post-sitemap.xml',
    f'{site}/page-sitemap.xml',
    f'{site}/sitemap-index.xml',
    f'{site}/sitemapindex.xml',
    f'{site}/sitemap_index.xml.gz',
    f'{site}/sitemap/index.xml',
    f'{site}/robots.txt'
]
# /sitemap.php
# /sitemap.txt
# /sitemap.xml.gz (using gzip compression)
# /sitemap1.xml (if there are multiple sitemaps, this may be the first sitemap in a group)
# /post-sitemap.xml (sitemap of posts, like the one on my website)
# /page-sitemap.xml (sitemap of pages, also like the one on my website)
# /sitemap-index.xml (with “-” instead of “_”)
# /sitemapindex.xml (without separation)
# /sitemap_index.xml.gz (using Gzip compression)
# /sitemap/index.xml (in a subfolder) 
# for obj in list:
#     with url.urlopen(obj) as connection:
#         code = connection.getcode()
#         print(obj,code)

for url in url_list:
    wk.Worker(f'python3 site_call.py {url}')