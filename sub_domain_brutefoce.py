import dns.resolver

print(''' _____           _      _____               _               
/  __ \         | |    /  __ \             | |              
| /  \/ ___   __| | ___| /  \/_ __ __ _ ___| |__   ___ _ __ 
| |    / _ \ / _` |/ _ \ |   | '__/ _` / __| '_ \ / _ \ '__|
| \__/\ (_) | (_| |  __/ \__/\ | | (_| \__ \ | | |  __/ |   
 \____/\___/ \__,_|\___|\____/_|  \__,_|___/_| |_|\___|_| 
   ''')



wordlist_file = input('Enter Wordlist File: ')
domain = input('Enter the Target domain: ')

with open(wordlist_file, 'r') as wordlist:
    subdomains = wordlist.readlines()

resolver = dns.resolver.Resolver()
resolver.nameservers = ['8.8.8.8'] 
with open('output.txt', 'w') as output_file:
    for subdomain in subdomains:
        subdomain = subdomain.strip()
        hostname = subdomain + '.' + domain
        try:
            answers = resolver.query(hostname, 'A')
            for rdata in answers:
                output = f'{hostname} {rdata.address}'
                print(output)
                output_file.write(output + '\n')
                if len(subdomains) >= 200:
                    break
        except dns.exception.DNSException:
            pass
