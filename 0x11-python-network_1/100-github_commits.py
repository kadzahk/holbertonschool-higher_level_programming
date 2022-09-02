#!/usr/bin/python3
"""
Write a Python script that takes 2 arguments
in order to solve this challenge.
"""

if __name__ == "__main__":
    from sys import argv
    import requests

    repo = argv[1]
    username = argv[2]
    URL = "https://api.github.com/repos/{}/{}/commits".format(username, repo)

    response = requests.get(URL)
    for commit in response.json()[:10]:
        line = "{}: {}".format(
            commit['sha'], commit['commit']['author']['name'])
        print(line)
