# -*- coding: utf-8 -*-
# related url : https://jarroba.com/anonymous-scraping-by-tor-network/
__author__ = 'Dongwook Kim'

import time
import urllib2
import requests
from stem import Signal
from stem.control import Controller

class connect_mg:
    def __init__(self):
        self.new_ip = "0.0.0.0"
        self.old_ip = "0.0.0.0"
        self.new_identity()

    def _get_connection(self):
        with Controller.from_port(port = 9051) as c:
        #c.authenticate(password="58C49D9DA1EE2E7660AD4EB10F67D5107985C53F37FC94C68C6A21EBDB")
        c.authenticate(password='your password set for tor controller port in torrc')
        print("Success!")
        c.signal(Signal.NEWNYM)
        print("New Tor connection processed")
        c.close()

# use tor proxy
    def request(self, url):
        try:
            proxies = {
                'http': 'socks5://127.0.0.1:9050',
                'https': 'socks5://127.0.0.1:9050'
                }
            x = requests.get(url, proxies=proxies).text
            print(x)

'''
url = 'http://icanhazip.com/'
res = requests.get(url, proxies=proxies)
print(res.text)
'''

