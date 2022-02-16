#!/usr/bin/python3
"""Function to query the number of subscribers of a subreddit"""

import requests


def number_of_subscribers(subreddit):
    """Return the number og subscribers on a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    subs = results.get("subscribers")
    return subs
