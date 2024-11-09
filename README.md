# Whois-Query
These codes perform a WHOIS query for a given domain by connecting to a WHOIS server (whois.iana.org), 
sending the domain name, and receiving registration information about that domain. 
It then returns the raw WHOIS response as a string.

The second one is improved with the following features:
Statements for socket handling are used, ensuring the connection is properly closed automatically (Socket Management).
Basic error handling is kept to catch issues like network errors or domain formatting problems.
The code dynamically extracts the correct WHOIS server from the response if it's needed.
