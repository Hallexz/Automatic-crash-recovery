# Service Auto-Recovery Script

This Python script is designed to automatically monitor and restart a specified service if it stops running. It utilizes the `systemctl` command to check the status of the service and restart it if necessary.

## Prerequisites

- Python 3.x installed
- `sudo` access (for restarting the service)

## Usage

1. Save the Python script to a file (e.g., `service_recovery.py`).
2. Open a terminal and navigate to the directory containing the script.
3. Run the script with the following command:

   ```
   python service_recovery.py
   ```

4. When prompted, enter the name of the service you want to monitor and restart automatically.

The script will continuously check the status of the specified service every 60 seconds (this interval can be modified in the `auto_recovery` function). If the service is not active, it will attempt to restart the service and print a message indicating the action taken.

## Functions

- `check_service(service_name)`: Checks if the specified service is active using the `systemctl` command.
- `restart_service(service_name)`: Restarts the specified service using the `sudo systemctl restart` command.
- `auto_recovery(service_name, sleep_time=60)`: The main function that continuously monitors the service and calls the `restart_service` function if the service is not active. The `sleep_time` parameter specifies the interval (in seconds) between service status checks.

