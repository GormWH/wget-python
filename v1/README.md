# wget-python: **Version1**

## Summary

In version1, wget-python will get response message and download the HTML content to the `../downloads/<domain>` directory.  
The downloading of internal links will be proformed in the later version.

## Structure

During the development of v1(version1), 3 new files were created.

1. `/custom_modules/requests.py`  
    Sends http request and recieve http response

2. `/custom_modules/utils.py`  
    Collection of utility functions

3. `/v1/v1.py`
    Main module of version1.  
    In `/main.py` `v1.v1.download_html(url, download_directory)` will be called.
