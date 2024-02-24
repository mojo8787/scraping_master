# config.py

# Base URLs for different categories or sites you are scraping
BASE_URLS = {
    "category1": "https://example.com/category1",
    "category2": "https://example.com/category2",
    # Add more categories as needed
}

# Common headers for your HTTP requests (if needed)
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

# Other global parameters
TIMEOUT = 10  # Timeout for HTTP requests in seconds
DELAY = 1     # Delay between requests in seconds

# Add any other configuration parameters that are common across your scripts
