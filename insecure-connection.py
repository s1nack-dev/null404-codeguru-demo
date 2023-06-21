# https://codeql.github.com/codeql-query-help/python/py-insecure-protocol/
import ssl
import socket


# Using the deprecated ssl.wrap_socket method
ssl.wrap_socket(socket.socket(), ssl_version=ssl.PROTOCOL_SSLv2)

# Using SSLContext
context = ssl.SSLContext(ssl_version=ssl.PROTOCOL_SSLv3)
