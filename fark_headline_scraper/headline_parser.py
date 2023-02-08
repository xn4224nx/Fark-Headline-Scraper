"""
Headline Parser

Functions to extract structured data from raw html pages.
"""

from .utilities import dir_check, load_all_json_in_dir, load_json, \
    get_webpage_html, connected_to_internet, is_website_up, save_json
from .html_parsing import findall_href, extract_headline_row


def headline_parser(start_page_url="https://www.fark.com/archives/"):
    """
    Function to extract all the headlines and their metadata from the Fark.com
    site.

    :param start_page_url: The Fark URL archive to start searching.
    :type start_page_url: str
    :return:
    """

    # Check that the folders to store the data exist
    for dir_ in ["scraped_data", "program_info"]:
        if not dir_check(dir_):
            raise Exception(f"The folder {dir_} "
                            f"could not be found or created.")

    # Load the old data files
    visited_webpages = load_json("program_info/visited_webpages.JSON", False)
    headline_data = load_json("program_info/headlines.JSON", False)
    websites_to_visit = list(load_json("program_info/websites_to_visit.JSON",
                                       False))

    # Add the base archive url to the list of website to visit
    if start_page_url not in websites_to_visit:
        websites_to_visit.append(start_page_url)

    # Scrape the site for site headline pages
    while websites_to_visit:

        # Save All Data to Disk
        save_json(visited_webpages, "program_info/visited_webpages.JSON")
        save_json(headline_data, "program_info/headlines.JSON")
        save_json(websites_to_visit, "program_info/websites_to_visit.JSON")

        if not connected_to_internet() or not is_website_up(start_page_url):
            break

        # Pick a websites_to_visit
        url = websites_to_visit.pop()

        # Load the html for the webpage
        raw_html_text = get_webpage_html(url)

        # Extract all links on the page
        websites_to_visit += findall_href(raw_html_text, url)

        # Remove duplicates
        websites_to_visit = list(set(websites_to_visit))

        # See if there are any headlines on the page
        new_headlines = extract_headline_row(raw_html_text)
        headline_data = {**headline_data, **new_headlines}
