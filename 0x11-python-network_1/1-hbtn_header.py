#!/usr/bin/python3
"""This script display the value of a header of a passed url"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        print(res.headers["X-Request-Id"])
