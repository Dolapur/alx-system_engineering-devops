#!/usr/bin/python3
"""This helps us prints"""
import requests


def top_ten(subreddit):
    """Print the top 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "Dear Dolapo v1.0.0"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
    else:
    	results = response.json()["data"]["children"]
    	for title in children:
            print(title["data"]["title"])
