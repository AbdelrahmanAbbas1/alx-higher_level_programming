#!/bin/bash
# This script sends a Json post request
curl -X POST -d "@$2" -H "Content-Type: application/json" -s "$1"
