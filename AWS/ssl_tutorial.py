import ssl
import socket
context = ssl.create_default_context()
conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname="www.python.org")
conn.connect(("www.python.org", 443))