#!/usr/bin/python3
"""
Queries a Reddit API

IMPORTS: requests
requests: Send and receive data packets from a URI
"""
import requests


def top_ten(subreddit)
    """
    Queries a valid subreddit and prints the first 10 hot posts

    Args:
    subreddit(str): A reddit topic

    Return:
    None
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10&t=all'
    headers = {'User-agent': 'Ubuntu20.04:api-advanced-script'}
    try:
        response = requests.get(url, allow_redirects=False, headers=headers)
    except Exception as e:
        print(f'An exception has occurred: {e}')

    if response.status_code == 200:
        resp_json = response.json()
        posts = rsp_json['data']['children']

    elif response.status_code == 301:
        new_loc = response.headers['Location']
        try:
            new_resp = requests.get(new_loc, headers=headers)
        except Exception as e:
            print(f'An exception has occurred: {e}')
        resp_json = new_resp.json()
        posts = resp_json['data']['children']

    else:
        print(f'Coulnt fetch posts. Eoor: {response.status_code}')

    for post in posts:
        title = post['data']['title']
        print(title)
