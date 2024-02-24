# config.py

import random
import time

# Base URLs for different categories or sites you are scraping
BASE_URLS = {
    "category1": "https://example.com/category1",
    "category2": "https://example.com/category2",
    # Add more categories as needed
}

# List of User Agents for rotation
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)...",
    # Add more user agents
]

# Function to get a random user agent
def get_random_user_agent():
    return random.choice(USER_AGENTS)

# Proxy settings (optional)
PROXIES = [
    # Add your proxy settings here (if using)
]

# Function to randomly vary delays to mimic human behavior

def human_like_delay():
    return random.uniform(1, 5)  # Random delay between 1 and 5 seconds

# Common headers for your HTTP requests (if needed)
HEADERS = {
    "User-Agent": get_random_user_agent()
}

# Other global parameters
TIMEOUT = 10  # Timeout for HTTP requests in seconds
DELAY = human_like_delay()  # Variable delay for requests

# Error handling
MAX_RETRIES = 3  # Maximum retries for a failed request

# Logging and Monitoring
LOG_FILE = "scraping.log"
LOG_LEVEL = "INFO"

# Data Storage
DATABASE_URI = "sqlite:///scraping_data.db"
FILE_STORAGE_PATH = "/path/to/store/files"

# Add any other configuration parameters that are common across your scripts

