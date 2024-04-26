#!/usr/bin/python3
"""This script displays the value of a header variable of url"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    res = requests.get(url)
    print(res.headers.get("X-Request-Id"))
