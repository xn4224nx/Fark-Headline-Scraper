"""
Unit Test Functions

Script full of tests to test each created function in the module.
"""

import pytest

from ..utilities import *
from ..html_parsing import *


def test_connected_to_internet():

    # Just test that it returns true
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
    with open(r"fark_headline_scraper\unit_tests\test_data\links.txt") as f:
        data = f.read()

    # If this fails check the test data not the function
    assert isinstance(data, str)

    links = findall_href(data)

    assert isinstance(links, list)

    assert all([isinstance(link, str) for link in links])

    assert len(links) == 10

    assert '/news/uk-england-64515347' in links


def test_extract_headline_row():

    # Load the test data
    with open (r"fark_headline_scraper\unit_tests\test_data\webpage.txt") as f:
        data = f.read()

    # If this fails check the test data not the function
    assert isinstance(data, str)

    headlines = extract_headline_row(data)

    assert isinstance(headlines, dict)

    assert all([isinstance(y, dict) for x,y in headlines.items()])

    assert len(headlines) == 240

    assert '23357' in headlines


def test_dir_check():

    # This directory should exist
    assert dir_check(r"fark_headline_scraper\unit_tests\test_data", False)

    # This should not
    assert not dir_check(r"fark_headline_scraper\unit_tests\not_exist", False)

def test_load_json():

    data = load_json(r"fark_headline_scraper\unit_tests\test_data\test0.json")

    assert isinstance(data, dict)
    assert len(data) == 5
    assert "00" in data
    assert "File" in data["20"]

def test_load_all_json_in_dir():

    data = load_all_json_in_dir(r"fark_headline_scraper\unit_tests\test_data")

    assert isinstance(data, dict)
    assert len(data) == 15
    assert "00" in data
    assert "File" in data["20"]