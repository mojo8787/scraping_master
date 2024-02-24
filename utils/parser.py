from bs4 import BeautifulSoup

def parse_html(html_content):
    """
    Parses the HTML content using Beautiful Soup and returns the soup object.
    """
    return BeautifulSoup(html_content, 'html.parser')

def extract_product_info(soup, class_name):
    """
    Extracts product information from a soup object.
    This is a generic function; you might need to adjust it based on the actual HTML structure.
    """
    products = soup.find_all('div', class_=class_name)
    product_info = []
    for product in products:
        title = product.find('a', class_='product-item-link').get_text(strip=True)
        # Extract more information as needed
        product_info.append({'title': title})
    return product_info
