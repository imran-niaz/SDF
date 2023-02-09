import socket
import sys
import time

def resolve(domain):
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except:
        return None

def dns_map(domain):
    ip = resolve(domain)
    subdomains = []
    if ip:
        print("[+] Resolved " + domain + " to " + ip)
        parts = domain.split(".")
        for i in range(1, len(parts)):
            subdomain = ".".join(parts[:-i]) + "."
            subdomain_ip = resolve(subdomain)
            if subdomain_ip:
                subdomains.append((subdomain, subdomain_ip))
                print("[+] Resolved subdomain " + subdomain + " to " + subdomain_ip)
            else:
                print("[-] Failed to resolve subdomain " + subdomain)
    else:
        print("[-] Failed to resolve " + domain)
    return subdomains

def dns_brute_force(domain):
    chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    for c1 in chars:
        for c2 in chars:
            subdomain = c1 + c2 + "." + domain
            subdomain_ip = resolve(subdomain)
            if subdomain_ip:
                print("[+] Found subdomain " + subdomain + " with IP address " + subdomain_ip)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        domain = input("Enter a domain name: ")
    else:
        domain = sys.argv[1]
    start = time.time()
    subdomains = dns_map(domain)
    end = time.time()
    print("[+] Total time taken for DNS resolution: " + str(end - start) + " seconds")
    choice = input("Do you want to perform a brute force search for subdomains? (yes/no): ")
    if choice == "yes":
        start = time.time()
        dns_brute_force(domain)
        end = time.time()
        print("[+] Total time taken for brute force search: " + str(end - start) + " seconds")
