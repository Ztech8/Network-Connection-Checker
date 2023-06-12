# Network Connection Checker

This Python script allows you to check the availability of a network connection by attempting to establish a connection to a specified host and port.

## Prerequisites

- Python 3.x

## Usage

1. Clone or download the repository to your local machine.
2. Open a terminal or command prompt and navigate to the directory where the script is located.

### Running the Script

1. Run the script by executing the following command:

   ```bash
   python network_connection_checker.py
   ```

2. Enter the host name when prompted. This can be the IP address or domain name of the target host.
3. Enter the port number when prompted. This should be the port on which the connection will be attempted.

### Result

- If a network connection can be established successfully, the following message will be displayed:

  ```
  ================================
  * Network connection available *
  ================================
  ```

- If a network connection cannot be established, the following message will be displayed:

  ```
  ===================================
  * Network connection not available *
  ===================================
  ```

## How It Works

The script uses the `socket` module in Python to attempt to create a connection with the specified host and port. It checks whether an `OSError` exception occurs while creating the connection. If an exception occurs, it indicates that the network connection is not available. Otherwise, it assumes that a network connection can be established successfully.

The `check_network()` function takes a host name (string) and port number (integer) as parameters. It attempts to create a connection to the specified host and port using `socket.create_connection()`. If the connection is established within a timeout of 5 seconds, it returns `True`, indicating a successful network connection. Otherwise, it returns `False`.

The user is prompted to enter the host name and port number. The script calls the `check_network()` function with the provided values. Based on the return value, it prints the appropriate message indicating the availability of the network connection.

## Customization

You can modify the code to suit your specific needs:

- Adjust the timeout value (`timeout=5`) in the `socket.create_connection()` function to change the duration for establishing a connection.
- Customize the messages displayed in the script to match your requirements.

Feel free to modify and integrate this code into your own projects as needed.
