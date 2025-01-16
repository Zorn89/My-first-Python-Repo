import socket

hostname = "example.com"
ip_address = socket.gethostbyname(hostname)
print(f"Die IP-Adresse von {hostname} ist {ip_address}")


import os
import platform

def ping(host):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = f"ping {param} 4 {host}"
    return os.system(command)

host = "google.com"
ping(host)


import os
import platform

def ping(host):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = f"ping {param} 4 {host}"
    return os.system(command)

# Get the hostname from user input
host = input("Enter the hostname or IP address to ping: ")
ping(host)