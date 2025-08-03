#!/usr/bin/python3
"""
Reddit hot article fetcher module.
Provides a recursive function to get all hot article titles for a subreddit.
"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively queries the Reddit API to get all hot article titles.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list to accumulate post titles (default is None).
        after (str): The 'after' parameter for pagination (default is None).

    Returns:
        list: A list of hot article titles, or None if subreddit is invalid.
    """
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "python:hot.fetcher:v1.0 (by /u/yourusername)"
    }
    params = {
        "after": after
    }

    try:
        response = requests.get(url, headers=headers,
        params=params, allow_redirects=False)

        if response.status_code != 200:
            return None

        data = response.json()
        posts = data.get("data", {}).get("children", [])

        for post in posts:
            title = post.get("data", {}).get("title")
            if title:
                hot_list.append(title)

        next_after = data.get("data", {}).get("after")

        if next_after is not None:
            return recurse(subreddit, hot_list, next_after)
        else:
            return hot_list

    except requests.RequestException:
        return None
