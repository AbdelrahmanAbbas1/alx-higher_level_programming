#!/usr/bin/python3
"""This script fetches an urr using requests package"""
import requests


if __name__ == "__main__":
    r = requests.get("https://alx-intranet.hbtn.io/status")
    data = r.text
    print(f"Body response:\n\t- type: {type(data)}\n\t- content: {data}")
