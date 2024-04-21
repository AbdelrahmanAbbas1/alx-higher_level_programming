#!/bin/bash
# This script displays the status code
curl -sw '%{http_code}' -o /dev/null "$1"
