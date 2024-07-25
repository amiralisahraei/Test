

import requests
from bs4 import BeautifulSoup

def scrape_product_info(url):
    """Scrapes product information from a given URL using requests and BeautifulSoup4.

    Args:
        url (str): The URL of the product page.

    Returns:
        dict: A dictionary containing the scraped product information,
              or None if scraping fails.

    Raises:
        requests.exceptions.RequestException: If an error occurs during the HTTP request.
    """

    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for non-200 status codes

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract product title, price, and description based on your target website's structure
        # Replace these selectors with the appropriate ones for your specific website
        title = soup.find('title').text.strip()
        # price = soup.find('span', class_='product-price').text.strip()
        # description = soup.find('div', class_='product-description').text.strip()

        # Create a dictionary to store the scraped information
        product_info = {
            'title': title
        }

        return product_info

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while scraping the URL: {e}")
        return None

# Example usage
target_url = 'https://quotes.toscrape.com'  # Replace with the actual URL
product_data = scrape_product_info(target_url)

if product_data:
    print(f"Title: {product_data['title']}")
else:
    print("Scraping failed or no product information found.")
