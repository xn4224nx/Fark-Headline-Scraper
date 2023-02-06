"""
Utility Functions

Functions universal to this project to perform general tasks needed by a
diverse set of functions.

"""

import socket
import requests
import os


def connected_to_internet() -> bool:
    """
    Test if the computer is connected to the internet.

    :return: is there is a functioning internet connection.
    rtype: bool
    """
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("1.1.1.1", 53))
        return True

    except OSError:
        pass

    return False


def is_website_up(website_url: str) -> bool:
    """
    Check that a website is up and still available.

    :param website_url: The website to check
    :type website_url: str
    :return: Is the website functioning and communicating with this computer
    rtype: bool
    """
    try:
        requests.get(website_url)
        return True

    except requests.exceptions.ConnectionError:
        pass

    return False


def get_webpage_html(website_url: str) -> str:
    """
    Get the raw html text of a webpage

    :param website_url: The website to get the raw html text from
    :type website_url: str
    :return:
    rtype: str
    """

    raw = requests.get(website_url).text

    return raw


def dir_check(dir_fp: str, create=True) -> bool:
    """
    Check if a folder at `dir_fp` exists and if not create it.

    :param dir_fp: File path of the directory to create.
    :type dir_fp: str

    :param create: Should a folder be created if they don't exist?
    :type create: bool

    :return: Has the folder been found or created?
    rtype: bool
    """

    # Does the folder exist
    if os.path.isdir(dir_fp):
        return True

    # If not create it
    elif create:
        os.makedirs(dir_fp, exist_ok=True)
        return True

    # Otherwise indicate it doesn't exist
    else:
        return False
