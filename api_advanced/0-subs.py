#!/usr/bin/python3
"""
Module for querying Reddit API to get subreddit subscriber counts.

This module provides functionality to retrieve the total number of subscribers
for a given subreddit using the Reddit API without authentication.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Query the Reddit API and return the number of subscribers for a subreddit.
    
    Args:
        subreddit (str): The name of the subreddit to query
        
    Returns:
        int: The number of subscribers for the subreddit, or 0 if invalid
    """
    if not subreddit or not isinstance(subreddit, str):
        return 0
    
    # Clean the subreddit name (remove /r/ prefix if present)
    subreddit = subreddit.strip().lstrip('r/').lstrip('/')
    
    # Reddit API endpoint for subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Set custom User-Agent to avoid rate limiting issues
    headers = {
        'User-Agent': 'SubredditSubscriberCounter/1.0 (by /u/api_user)'
    }
    
    try:
        # Make request without following redirects
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if we got a redirect (invalid subreddit)
        if response.status_code in [301, 302, 404]:
            return 0
            
        # Check for successful response
        if response.status_code != 200:
            return 0
            
        # Parse JSON response
        data = response.json()
        
        # Check if the response contains valid subreddit data
        if 'data' not in data or data['data'] is None:
            return 0
            
        # Extract subscriber count
        subscribers = data['data'].get('subscribers')
        
        # Return subscriber count or 0 if not found/invalid
        return subscribers if isinstance(subscribers, int) and subscribers >= 0 else 0        
    except (requests.RequestException, ValueError, KeyError):
        return 0
