# Network Connection Checker

The Network Connection Checker is a Python script that allows users to perform various network-related tasks, such as checking a specific host and port, verifying internet connectivity, resolving the IP address of a host, and scanning open ports of a host.

## How to Use

1. Ensure you have Python installed on your system.

2. Clone or download the script from the GitHub repository.

3. Open a terminal or command prompt and navigate to the directory where the script is located.

4. Run the script using the following command:

```bash
python network_connection_checker.py
```

5. The script will display a menu with the following options:

   - Check specific host and port
   - Check internet connection
   - Resolve IP address of a host
   - Scan ports of a host
   - Exit

6. Choose the desired option by entering the corresponding number (1-5) and follow the prompts.

## Options

### 1. Check specific host and port

This option allows you to check if a specific host and port are reachable on the network.

### 2. Check internet connection

This option verifies if the script can connect to a well-known public host (e.g., example.com) and port (e.g., port 80) to determine internet connectivity.

### 3. Resolve IP address of a host

Enter the hostname, and the script will attempt to resolve its IP address.

### 4. Scan ports of a host

Enter the hostname and a range of ports to scan (start_port and end_port). The script will check for open ports within the specified range.

### 5. Exit

Choose this option to terminate the Network Connection Checker.

## Contributions

Contributions to the project are welcome. If you encounter any bugs or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## Disclaimer

This script is meant for educational and testing purposes only. Use it responsibly and only on systems you have permission to scan.
