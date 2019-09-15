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
        domains.append((get_domain_name(domain_key_val[d]), d))

    #Sort the domain names
    sorted_domains = sorted(domains)

    #Replace the sorted domain names with the correct URLs
    i = 0
    sorted_urls = []
    while i < len(sorted_domains)-1:

        #If the current domain is the same as the next domain
        if sorted_domains[i][0] == sorted_domains[i+1][0]:

            #Split both domains by '.' and save the last element in two variables
            #The last element will tell us whether the URL has only ended with .com, or
            #it has more information like port number etc.
            url1 = domain_key_val[sorted_domains[i][1]].split('.')[-1]
            url2 = domain_key_val[sorted_domains[i+1][1]].split('.')[-1]

            #Check if the URL ended with just 'com' or it has more information
            #Append to the sorted_urls only if it has more information
            if url1 != 'com':
                sorted_urls.append(domain_key_val[sorted_domains[i][1]])
            if url2 != 'com':
                sorted_urls.append(domain_key_val[sorted_domains[i+1][1]])
            i += 1
        else:
            sorted_urls.append(domain_key_val[sorted_domains[i][1]])
            i += 1

    return list(dict.fromkeys(sorted_urls))

if __name__ == "__main__":
    with open ('sample_urls.txt', 'r') as f:
        urls = f.readlines()

    #Strip the escape character
    urls = [url.strip('\n') for url in urls]

    print_list(sort_urls(urls))
