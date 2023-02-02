"""
Utility Functions

Functions universal to this project to perform general tasks needed by a
diverse set of functions.

"""

import socket
import requests


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

    :param website_url:
    :return: Is the website functioning and communicating with this computer
    rtype: bool
    """
    try:
        requests.get(website_url)
        return True

    except requests.exceptions.ConnectionError:
        pass

    return False
