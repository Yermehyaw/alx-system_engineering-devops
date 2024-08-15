#!/usr/bin/python3
"""
Queries a subreddit and returns the no of subscribers


IMPORTS: requests

requests: Send and receive data packets from a URI
"""
import requests


url = ''
with requests.get(url, follow_redirects=false) as response:
    resp_json = response.json()
