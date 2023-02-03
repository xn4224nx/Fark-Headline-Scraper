"""
Web Access Functions

Functions to access headline data on the website and download it in a raw
format.
"""

from bs4 import BeautifulSoup


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


