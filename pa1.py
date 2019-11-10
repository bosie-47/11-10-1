import requests
import urllib3
from bs4 import BeautifulSoup
http = urllib3.PoolManager()
quote_page = http.request('GET',"https://blog.snowstar.org/")
page = (quote_page.data.decode())
soup = BeautifulSoup(page,'html.parser')
head_box = soup.find('header',attrs={'class':'entry-header'})
head = head_box.text.strip()



date_box = soup.find('span',attrs={'class':'posted-date'})
date = date_box.text.strip()

author_box = soup.find('span',attrs={'class':'posted-author'})
author = author_box.text.strip()

summary_box = soup.find('p')
summary = summary_box.text.strip()

data=[head,date,author,summary]
print (data)

from flask import Flask
app=Flask(__name__)
@app.route('/')
def onpage():
    return data
if __name__=='__main__':
    app.run()
