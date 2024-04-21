#!/bin/bash
# This script displays the status code
curl -sw '%{http_code}\n' -o /dev/null "$1"
