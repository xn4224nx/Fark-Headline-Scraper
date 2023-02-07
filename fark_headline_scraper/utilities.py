"""
Utility Functions

Functions universal to this project to perform general tasks needed by a
diverse set of functions.

"""

import socket
import requests
import os
import pathlib
import json
import re


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


def load_json(json_fp: str, raise_for_missing=True) -> dict:
    """
    Load a *.JSON file from disk and return as a dictionary.

    :param json_fp: File path to the *.JSON file to load from disk.
    :type json_fp: str

    :param raise_for_missing: Should an error be raised for a missing file?
    :type raise_for_missing: bool

    :return: A dict of the loaded data or empty if not found
    """
    try:
        with open(json_fp, "r") as f:
            data = json.load(f)
    except OSError:

        if raise_for_missing:
            raise OSError(f"File '{json_fp}' was not found.")

        else:
            return {}

    return data


def load_all_json_in_dir(dir_fp: str, raise_for_missing=True) -> dict:
    """
    Find all *.JSON files in a directory load all of them and try and combine
    them and return one dict with all the JSONs combined.

    :param dir_fp: A file path to a directory of *.JSON files to combine.
    :type dir_fp: str

    :param raise_for_missing: Should an error be raised for a missing file?
    :type raise_for_missing: bool

    :return:
    rtype: dict
    """

    found_jsons = []
    loaded_jsons = []

    # Find all *.JSON files in the directory
    found_jsons = list(pathlib.Path(dir_fp).rglob("*.json"))

    # If none have been found raise exception
    if not found_jsons:
        if raise_for_missing:
            raise Exception(f"No *.JSON files found in the folder '{dir_fp}'.")
        else:
            return {}

    # Load each *.JSON from disk into a dict
    for file in found_jsons:
        loaded_jsons.append(load_json(file))

    # Combine all the dicts in the list `loaded_jsons` into one big dict
    comb_dict = {k: v for d in loaded_jsons for k, v in d.items()}

    return comb_dict
