#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

url = "https://www.cnn.com/2019/06/03/politics/jared-kushner-axios/index.html"
resp = requests.get(url)

soup = BeautifulSoup(resp.text, 'html.parser')
print(soup.prettify())

from goose3 import Goose
g = Goose()
article = g.extract(url='https://www.cnn.com/2019/06/03/politics/jared-kushner-axios/index.html')
print(article.cleaned_text)
g.close()