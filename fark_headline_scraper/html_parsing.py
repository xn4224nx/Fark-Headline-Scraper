"""
Web Access Functions

Functions to access headline data on the website and download it in a raw
format.
"""

from bs4 import BeautifulSoup
from urllib.parse import urlparse
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

    # Repair partial archive URLs and remove URL's from outside the site
    ret_ls = []

    for i in range(len(urls)):

        # Remove Nones
        if urls[i] is None:
            continue

        # Fix archive links
        if re.match(r"\d{4}-\d{2}-\d{2}", urls[i]):
            ret_ls.append("https://www.fark.com/archives/" + urls[i])

        # # Remove Fark goto links
        # if "/goto/" in urls[i]:
        #     continue
        #
        # elif base_url in urls[i]:
        #     ret_ls.append(urls[i])

    return ret_ls


def extract_headline_row(webpage_text: str) -> dict:
    """
    Extract all the headline rows from the webpage text of a Fark webpage and
    return a dict of all the headline metadata.

    :param webpage_text:
    :type webpage_text: str
    :return: structured metadata of all the headlines in the webpage text
    rtype: dict
    """
    soup = BeautifulSoup(webpage_text, 'html.parser')

    regex = re.compile('.*headlineRow.*')

    headline_data = {}

    # Loop over all the headline rows
    for headline in soup.find_all("tr", {"class": regex}):

        try:
            # Extract the article link
            headline_link = headline.find("a", attrs={"href": True})["href"]

            # Extract details from the link
            link_id = re.search(r"goto/(\d+)/", headline_link).group(1)
            article_root = re.search(r"/\d+/([0-9a-zA-Z\.]+)",
                                     headline_link).group(1)

            headline_data[link_id] = {
                "Article Site": article_root,
                "Topic": headline.find("a", attrs={"title": True})["title"],
                "Comments": headline.find(class_='headlineComments'
                                          ).text.strip(),
                "Headline": headline.find("span", class_="headline"
                                          ).text.strip()
            }

        except AttributeError:
            pass

    return headline_data
