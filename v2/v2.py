# v2.py

import os
from urllib.parse import urlparse
from custom_modules.requests import send_request
from custom_modules.html_parser import extract_internal_links

def download_htmls(url, directory_path):
    html = download_html_from_url(url, directory_path)
    internal_links = extract_internal_links(url, html)
    for link_url in internal_links:
        download_html_from_url(link_url, directory_path)


def download_html_from_url(url:str, directory_path:str):
    """
    Given 'url' and a 'directory' for download,
    downloads the html content of a 'url' to the 'directory'
    """
    response = send_request(url)
    header_and_body = response.split(b"\r\n\r\n", 1)
    try:
        header = header_and_body[0].decode()
        if len(header_and_body) < 2:
            html = ""
        else:
            html = header_and_body[1]

        if bool(html) and is_content_html(header):
            html = html.decode()
            write_html_file(url, html, directory_path)
            print("Downloading: ", url)
        
        return html
    except UnicodeDecodeError: # Sometimes this error occured. Wasn't able to handle right.
        print("Error:'utf-8' codec can't decode content in ", url)
        return ""



def is_content_html(header:str):
    """
    Given HTTP header string,
    returns a boolean indicating whether or not the response is of type "text/html".
    """
    # Split the header string into individual lines
    lines = header.strip().split('\r\n')
    
    # Loop through the lines until we find the Content-Type header
    for line in lines:
        if line.lower().startswith('content-type:'):
            # Extract the value of the Content-Type header
            content_type = line.split(':')[1].strip()
            # Check if the content type is "text/html"
            if content_type.startswith('text/html'):
                return True
            else:
                return False
    
    # If we reach this point, there was no Content-Type header
    return False

def write_html_file(url:str, html:str, directory_path:str):
    """
    Given an 'url', 'html', 'directory_path' (all strings),
    writes html file to the '<directory_path>/<filename>'
    """
    file_name = make_file_name(url)
    # Open file in write mode
    with open(f"{directory_path}/{file_name}", "w") as file:
        # Write HTML to file
        file.write(f"<!-- This file is generated from: {url} -->")
        file.write(html)


def make_file_name(url:str):
    """
    Given an 'url' string,
    returns 'filename' based on the path of the 'url'
    (example) www.hostname.com/dir1/dir2/htmlfile.html -> dir1_dir2_htmlfile.html
    """
    path = urlparse(url).path
    if not path or path == "/" or path == "":
        return "index.html"

    filename = path.replace("/","_")
    if filename.startswith("_"):
        filename = filename[1:]
    if not filename.endswith(".html"):
        filename = filename + ".html"
    return filename