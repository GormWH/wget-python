# v3.py

import threading
from urllib.parse import urlparse
from custom_modules.requests import send_request
from custom_modules.html_parser import extract_internal_links

file_count = 0

def download_htmls_of_depth(url:str, directory_path:str, depth:int=0):
    visited_urls = set()

    target_urls = set()
    target_urls.add(url)

    for i in range(depth + 1):
        print("Current depth = ", i)
        htmls = download_htmls_from_urls(target_urls, directory_path)
        visited_urls.update(target_urls)
        tmp = set()
        for html_source_url, html in htmls.items():
            if not bool(html):
                continue
            internal_links = extract_internal_links(html_source_url, html)
            new_links = [link for link in internal_links if link not in visited_urls]
            tmp.update(new_links)
        target_urls = tmp

    
    for visited_url in visited_urls:
        print(visited_url)
    global file_count
    print(f"Total of {file_count} urls were downloaded")


def download_htmls_from_urls(urls:set, directory_path:str):
    threads = []
    results = {}

    # Limit the number of threads to 50
    max_threads = 100
    num_threads = min(len(urls), max_threads)

    # Use a semaphore to limit the number of active threads
    semaphore = threading.Semaphore(num_threads)

    def download_html_from_url_worker(url):
        try:
            semaphore.acquire()
            results[url] = download_html_from_url(url, directory_path)
        except Exception as e:
            print(f"Error downloading {url}: {e}")
        finally:
            semaphore.release()

    # start threads for each URL
    for url in urls:
        thread = threading.Thread(target=download_html_from_url_worker, args=[url])
        threads.append(thread)
        thread.start()

    # wait for all threads to finish
    for thread in threads:
        thread.join()

    return {k: v for k, v in results.items() if v} # filter empty htmls

def download_html_from_url(url:str, directory_path:str):
    """
    Given 'url' and a 'directory' for download,
    downloads the html content of a 'url' to the 'directory'
    """
    response = send_request(url)
    header_and_body = response.split(b"\r\n\r\n", 1)
    try:
        header = header_and_body[0].decode()
        if is_content_html(header):
            if len(header_and_body) < 2:
                html = ""
            else:
                html = header_and_body[1]

            if bool(html):
                html = html.decode()
                write_html_file(url, html, directory_path)
                print("Downloading: ", url)
                return html
            else:
                return ""
        
        
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
        global file_count
        file_count = file_count + 1


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