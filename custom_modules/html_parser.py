# html_parser.py 

from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin


def extract_internal_links(url:str, html:str):
    """
    Extract all internal links from HTML content that point to the same domain as the given URL.

    Given
    url: The URL whose domain is used as the reference for internal links.
    html: The HTML content from which to extract internal links.
    
    Return
    return: A list of internal links.
    """

    # Extract the domain from the given URL.
    domain = urlparse(url).hostname

    # Parse the HTML content using BeautifulSoup.
    soup = BeautifulSoup(html, 'html.parser')

    # Use a list comprehension to extract internal links.
    parsed_url_list = [urlparse(urljoin(url,atag.get('href'))) for atag in soup.find_all('a', href=True)]
    internal_links = [f"{parsed_url.scheme}://{parsed_url.hostname}{parsed_url.path}" for parsed_url in parsed_url_list
                      if parsed_url.hostname == domain]

    return internal_links

def get_atag_href(html):
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find all <a> tags and extract their href attributes
    hrefs = [a['href'] for a in soup.find_all('a', href=True)]

    # Print the href attributes
    return hrefs

