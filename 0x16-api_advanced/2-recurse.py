#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a list of titles of all hot posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0"
    }
    query = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=query,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    data = response.json().get("data")
    after = data.get("after")
    count += data.get("dist")
    for c in data.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
