# wget-python

This repo is a practice for implementing 'wget' like proformance with Python without using http modules(for example, 'requests' module).

## Development environment
- Dev OS: Ubuntu(22.04.2 LTS)
- Programming language: Python(3.11.2)

# How to use

This program downloads HTML content of the 'url' and it's inner links, where the 'url' is a given input from the user.

- [Preparation](#preparation)
- [Execution](#execution)

## Preparation

1. Install python  
    As mentioned in the [beginning](#development-environment), you must have python installed.

2. Clone(or download) this repository

3. Install dependencies  
    Install required modules to execute the program.  
    `requirements.txt` contains the necessary packages.  
    ***You can install all the required packages with below command.***
```bash
$ pip install -r requirements.txt
```

## Execution

Below is the execution command for this program.  
In the `root` directory of this project, type below command.

```bash
$ python main.py <url>
```

Above command will download html contents to the `./downlads/<domain>` directory, where `<domain>` is the domain name of the input url.


