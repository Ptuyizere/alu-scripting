#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit: str):
    """
    Return the number of subscribers for a given subreddit or return 0 in the subreddit is invalid.

    Parameters:
        subreddit (str): The name of the subreddit (without '/r/').
    Retruns:
        int: Number of subscribers or 0 if subreddit is invalid.
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "python:subreddit.subscriber.counter:v1.0 (by /u/MUI007)"}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return data.get("data", {}).get("subscribers", 0)
        else:
            return 0
    except requests.RequestException:
        return 0

print(number_of_subscribers("python"))
