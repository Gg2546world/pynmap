import ipaddress

def ip_range(ip):
    """get ip range"""

    resulte = []

    network_ipadress_range = ipaddress.ip_network(ip,strict=False)

    for ip_list in network_ipadress_range.hosts():
        resulte.append(str(ip_list))

    return resulte

if __name__ == "__main__":
    print(ip_range("192.168.0.1/24"))
