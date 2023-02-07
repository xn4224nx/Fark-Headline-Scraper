"""
Web Access Functions

Functions to access headline data on the website and download it in a raw
format.
"""

from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import re


def findall_href(webpage_text: str, page_url: str) -> list[str]:
    """
    Find all the links on a webpage.

    :param webpage_text: The raw html text of a webpage.
    :type webpage_text: str

    :param page_url: The url of the original webpage
    :type page_url: str

    :return: a list of the full urls of the discovered links
    rtype: list[str]
    """
    soup = BeautifulSoup(webpage_text, 'html.parser')

    urls = [x.get('href') for x in soup.find_all('a')]

    # Extract the base URL
    url_split = urlparse(page_url)
    base_url = url_split.scheme + "://" + url_split.netloc

    # Repair partial URLs
    for i in range(len(urls)):
        if base_url not in urls[i]:
            urls[i] = base_url + urls[i]

    return urls


def extract_headline_row(webpage_text: str) -> dict:
    """
    Extract all the headline rows from the webpage text of a Fark webpage and
    return a dict of all the headline metadata.

    :param webpage:
    :type webpage_text: str
    :return: structured metadata of all the headlines in the webpage text
    rtype: dict
    """
    soup = BeautifulSoup(webpage_text, 'html.parser')

    regex = re.compile('.*headlineRow.*')

    headline_data = {}

    # Loop over all the headline rows
    for headline in soup.find_all("tr", {"class" : regex}):

        # Extract the article link
        headline_link = headline.find("a", attrs={"href": True})["href"]

        # Extract details from the link
        link_id = re.search(r"goto/(\d+)/", headline_link).group(1)
        article_root = re.search(r"/\d+/([a-zA-Z\.]+)", headline_link).group(1)

        headline_data[link_id] = {
            "Article Site": article_root,
            "Topic": headline.find("a", attrs={"title": True})["title"],
            "Comments": headline.find(class_='headlineComments').text.strip(),
            "Headline": headline.find("span", class_="headline").text.strip()
        }

    return headline_data
