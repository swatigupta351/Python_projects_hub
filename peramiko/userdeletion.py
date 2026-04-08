# Objective : Automate the safe deletion of an unused user from a remote Linux server.

# Pre-check Conditions

# Verify if the user exists in /etc/passwd.
# Ensure the user’s shell is /sbin/nologin.
# Confirm no active processes are running under the user.

# Execution Logic
# If user does not exist → Exit with message ( user is not exist )
# If shell is not /sbin/nologin → Do not proceed. exit with message ("User shell is NOT '/sbin/nologin" )
# If processes are running → Do not proceed. exit with message  ("processes are running")
# If all conditions satisfied → Delete user.

# Post-check
# Verify user deletion using id <username>.


import paramiko

#  Multiple servers list
servers = [
    {"host": "13.233.142.80", "user": "ec2-user", "key": "/home/swati/swati_projects/terraform-project/tf-key.pem"},
    {"host": "13.234.59.10", "user": "ec2-user", "key": "/home/swati/swati_projects/terraform-project/tf-key.pem"},
    {"host": "52.66.207.82", "user": "ec2-user", "key": "/home/swati/swati_projects/terraform-project/tf-key.pem"},
    {"host": "13.232.195.18", "user": "ec2-user", "key": "/home/swati/swati_projects/terraform-project/tf-key.pem"},
    {"host": "13.233.207.167", "user": "ec2-user", "key": "/home/swati/swati_projects/terraform-project/tf-key.pem"},
]

TARGET_USER = "testuser" # username for deletion 


# Reusable function to run command
def run_command(client, command):
    try:
        stdin, stdout, stderr = client.exec_command(command)
        output = stdout.read().decode().strip()
        error = stderr.read().decode().strip()
        return output, error
    except Exception as e:
        return "", str(e)


# Process each server
def process_server(server):
    print("\n==============================")
    print(f"Connecting to {server['host']}")

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # auto trust to server server new h allow automatically 

    connected = False

    # Connection try
    try:
        client.connect(
            hostname=server["host"],
            username=server["user"],
            key_filename=server["key"]
        )
        print("Connection established")
        connected = True

    except Exception as e:
        print(f"Connection failed: {e}")

# if server is not connected 
    if not connected:
        print("Skipping this server\n")
        return # return from this function

    #  Main logic to check user exist or not 
    try:
        print(f"Checking if user '{TARGET_USER}' exists...")
        output, error = run_command(client, f"id {TARGET_USER}")

        if error:
            print(f"User '{TARGET_USER}' does NOT exist. No action required.")
            return

        print(f"User '{TARGET_USER}' exists")

        # Shell check
        print(" Checking user shell...")
        output, _ = run_command(client, f"grep {TARGET_USER} /etc/passwd") # _ this variable use for ignore the value 

        if "/sbin/nologin" not in output:
            print("Shell is NOT /sbin/nologin")
            return

        print("Shell is /sbin/nologin")

        # Process check
        print("Checking running processes...")
        output, _ = run_command(client, f"ps -u {TARGET_USER}")

        if len(output.split("\n")) > 1: # .split("\n") lines ko list m todta h , list lenth 
            print("Active processes found. Cannot delete user.")
            return

        print("No active processes")

        # Delete user
        print(f"Deleting user '{TARGET_USER}'...")
        run_command(client, f"sudo userdel {TARGET_USER}")

        # Verify deletion
        print("Verifying deletion...")
        _, error = run_command(client, f"id {TARGET_USER}")

        if error:
            print(f"User '{TARGET_USER}' deleted successfully")
        else:
            print(f"User '{TARGET_USER}' still exists")

    except Exception as e:
        print(f"Error during execution: {e}")

    finally:
        client.close()
        print("Connection closed")


# Loop all servers
for server in servers:
    process_server(server)
