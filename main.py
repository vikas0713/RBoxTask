"""
The driver script of the crawler, you can enter pass argument from command line also
Created By : Vikas Verma
"""
import sys

from RBCrawler import CrawlTheWeb

if __name__ == "__main__":
    if sys.argv[1:]:
        for cli_urls in sys.argv[1:]:
            crawl_obj = CrawlTheWeb(cli_urls)
            if crawl_obj.valid_url:
                print("Crawling the Web.......")
    else:
        crawl_obj = CrawlTheWeb("http://www.apache.org/")
    # print(sys.argv[1:])
