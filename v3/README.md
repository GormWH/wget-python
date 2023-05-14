# wget-python: **Version3**

## Summary

In version3, wget-python will get response message and download the HTML content to the `../downloads/<domain>` directory.  
Moreover, version3 seeks for all the internal links within the depth of 3.  
And downloads all the html contents of found links.

## Problems of version2

1. Version2 only seeks for internal links of depth 1  
2. Duplicate links  
2. Each request takes 5 seconds to close connection  

## Improvements

Version3 on the other hand,
1. Seeks for nested links of depth 3
2. Use 'set' data structure
2. implementation of multy threading

