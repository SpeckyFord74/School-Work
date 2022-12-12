import socket
hostname = socket.getfqdn()
print("IP Address:",socket.gethostbyname_ex(hostname))
