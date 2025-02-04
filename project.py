import socket
import datetime

# Test host IP addresses: 192.168.254.137, 192.168.254.137


def scan_ports(target_host):
    with open(f"scan_results_{target_host}.txt" ,"w") as file:
        start_time = datetime.datetime.now()
        file.write(f"Scan started at: {start_time}\n")
        file.write(f"Scanning host: {target_host}\n\n")

        open_ports: []
        try:
            for port in range(1, 1026):
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(0.5)
                    result = s.connect_ex((target_host, port))

                    if result == 0:
                        open_ports.append(port)
                        file.write(f"Port {port} is open. \n")


        except socket.gaierror:
            file.write("Error: Host name could not be resolved. \n")
        except socket.error:
            file.write("Error: Host is not available. \n")
        except Exception as e:
            file.write(f"An error occurred: {e}\n")

        end_time = datetime.datetime.now()
        total_time = end_time - start_time
        file.write(f"\nScan ended at: {end_time}\n")
        file.write(f"Total scan duration: {total_time}\n")

        if open_ports:
            print(f"Open ports on {target_host}: {open_ports}")
        else:
            print(f"No open ports found on {target_host} in the range 1-2025")

host = input("Enter a host to scan: ")
scan_ports(host)