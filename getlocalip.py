import socket
import os

hostname = socket.gethostname()

def get_all_ip_addresses():
    ip_list = []
    try:
        host_info = socket.gethostbyname_ex(hostname)
        ip_list.extend(host_info[2])
    except socket.gaierror as e:
        print(f"Error retrieving IP addresses: {e}")
    return ip_list

ips = get_all_ip_addresses()

print(f"Hostname: {hostname}")
print(f"IP Addresses: {', '.join(ips)}")
