#!/bin/bash
# This script sends a GET request and displays the status code
curl -w '%{http_code}\n' -o /dev/null -s $1
