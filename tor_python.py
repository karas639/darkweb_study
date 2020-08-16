import requests

x = requests.get('https://ident.me').text
print("Local IP :",x)

# use tor proxy
proxies = {
        'http': 'socks5://127.0.0.1:9050',
        'https': 'socks5://127.0.0.1:9050'
    }

# use tor proxy and access url
y = requests.get('https://ident.me', proxies=proxies).text
print("Current IP :",y)

#fake-UserAgent
from fake_useragent import UserAgent

headers = { 'User-Agent': UserAgent().random }
z = requests.get('https://haystakvxad7wbk5.onion.ws', proxies=proxies, headers=headers).text
print(z)



# Automation with cron
'''
import random, time
wait = random.uniform(0, 2*60*60)
time.sleep(wait)
'''
