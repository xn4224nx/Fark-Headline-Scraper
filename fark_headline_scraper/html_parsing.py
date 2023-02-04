"""
Web Access Functions

Functions to access headline data on the website and download it in a raw
format.
"""

from bs4 import BeautifulSoup
import re

def findall_href(webpage_text: str) -> list[str]:
    """
    Find all the links on a webpage.

    :param webpage_text: The raw html text of a webpage.
    :type webpage_text: str
    :return: a list of the full urls of the discovered links
    rtype: list[str]
    """
    soup = BeautifulSoup(webpage_text, 'html.parser')

    urls = [x.get('href') for x in soup.find_all('a')]

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

    # Loop over all the headline rows
    for headline in soup.find_all("tr", {"class" : regex}):

        # Extract the topic
        print(headline.find("a", attrs={"title": True})["title"])

        # Extract the URL
        print(headline.find("a", attrs={"href": True})["href"])

        # Extract the number of comments
        print(headline.find(class_='headlineComments').text.strip())

        # Extract the headline text
        print(headline.find("span", class_="headline").text.strip())

        break