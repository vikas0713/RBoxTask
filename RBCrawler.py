"""
This is an example crawler, which takes a url and traverse the all links and save them in a JSON file.
You can pass any urls at a time and files of respective website will save in there repsective folders.
Created By : Vikas Verma
"""
import json
import gc

import validators  # For validating the urls entered by the user
import requests  # For making Http requests
from BeautifulSoup import BeautifulSoup as parser   # Parsing HTML data

from base import Base
from constants import CrawlerException
from web_data import WebData


class CrawlTheWeb(Base):
    """
    Description will go here
    """

    def __init__(self, url):
        super(CrawlTheWeb, self).__init__()
        self.root_url = url
        self.valid_url, self.response, self.title, self.directory = None, None, None, None
        self.all_links, self.primary_links = [], []
        self.parsed_html ,self.folder_created, self.page = None, None, None
        self.validate_url()

    def validate_url(self):
        if "https://" in self.root_url or "http://" in self.root_url:
            # Check if http/https is already prepended in the URL
            if validators.url(self.root_url):
                # Check if the url is valid or not
                if self.root_url.endswith("/"):
                    self.valid_url = self.root_url[:-1]     # Removing / from the end
                    self.title = self.root_url.replace("http://", "").replace("https://", "").replace("/", "")
                else:
                    self.valid_url = self.root_url
                    self.title = self.root_url.replace("http://", "").replace("https://", "").replace("/", "")

                self.request(self.valid_url)  # Call server with valid_url
            else:
                self.valid_url = None
                raise CrawlerException("URL is not Valid")

        else:
            self.root_url = "http://" + self.root_url
            if validators.url(self.root_url):
                if self.root_url.endswith("/"):
                    self.valid_url = self.root_url[:-1]
                    self.title = self.root_url.replace("http://", "").replace("https://", "").replace("/", "")
                else:
                    self.valid_url = self.root_url
                    self.title = self.root_url.replace("http://", "").replace("https://", "").replace("/", "")
                self.request(self.valid_url)  # Call server with valid_url

            else:
                self.valid_url = None

        for link in self.primary_links:
            self.request(link)  # Collect secondary links
            self.all_links = [hl for hl in self.all_links if
                              hl not in self.primary_links]  # Removing Duplicates if present
            gc.collect()  # Manual garbage collection
            print("."),
        self.primary_links += self.all_links
        self.primary_links = list(set(self.primary_links))
        if self.primary_links:
            with open(self.directory + "sitemap.json", "w") as fp:
                fp.write(json.dumps({"site_uls": self.primary_links}, indent=4))

            # CALL TO SAVE PAGES TO THE DIRECTORY
            self.web_data()
        else:
            print("Resource not found!!!!")

    def request(self, url):
        if True:
            self.response = requests.get(self.valid_url)
            status_code = self.response.status_code
        else:
            status_code = None

        if status_code == 200:
            self.parsed_html = parser(self.response.text)
            if not self.folder_created:  # Create folder on first request
                print("Fetching links from server %s" % self.valid_url),
                self.directory = "./" + self.title + "/"
                self.create_folder(self.directory)  #
                self.folder_created = True
                self.crawl_links(primary_links=True)
            else:
                self.crawl_links()

    def crawl_links(self, primary_links=False):
        for link in self.parsed_html.findAll('a'):
            try:
                if link['href'].strip() not in self.all_links and link['href'].strip() not in self.primary_links:
                    if self.valid_url in link['href']:
                        if primary_links:
                            self.primary_links.append(link['href'].strip())
                        else:
                            self.all_links.append(link['href'].strip())
                    elif link['href'].startswith('/'):
                        if primary_links:
                            self.primary_links.append(self.valid_url + link['href'].strip())
                        else:
                            self.all_links.append(self.valid_url + link['href'].strip())
                    else:
                        pass
            except :    # AttributeError or KeyError
                pass

    def web_data(self):
        # Fetch HTML, CSS, JS and Images from the sources
        for link in self.primary_links:
            raw_html = self.simple_request(link)
            if raw_html:
                WebData(raw_html, self.directory, self.valid_url)
            else:
                pass






