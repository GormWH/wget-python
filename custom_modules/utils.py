# utils.py

import os
from urllib.parse import urlparse

def valid_url(url:str):
    parsed_url = urlparse(url)
    valid_scheme = parsed_url.scheme == "http" or parsed_url.scheme == "https"
    valid_host = bool(parsed_url.hostname)
    return valid_scheme and valid_host

def create_download_directory(url:str, downloads_folder_path):
    host = urlparse(url).hostname
    # Define the directory name and path
    directory_name = host
    directory_path = f"{downloads_folder_path}/{directory_name}" 

    # Create the directory if it doesn't exist
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    
    return directory_path