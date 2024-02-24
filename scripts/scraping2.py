import requests
from bs4 import BeautifulSoup
import csv

def scrape_page(url):
    try:
        response = requests.get(url)
        print(f"Requesting {url}, Status Code: {response.status_code}")
        if response.status_code != 200:
            print(f"Failed to retrieve the page with status code: {response.status_code}")
            return
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return

    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    listings = soup.find_all('div', class_='product-item-info')  # Update with the actual class name

    if not listings:
        print("No listings found on this page.")
        return

    with open('scraped_data.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title'])  # Column headers, add more if needed

        for listing in listings:
            title = listing.find('a', class_='product-item-link').text.strip()
            writer.writerow([title])  # Write the data
            print(title)  # Print title

# URL for the 'hair' category
url = 'https://www.tamata.com/beauty-health/hair.html'
scrape_page(url)


