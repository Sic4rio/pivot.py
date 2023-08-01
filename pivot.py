import subprocess
import threading
import paramiko
from colorama import Fore, Style

def ssh_remote_port_forwarding():
    try:
        victim_ip = input("Enter the victim IP address: ")
        local_port = input("Enter local port: ")
        remote_port = input("Enter remote port on the victim machine: ")
        subprocess.run(f"ssh -R {remote_port}:localhost:{local_port} user@{victim_ip}", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")

def dynamic_port_forwarding():
    try:
        victim_ip = input("Enter the victim IP address: ")
        ssh_username = input("Enter SSH username: ")
        local_port = input("Enter local port: ")

        # Construct the SSH command
        ssh_cmd = f"ssh -D 127.0.0.1:{local_port} {ssh_username}@{victim_ip}"

        # Execute the SSH command using subprocess
        subprocess.run(ssh_cmd, shell=True, check=True)

    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")

def ssh_local_port_forwarding():
    try:
        victim_ip = input("Enter the victim IP address: ")
        local_port = input("Enter local port: ")
        remote_port = input("Enter remote port on the victim machine: ")
        subprocess.run(f"ssh user@{victim_ip} -L {local_port}:127.0.0.1:{remote_port}", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")

def modify_proxychains_config():
    try:
        subprocess.run("sudo nano /etc/proxychains4.conf", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")

def sshuttle_vpn():
    try:
        victim_ip = input("Enter the victim IP address: ")
        subnet = input("Enter the subnet to forward (e.g., 172.16.2.0/24): ")
        ssh_key_path = input("Enter path to SSH key (or leave empty if password-based): ")

        ssh_cmd = f"ssh -i {ssh_key_path}" if ssh_key_path else "ssh"
        sshuttle_cmd = f"sshuttle -vvr {ssh_cmd} root@{victim_ip} {subnet}"

        subprocess.run(sshuttle_cmd, shell=True, check=True)

    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")

def display_banner():
    banner = r"""
⠀⢀⣠⣤⣤⣄⡀⠀             
⣴⣿⣿⣿⣿⣿⣿⣦  ┏┓•
⣿⣿⣿⣿⣿⣿⣿⣿  ┃┃┓┓┏┏┓╋ ┏┓┓┏
⣇⠈⠉⡿⢿⠉⠁⢸  ┣┛┗┗┛┗┛┗•┣┛┗┫
⠙⠛⢻⣷⣾⡟⠛⠋           ┛  ┛
⠀⠀⠀⠈⠁⠀⠀⠀     
"""

    print(f"{Fore.YELLOW}{banner}{Style.RESET_ALL}")

def display_help():
    help_menu = f"""
Options:
{Fore.RED}1. Perform SSH Remote Port Forwarding
   - This option allows you to forward a port on the victim machine back to the attacker machine.
   - You will be prompted to enter the victim IP address, local port, and remote port on the victim machine.

{Fore.GREEN}2. Perform Dynamic Port Forwarding
   - This option sets up dynamic port forwarding (SOCKS proxy) on the victim machine.
   - You will be prompted to enter the victim IP address, SSH username, and local port. (Make sure you have already edited the ProxyChains Config File.)

{Fore.BLUE}3. Modify ProxyChains Config File
   - This option opens the ProxyChains configuration file for editing using the 'nano' text editor.
   - Make necessary changes and save the file to use ProxyChains with your desired proxy settings.

{Fore.CYAN}4. SSH Local Port Forwarding
   - This option allows you to forward a port from the attacker machine to a port on the victim machine.
   - You will be prompted to enter the victim IP address, local port, and remote port on the victim machine.

{Fore.MAGENTA}5. Use SSHuttle VPN
   - This option creates a VPN connection from your machine to the victim machine via SSH.
   - You will be prompted to enter the victim IP address, the subnet to forward, and SSH authentication details.
     If using key-based authentication, leave the SSH password field empty.

{Fore.YELLOW}6. Exit
   - This option exits the script.
"""

    print(help_menu)

if __name__ == "__main__":
    try:
        display_banner()
        print("Select an option:")
        display_help()
        while True:
            choice = input("Enter your choice: ")

            if choice == "1":
                ssh_remote_port_forwarding()
            elif choice == "2":
                dynamic_port_forwarding()
            elif choice == "3":
                modify_proxychains_config()
            elif choice == "4":
                ssh_local_port_forwarding()
            elif choice == "5":
                sshuttle_vpn()
            elif choice == "6":
                break
            else:
                print(f"{Fore.RED}Invalid choice. Please try again.{Style.RESET_ALL}")

    except KeyboardInterrupt:
        print(f"{Fore.YELLOW}\nKeyboard interrupted. Exiting...{Style.RESET_ALL}")
