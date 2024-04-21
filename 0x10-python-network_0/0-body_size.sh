#!/bin/bash
# This script takes in a URL and displays the size of the vody of the response

curl -w '%{size_download}\n' -o /dev/null -s "$1"
