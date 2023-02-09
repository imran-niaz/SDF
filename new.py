import dns.resolver

def get_ns_records(domain):
    try:
        answers = dns.resolver.resolve(domain, 'NS')
        ns_records = [record.to_text() for record in answers]
        print(f"[+] NS records for {domain}:")
        for record in ns_records:
            print(f"  {record}")
    except dns.resolver.NoAnswer:
        print(f"[-] Failed to resolve NS records for {domain}")
    except dns.resolver.NXDOMAIN:
        print(f"[-] {domain} does not exist")

def get_a_records(domain):
    try:
        answers = dns.resolver.resolve(domain, 'A')
        a_records = [record.to_text() for record in answers]
        print(f"[+] A records for {domain}:")
        for record in a_records:
            print(f"  {record}")
    except dns.resolver.NoAnswer:
        print(f"[-] Failed to resolve A records for {domain}")
    except dns.resolver.NXDOMAIN:
        print(f"[-] {domain} does not exist")

def get_possible_subdomains(domain):
    subdomains = []
    with open("subdomains.txt") as f:
        subdomains = [line.strip() + "." + domain for line in f]
    print(f"[+] Possible subdomains for {domain}:")
    for subdomain in subdomains:
        try:
            answers = dns.resolver.resolve(subdomain, 'A')
            print(f"  {subdomain} resolved to {answers[0]}")
        except dns.resolver.NoAnswer:
            print(f"  [-] Failed to resolve {subdomain}")
        except dns.resolver.NXDOMAIN:
            print(f"  [-] {subdomain} does not exist")

if __name__ == '__main__':
    domain = input("Enter a domain name: ")
    get_ns_records(domain)
    get_a_records(domain)
    get_possible_subdomains(domain)
