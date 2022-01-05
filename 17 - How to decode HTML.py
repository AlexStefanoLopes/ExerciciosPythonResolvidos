import requests
from bs4 import BeautifulSoup
# r = "html.parser"

base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text)

for story_heading in soup.find_all(class_="story-heading"):
    if story_heading.a:
        print(story_heading.a.text.replace("\n", " ").strip())
    else:
        print(story_heading.contents[0].strip())

# Outra forma
import requests
import BeautifulSoup

url = 'http://www.nytimes.com/'
ttl_lst = []

soup = BeautifulSoup.BeautifulSoup(requests.get(url).text)
title = soup.findAll('h2', {'class': 'story-heading'})
for row in title:
    ttl_lst.append(row.text)

print(ttl_lst)