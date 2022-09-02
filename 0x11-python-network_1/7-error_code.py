#!/usr/bin/python3
"""
Write a Python script that takes in a URL,
sends a request to the URL and displays
the body of the response.
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    url = argv[1]

    response = requests.get(url)
    if response.status_code == 200:
        print(response.text)
    else:
        print("Error code:", response.status_code)
