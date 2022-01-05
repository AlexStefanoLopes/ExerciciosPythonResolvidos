#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import requests
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get("https://www.sikayetvar.com/onedio", headers = headers)

soup = BeautifulSoup(response.text, "html.parser")   #Use a parser to fix second error warning
pages = soup.select('div.pagination a')

a = int(pages[-2].text)
print(a)