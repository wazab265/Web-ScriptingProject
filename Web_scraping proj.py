import requests
import pprint
from bs4 import BeautifulSoup
res=requests.get('https://news.ycombinator.com/news?p=2')
soup=BeautifulSoup(res.text, 'html.parser')
votes=soup.select('.score')
links=soup.select('.storylink')

def custom_nletter(links,votes):
    hn=[]
    for idx,itm in enumerate(links):
        Title=links[idx].getText()
        href=links[idx].get('href',None)
        points=int(votes[idx].getText().replace(' points', ''))
        if points>50:
            hn.append({'title':Title,'link':href,'points':points})
    return hn


pprint.pprint(custom_nletter(links,votes))
