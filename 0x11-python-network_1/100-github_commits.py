#!/usr/bin/python3
"""This script lists 10 most recent commits or the repo"""
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    res = requests.get(url)
    resjson = res.json()
    for i in range(0, len(resjson)):
        if i < 10:
            sha = resjson[i].get("sha")
            author = resjson[i].get("commit").get("author").get("name")
            print(f"{sha}: {author}")
        else:
            break
