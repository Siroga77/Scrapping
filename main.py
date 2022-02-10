import socket
from requests import get

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
public_ip = get('http://api.ipify.org').text
print(".......................")
print(f'Host: {hostname}')
print(f'Local iP: {local_ip}')
print(f'Public iP: {public_ip}')
ent = input("Press \"e: \"")
if ent == "e":
    break