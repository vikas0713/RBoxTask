"""
The driver script of the crawler, you can enter pass argument from command line also
Created By : Vikas Verma
"""
import sys

from RBCrawler import CrawlTheWeb

if __name__ == "__main__":
    if sys.argv[1:]:
        CrawlTheWeb(sys.argv[1])
    else:
        # Default options
        options = {
            "1": "http://www.apache.org",
            "2": "http://www.python.org",
            "3": "http://getbootstrap.com \n"
        }
        print("\033[95m Enter URL to crawl or choose from options given below for test: \033[0m")
        print("\033[1m 1. http://www.apache.org  \033[0m")
        print("\033[1m 2. http://www.python.org \033[0m")
        print("\033[1m 3. http://getbootstrap.com \033[0m")
        user_input = raw_input("\n")
        if user_input.isdigit():
            try:
                url = options[user_input]
                print("\033[92m Fetching Content from %s \033[0m" %url)
                crawl_obj = CrawlTheWeb(url)
            except:
                print("Not a valid options!!")
        else:
            print("\033[92m Fetching Content from %s \033[0m" %user_input)
            CrawlTheWeb(user_input)
