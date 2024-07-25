import requests
from bs4 import BeautifulSoup


def scraper(url):

    try:

        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for non-200 status codes

        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.find("title").text.strip()
        quotes = soup.find_all("span", class_="text")
        quotes = [ quote.text.strip() for quote in quotes]
        output = {
            "title": title,
            "quotes": quotes
            }
        return output

    except requests.exceptions.RequestException as e:
        print("An error occured during request: {e}")
        return None


target_url = "https://quotes.toscrape.com"
result = scraper(target_url)
print(result)
