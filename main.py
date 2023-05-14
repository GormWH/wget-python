# main.py

import sys, os
from custom_modules.utils import valid_url, create_download_directory
import v1.v1 as v1
import v2.v2 as v2
import v3.v3 as v3

if len(sys.argv) != 2:
    print(f"Usage: $ python {os.path.basename(__file__)} <url>")
    sys.exit(1)

url = sys.argv[1]
if not valid_url(url):
    raise ValueError("Invalid URL")

download_directory = create_download_directory(url, os.getcwd() + "/downloads")

print("Download directory = ", download_directory)

# version1: only downloads the contents in 'url'
# v1.download_html(url, download_directory)

# version2: downloads contents in 'url' and its internal links
# v2.download_htmls(url, download_directory)

# version3: downloads contetns in 'url' and its internal links to depth of 'depth'
v3.download_htmls_of_depth(url, download_directory, depth=3)

