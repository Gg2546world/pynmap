import socket

def network_scan(ip_range,port=80):
    """scan one ip """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)

    try:
        sock.connect((ip_range, port))
        return f"~ {ip_range} : IS EXIST"
    except socket.timeout:
        return None
    except ConnectionRefusedError:
        return f"~ {ip_range} : IS EXIST"
    except Exception:
        return None
    finally:
        sock.close()
