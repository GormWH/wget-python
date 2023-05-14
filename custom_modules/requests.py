# requests.py

from urllib.parse import urlparse
import socket
import ssl


def send_request(url:str):
    # parse url
    parsed_url = urlparse(url)
    scheme = parsed_url.scheme
    host = parsed_url.hostname
    path = parsed_url.path
    port = 80 if scheme == "http" else 443

    # create and connect client socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if scheme == "https":
        context = ssl.create_default_context()
        client = context.wrap_socket(client, server_hostname=host)
    client.settimeout(5)
    client.connect((host, port))

    # create request
    request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\n\r\n"
    
    # send request
    client.send(request.encode())

    # receive response
    response = bytearray()
    try:
        while True:
            data = client.recv(4096)
            if not data:
                break
            response.extend(data)
    except socket.timeout:
        # handle timeout error
        pass
        #print("Error: Request timed out")

    client.close()

    return response
