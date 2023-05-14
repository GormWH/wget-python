# html_parser.py 

from bs4 import BeautifulSoup

def get_atag_href(html):
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find all <a> tags and extract their href attributes
    hrefs = [a['href'] for a in soup.find_all('a', href=True)]

    # Print the href attributes
    return hrefs

