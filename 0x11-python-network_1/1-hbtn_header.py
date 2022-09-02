#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the
URL and displays the value of the X-Request-Id
variable found in the header of the response.
"""

from urllib import request
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    req = request.Request(url)
    with request.urlopen(req) as response:
        the_page = response.headers
        print(the_page["X-Request-Id"])
