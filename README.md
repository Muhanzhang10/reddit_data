# reddit_data_crawler
## Introduction
This is a skeleton of code for web crawling reddit comments with a key word using python selenium. The current approach is of the following:
1. Crawl the URLs of the posts with the related search keyword. For example, to search the posts with the key word "wall street bank", run `python3 url.py --keyword="wall street bank"`.
2. Use the stored URLs of the posts and crawl the content within by running `python3 comment.py`

A quick demonstrative result is stored in the "result/" directory. 

## Future TODOs
1. Set up an IP pool to prevent the same IP exceeding number of available requests.
2. Add Xpath of follow up comment of each post to crawl these textual data. 
3. Set up a database to systematically store crawled data.