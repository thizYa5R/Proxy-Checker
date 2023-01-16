import requests
import threading

def check(proxy, http):
    if http == 'no':
        proxy = f'socks5://{proxy}'
    try:
        response = requests.get('https://www.google.com/', proxies={'http':proxy,'https':proxy}, timeout=10)
        if response.status_code == 200:
            with open('working_proxies.txt','a') as file:
                file.write(f'{proxy} \n')
    except:
        pass

proxy_file = input('Enter the path to the proxies file: ')
http = input('Are the proxies http?(yes or no) ')

with open(proxy_file,'r') as pf:
    for proxy in pf:
        proxy = proxy.rstrip()

        Thread = threading.Thread(target=check,args=(proxy,http))
        Thread.start()

print('Done')