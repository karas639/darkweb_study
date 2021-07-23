from stem import Signal
from stem.control import Controller
import requests

with Controller.from_port(port = 9051) as c:
    c.authenticate()
    c.signal(Signal.NEWNYM)

# use tor proxy
proxies = {
        'http': 'socks5://127.0.0.1:9050',
        'https': 'socks5://127.0.0.1:9050'
    }

x = requests.get('https://api.ipify.org', proxies=proxies).text
print(x)


'''
url = 'http://icanhazip.com/'

proxies = {
            'http': 'socks5://127.0.0.1:9050',
                'https': 'socks5://127.0.0.1:9050',
                }

res = requests.get(url, proxies=proxies)
print(res.text)
'''
