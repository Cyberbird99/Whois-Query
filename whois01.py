import socket

def whois_query(domain):
    
    # create a socket connection to the WHOIS server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the WHOIS server on port 43
    s.connect(("whois.iana.org", 43))

    # Send the domain name query to WHOIS server with a new line character
    s.send(f"{domain}\r\n".encode())

    # Receive the response from the WHOIS sever (buffer size 4096 bytes)
    response = s.recv(4096).decode()
    s.close()

    # return the WHOIS response
    return response

print(whois_query(("example.com")))