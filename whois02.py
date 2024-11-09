import socket

def whois_query(domain):
    try:
        # Connect to the IANA WHOIS server to get the TLD WHOIS server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(("whois.iana.org", 43))
            s.send(f"{domain}\r\n".encode())
            response = s.recv(4096).decode()

        # Extract the WHOIS server from the response
        if "whois:" in response:
            whois_server = response.split("whois:")[1].split("\n")[0].strip()
            return query_whois_server(domain, whois_server)
        
        return response
    
    except Exception as e:
        return f"Error: {e}"

def query_whois_server(domain, whois_server):
    try:
        # Connect to the domain-specific WHOIS server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((whois_server, 43))
            s.send(f"{domain}\r\n".encode())
            response = s.recv(4096).decode()
        return response

    except Exception as e:
        return f"Error querying {whois_server}: {e}"

if __name__ == "__main__":
    domain = input("Enter domain (e.g., example.com): ")
    print("\nWHOIS Information:\n", whois_query(domain))
