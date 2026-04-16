import socket
import errno

def port_scan(ip,port):
    """scan one port"""

    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.settimeout(2)

    port_status = sock.connect_ex((ip,port))

    try:

        if port_status == 0:

            try:
                service = socket.getservbyport(port,"tcp,")
            except:
                service = "unknown"

            return f"port : {port} ({service}) is open"
    
        elif port_status == errno.ECONNREFUSED:

            return None

        elif port_status in (errno.EHOSTUNREACH, errno.ENETUNREACH, errno.ETIMEDOUT):

            try:
                 service = socket.getservbyport(port,"tcp,")
            except:
                service = "unknown"

            return f"port : {port} ({service}) is filtred (or None response)"
    
        else:

            try:
                 service = socket.getservbyport(port,"tcp,")
            except:
                service = "unknown"

            return f"port : {port} ({service})  has a unknow Error"

    finally:
        sock.close()
