"""
Unit Test Functions

Script full of tests to test each created function in the module.
"""

import pytest

from ..utilities import *


def test_connected_to_internet():

    # Just test that is returns true
    assert connected_to_internet() is True


def test_is_website_up():

    # Is the Google website active
    assert is_website_up("https://www.google.com") is True

    # Check that a website that doesn't exist returns false
    assert is_website_up("https://thisisnotarealwebsiteatall.isit/") is False
