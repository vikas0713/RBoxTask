"""
This file contains the constants that is used byt the crawler
Created By: Vikas Verma
"""


class CrawlerException(Exception):
    """
    Exception when user enters some bad input
    """
    def __init__(self, message):
        super(CrawlerException, self).__init__(message)
        self.message = message




