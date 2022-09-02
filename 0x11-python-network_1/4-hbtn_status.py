#!/usr/bin/python3
"""
Write a Python script that fetches https://intranet.hbtn.io/status
"""


if __name__ == "__main__":
    import requests
    url = "https://intranet.hbtn.io/status"
    response = requests.get(url)
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
