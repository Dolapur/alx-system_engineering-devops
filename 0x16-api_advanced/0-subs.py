#!/usr/bin/python3
"""This queries the suscribers lists."""
import requests


def number_of_subscribers(subreddit):
    """Return the numbers of subscribers."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "Dear Dolapo v1.0.0)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
