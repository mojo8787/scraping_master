from scripts import scraping_script1, scraping_script2, scraping_script3, scraping_script4
from data_processing.data_cleaner import process_data
from utils import http_requests
import config

def main():
    # Example of how to use the configuration
    url = config.BASE_URLS['category1']
    headers = config.HEADERS

    # Example of using a utility function
    html_content = http_requests.get_html(url)

    # Example of executing one of the scraping scripts
    data = scraping_script1.scrape_function()  # Replace 'scrape_function' with the actual function name in scraping_script1

    # Process the scraped data
    cleaned_data = process_data(data)

    # You can add more logic here to run other scripts, handle different categories, etc.

    print("Scraping completed.")

if __name__ == "__main__":
    main()
