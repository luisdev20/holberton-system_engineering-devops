#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""

import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0"
    }
    query = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=query,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    data = response.json().get("data")
    
    for c in data.get("children"):
        print (c.get("data").get("title"))
    