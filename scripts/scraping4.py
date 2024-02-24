import requests
from bs4 import BeautifulSoup
import csv
import time

def get_total_pages(soup):
    pagination = soup.find('ul', class_='pagination')
    if pagination:
        return int(pagination.find_all('li')[-2].text)
    else:
        return 1

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
    listings = soup.find_all('div', class_='product-item-info')

    if not listings:
        print("No listings found on this page.")
        return

    with open('scraped_data.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for listing in listings:
            title = listing.find('a', class_='product-item-link').text.strip()
            writer.writerow([title])
            print(title)  # Print title

def scrape_category(category, subcategories):
    for subcategory in subcategories:
        first_page_url = f'https://www.tamata.com/{category}/{subcategory}.html'
        response = requests.get(first_page_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        total_pages = get_total_pages(soup)

        for page in range(1, total_pages + 1):
            url = f'{first_page_url}?page={page}'
            scrape_page(url)
            time.sleep(1)  # Delay to be respectful of the server

categories = {
    'beauty-health': ['makeup/brushes', 'fragrance', 'shaving-hair-removal'],
    'electronics': ['laptops-computers', 'mobile-tablet', 'headphones'],
    }

# Start scraping
for category, subcategories in categories.items():
    scrape_category(category, subcategories)
