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
        print("No listings found on this page, stopping the script.")
        return

    with open('scraped_data.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if url.endswith('page=1'):  # Write headers only once
            writer.writerow(['Title'])  # Column headers, add more if needed

        for listing in listings:
            title = listing.find('a', class_='product-item-link').text.strip()
            writer.writerow([title])  # Write the data
            print(title)  # Print title

base_url = 'https://www.alibaba.com/product-detail/App-Remote-Control-Car-Rear-Windshield_1600961908271.html?spm=a2700.galleryofferlist.normal_offer.d_title.728e6d9bzyscAQ'
page = 1
max_pages = 5  # Set a limit for pages to scrape

while page <= max_pages:
    current_url = base_url + str(page)
    scrape_page(current_url)
    page += 1

print("Scraping completed.")

