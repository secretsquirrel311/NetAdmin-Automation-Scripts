import paramiko

def cisco_switch_scan(switch_ip, username, password):
    ''' This function takes the above arguments and will scan the identified switch ip for status of all ports'''
    # Secure Shell
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Try to connect to the switch
        client.connect(switch_ip, username=username, password=password)

        # Commands to be executed to show the port interface statuses
        stdin, stdout, stderr = client.exec_command("Show Interface Status")
        output = stdout.read().decode('utf-8')

        # Need to process the output of the code above
        print("Interface Status:")
        multi_string = output.splitlines() # Breaks up the multi-line strings into a list of lines (ports)

        for line in multi_string:
            if "Up" in line or "Down" in line:
                ports = line.split()
                if len(ports) >1:
                    interface_name = ports[0] # Get interface name
                    port_status = ports[1].strip()  # Get port status

                    # Print output of interface status
                    if "Up" in port_status:
                        print(f"{interface_name} is Open")
                    elif "Down" in port_status:
                        print(f"{interface_name} is Closed")
                    else:
                        print(f"{interface_name} status is unknown: {port_status}")

    except Exception as e:
        print(f"Error occured durring scan: {e}")
    finally:
        # Now its time to close the SSH connection established in the function
        client.close()

if __name__ == "__main__":
    # Enter the credentials we will pass to the switch
    switch_ip = "xxx.xxx.xxx.xxx"       # Enter your switch IP address
    username = "administrator"          # Enter your username
    password = "supersecretpassword"    # Enter your password

    cisco_switch_scan(switch_ip,username, password)
