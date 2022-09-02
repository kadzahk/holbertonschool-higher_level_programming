#!/usr/bin/python3
"""
Write a Python script that takes your GitHub
credentials (username and password) and uses
the GitHub API to display your id.
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    response = requests.get(
        "https://api.github.com/user", auth=(argv[1], argv[2]))
    if response.status_code == 200:
        print(response.json()["id"])
    else:
        print("None")
