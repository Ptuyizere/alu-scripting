#!/usr/bin/python3
"""
Reddit subscriber counter module.
Provides a function to get the number of subscribers for a subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers to a given subreddit.

    Args:
        subreddiit (str): The name of the subreddit to query.

    Returns:
        int: Number of subscribers, or 0 if the subreddit is invalid.
    """
    if not isinstance(subreddit, str):
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "python:subscriber.fetcher:v1.0 (by /u/yourusername)"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data.get("data", {}).get("subscribers", 0)
        else:
            return 0
    except requests.RequestException:
        return 0

