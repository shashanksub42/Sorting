urls = []
with open('sample_urls', 'r') as f:
    line = f.readline()
    while line:
        urls.append(line)
        line = f.readline()
       
def get_domain_name(url):
    var_split = url.split('/')
    var_split = var_split[2].split('.')
    return var_split[1]




def print_list(stuffs):
    for stuff in stuffs:
        print(stuff)

domains = []
for url in urls:
    domains.append(get_domain_name(url))

sorted_domains = sorted(domains)
for i in range(len(sorted_domains)):
    for j in range(len(urls)):
        if sorted_domains[i] == get_domain_name(urls[j]):
            sorted_domains[i] = urls[j]

print_list(sorted_domains)

