def get_domain_name(url):
    var_split = url.split('/')
    var_split = var_split[2].split('.')
    return var_split[1]

def print_list(stuffs):
    for stuff in stuffs:
        print(stuff)

def sort_urls(urls):
    #Convert the urls to {index : url} pairs
    domain_key_val = {}
    for i in range(len(urls)):
        domain_key_val[i] = urls[i]

    #Filter out the domain names from the URL
    domains = []
    for d in domain_key_val:
        domains.append(get_domain_name(domain_key_val[d]))

    #Sort the domain names
    sorted_domains = sorted(domains)

    #Replace the sorted domain names with the correct URLs
    for i in range(len(sorted_domains)):
        idx = domains.index(sorted_domains[i])
        sorted_domains[i] = domain_key_val[idx]

    return sorted_domains

if __name__ == "__main__":
    with open('sample_urls', 'r') as f:
        urls = f.readlines()

    #Strip the escape character
    urls = [urls[i].strip('\n') for i in range(len(urls))]

    print_list(sort_urls(urls))
