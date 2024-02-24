import requests
from requests.exceptions import RequestException

def get_html(url):
    """
    Makes an HTTP GET request to the provided URL and returns the HTML content.
    Returns None if the request fails or if the status code is not 200.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.content
    except RequestException as e:
        print(f"Error during request to {url}: {e}")
        return None
