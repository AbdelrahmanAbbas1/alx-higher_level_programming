#!/bin/bash
# This script sends a POST request
curl -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" -s "$1"
