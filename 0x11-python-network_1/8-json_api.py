#!/usr/bin/python3
"""This script sends a POST request"""
import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    data = {"q": ""}
    if len(sys.argv) > 1:
        data["q"] = sys.argv[1]

    res = requests.post(url, data)
    try:
        res_json = res.json()
        if res_json:
            print("[{}] {}".format(res_json["id"], res_json["name"]))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
