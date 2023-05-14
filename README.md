# wget-python

This repo is a practice for implementing 'wget' like proformance with Python without using http modules(for example, 'requests' module).

- Dev environment: Ubuntu(22.04.2 LTS)
- Programming language: Python(3.11.2)
- Required python modules:

## usage

This program downloads HTML content of the 'url' and it's inner links, where the 'url' is given by the user.

Below is the execution command for this program.
```bash
$ python main.py <url>
```

Above command will download html contents to the `./downlads/<domain>` directory, where `<domain>` is the domain name of the input url.
