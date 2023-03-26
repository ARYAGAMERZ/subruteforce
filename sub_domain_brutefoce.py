import dns.resolver

print(''' _____           _      _____               _               
/  __ \         | |    /  __ \             | |              
| /  \/ ___   __| | ___| /  \/_ __ __ _ ___| |__   ___ _ __ 
| |    / _ \ / _` |/ _ \ |   | '__/ _` / __| '_ \ / _ \ '__|
| \__/\ (_) | (_| |  __/ \__/\ | | (_| \__ \ | | |  __/ |   
 \____/\___/ \__,_|\___|\____/_|  \__,_|___/_| |_|\___|_| 
   ''')

wordlist_file = input('Enter Wordlist File (Compulsory): ')
domain = input('Enter the Target domain: ')
output_file_name = input('Enter the Output file name: ')

if not output_file_name.endswith('.txt'):
    output_file_name += '.txt'

with open(wordlist_file, 'r') as wordlist:
    subdomains = wordlist.readlines()

resolver = dns.resolver.Resolver()
resolver.nameservers = ['9.9.9.9'] 

with open(output_file_name, 'w') as output_file:
    for subdomain in subdomains:
        subdomain = subdomain.strip()
        hostname = subdomain + '.' + domain
        try:
            answers = resolver.query(hostname, 'A')
            for rdata in answers:
                output = f'https://{hostname}'
                print(output)
                output_file.write(output + '\n')
                if len(subdomains) >= 200:
                    break
        except dns.exception.DNSException:
            pass
