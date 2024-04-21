#!/bin/bash
# This script displays all HTTP methods the server will accept
curl -X OPTIONS -si "$1" | grep "Allow:" | cut -d' ' -f2-
