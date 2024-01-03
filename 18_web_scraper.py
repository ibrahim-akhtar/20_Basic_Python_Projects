# Project 18
# Web Scraper (Extracting data from a website)

# pip install requests <done in project 17>
# pip install bs4

import requests
from bs4 import BeautifulSoup

url = 'https://www.codewithtomi.com/'
r = requests.get(url)
print("response:", r)   # if its 200, the its alright
soup = BeautifulSoup(r.content, 'lxml')
print(1+1)
# for this you better watch the video https://www.youtube.com/watch?v=pdy3nh1tn6I
title = soup.find_all('h2', {'class':'post-title'})

t = title[0].getText()
print(t)

"""
or
for t in title:
    print(t.getText())
"""

# this program isn't working for me