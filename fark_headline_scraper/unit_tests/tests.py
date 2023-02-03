"""
Unit Test Functions

Script full of tests to test each created function in the module.
"""

import pytest

from ..utilities import *
from ..html_parsing import *


def test_connected_to_internet():

    # Just test that is returns true
    assert connected_to_internet() is True


def test_is_website_up():

    # Is the Google website active
    assert is_website_up("https://www.google.com") is True

    # Check that a website that doesn't exist returns false
    assert is_website_up("https://thisisnotarealwebsiteatall.isit/") is False


def test_get_webpage_html():

    text = get_webpage_html("https://www.google.com")

    assert isinstance(text, str) is True

    # get known webpage and check that it contains a common html element
    assert "<head>" in text


def test_findall_href():

    # Load the test data
    with open(r"fark_headline_scraper\unit_tests\test_data\links.txt") as file:
        data = file.read()

    # If this fails check the test data not the function
    assert isinstance(data, str)

    links = findall_href(data)

    assert isinstance(links, list)

    assert all([isinstance(link, str) for link in links])

    assert len(links) == 10

    assert '/news/uk-england-64515347' in links
