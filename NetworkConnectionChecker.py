import socket


def check_network(host, port):
    try:
        socket.create_connection((host, port), timeout=5)
        return True
    except OSError:
        return False


def check_internet_connection():
    # We will try to connect to a well-known public host
    host_name = "example.com"
    port_number = 80

    if check_network(host_name, port_number):
        return True
    else:
        return False


def resolve_ip_address(host):
    try:
        ip_address = socket.gethostbyname(host)
        return ip_address
    except socket.gaierror:
        return None


def scan_ports(host, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        if check_network(host, port):
            open_ports.append(port)
    return open_ports


def main():
    print("Welcome to the Network Connection Checker!")
    print("1. Check specific host and port")
    print("2. Check internet connection")
    print("3. Resolve IP address of a host")
    print("4. Scan ports of a host")
    print("5. Exit")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        # Check specific host and port
        host_name = input("Enter the host name: ")
        port_number = int(input("Enter the port number: "))

        if check_network(host_name, port_number):
            print("=" * 32)
            print("* Network connection available *")
            print("=" * 32)
        else:
            print("=" * 36)
            print("* Network connection not available *")
            print("=" * 36)

    elif choice == 2:
        # Check internet connection
        if check_internet_connection():
            print("=" * 32)
            print("* Internet connection available *")
            print("=" * 32)
        else:
            print("=" * 36)
            print("* Internet connection not available *")
            print("=" * 36)

    elif choice == 3:
        # Resolve IP address of a host
        host_name = input("Enter the host name: ")
        ip_address = resolve_ip_address(host_name)
        if ip_address:
            print(f"IP address of {host_name}: {ip_address}")
        else:
            print(f"Could not resolve IP address for {host_name}")

    elif choice == 4:
        # Scan ports of a host
        host_name = input("Enter the host name: ")
        start_port = int(input("Enter the start port number: "))
        end_port = int(input("Enter the end port number: "))
        open_ports = scan_ports(host_name, start_port, end_port)

        if open_ports:
            print(f"Open ports on {host_name}: {', '.join(map(str, open_ports))}")
        else:
            print(f"No open ports found on {host_name}")

    elif choice == 5:
        print("Exiting the Network Connection Checker.")
        return

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
