#!/usr/bin/python3
"""
Queries a Reddit API

IMPORTS: requests
requests: Send and receive data packets from a URI
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries a valid subreddit and retrives the no of subs

    Args:
    subreddit(str): A reddit topic

    Return:
    No of subs a subreddit has
    """
url = ''
with requests.get(url, follow_redirects=false) as response:
    resp_json = response.json()
