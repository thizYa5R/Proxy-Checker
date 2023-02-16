import requests
import threading

def check(proxy, ptype, semaphore):
    if ptype == 'socks5' or ptype == 'socks4':
        proxy = f'{ptype}://{proxy}'
    try:
        semaphore.acquire()
        print(f'[+] {proxy}')
        response = requests.get('https://www.google.com', proxies={'http':proxy,'https':proxy}, timeout=5)
        if response.status_code == 200:
            with open('working_proxies.txt','a') as file:
                file.write(f'{proxy}\n')
    except:
        pass
    finally:
        semaphore.release()

proxy_file = input('Enter the path to the proxies file: ')
ptype = input('Enter the type of proxies(http,socks5,socks4): ')


# Set maximum number of threads
max_threads = int(input('Enter the max number of proxies to be checked at once: ')) 
threads = []
semaphore = threading.Semaphore(max_threads)

#Asking the user for clearing the hits if he wants to
clear_hits = input('Do you want to clear the old hits?(yes or no) ')
if clear_hits == 'yes':
    with open('working_proxies.txt','w') as clear:
        pass


with open(proxy_file,'r') as proxies:
    for proxy in proxies:
        proxy = proxy.rstrip()
        Thread = threading.Thread(target=check,args=(proxy,ptype,semaphore))
        Thread.start()
        threads.append(Thread)

for thread in threads:
    thread.join()
    
print('Done!')
