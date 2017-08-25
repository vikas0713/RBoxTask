"""
The base script of the crawler, for reusability purpose we are using this
Created By : Vikas Verma
"""
import os

import requests
from BeautifulSoup import BeautifulSoup as parser


class Base(object):
    """
    Base class for reusability of code
    """

    def __init__(self):
        pass

    def simple_request(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.text
            else:
                return None
        except:    # SSL Exception or may be Timeout Exception
            return None

    def beautify(self, url):
        response_data = self.simple_request(url)        # Parsing response data to HTML
        if response_data:
            return parser(response_data)
        else:
            return None

    def create_folder(self, directory):  # Creating respective directory of the web
        if not os.path.exists(directory):
            os.makedirs(directory)
        else:
            pass

    def is_exists(self, directory):
        return True if os.path.exists(directory) else False

    def parse_raw_html(self, raw_html):
        return parser(raw_html)