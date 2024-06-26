#!/usr/bin/python3
"""This script takes github credentials and uses github api"""
import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/user"
    username = sys.argv[1]
    token = sys.argv[2]

    res = requests.get(url, auth=(username, token))
    print(res.json().get("id"))
