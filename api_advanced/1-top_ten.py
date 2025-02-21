#!/usr/bin/python3
"""
Script to query the Reddit API and print the titles of the first 10 hot posts for a given subreddit.
"""

import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None
    """
    # Reddit API URL for hot posts in a subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    
    # Set a custom User-Agent to avoid rate limiting
    headers = {"User-Agent": "alu-scripting/1.0"}

    # Make the request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the subreddit is valid
    if response.status_code == 200:
        try:
            # Parse the JSON response
            data = response.json()
            posts = data["data"]["children"]

            # Print the titles of the first 10 hot posts
            for post in posts:
                print(post["data"]["title"])
        except KeyError:
            # Handle invalid subreddit or unexpected response format
            print(None)
    else:
        # Handle invalid subreddit or other errors
        print(None)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
