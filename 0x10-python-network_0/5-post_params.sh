#!/bin/bash
# This script sends a POST request
curl -X POST -H "email: test@gmail.com; subject: I will always be here for PLD" -s "$1"
