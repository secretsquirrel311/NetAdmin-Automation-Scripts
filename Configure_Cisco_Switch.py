import paramiko
import time

def configure_cisco_switch(host, username, password, commands):
    # This function will create an SSH client instance
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Connect to the switch
        ssh.connect(hostname=host, username=username, password=password)
        print(f'Connected to {host}')

        # Open an interactive Session
        remote_connection = ssh.invoke_shell()
        time.sleep(1)

        #Enter enable mode
        remote_connection.send('enable\n')
        time.sleep(1)
        remote_connection.send(password + '\n')
        time.sleep(1)

        # Send config commands
        for command in commands:
            print(f'sending command: {command}')
            remote_connection.send(command + '\n')
            time.sleep(1)

        # Capture and show output after the commands are sent
        output = remote_connection.recv(65535).decode('utf-8')
        print(output)

    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        # This ends the SSH connection
        ssh.close()

if __name__ == "__main__":
    # Switch info
    switch_ip = 'xxx.xxx.xxx.xxx'       # Enter switches IPv4 address here
    username = 'admin'                  # Enter the switch username
    password = 'supersecretpassword'    # Enter switch password. This should also be the password for the enable command too

    # Config commands to send to the switch
    configure_commands = [
        'configure terminal',
        'hostname Switch1',
        'interface GigabitEthernet0/1',
        'description xxxxxxxx',
        'switchport mode trunk',
        'exit',
        'interface Vlan1',
        'ip address xxx.xxx.xxx.xxx yyy.yyy.yyy.yyy',       # IPv4 and then subnet
        'no shutdown',
        'exit',
        'exit',
        'write memory'
    ]

    # Configure the switch
    configure_cisco_switch(switch_ip,  username, password, configure_commands)
