import socket

def check_network(host, port):
    try:
        socket.create_connection((host, port), timeout=5)
        return True
    except OSError:
        return False

host_name = input("Enter the host name: ")
port_number = int(input("Enter the port number: "))


if check_network(host_name, port_number):
    print("="*32)
    print("* Network connection available *")
    print("="*32)
else:
    print("="*36)
    print("* Network connection not available *")
    print("="*36)
