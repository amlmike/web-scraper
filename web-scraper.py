#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

url = "https://www.cnn.com/2019/06/03/politics/donald-trump-queen-elizabeth-ii-buckingham-palace-banquet/index.html"
resp = requests.get(url)

soup = BeautifulSoup(resp.text, 'html.parser')
