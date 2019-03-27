import bs4
import requests
import lxml
import re

static = "https://www.yourdictionary.com/"
def findWord(word):
    t1=''
    link = static + word
    req = requests.get(link)

    if(req.status_code == 200):
        soup = bs4.BeautifulSoup(req.text, 'lxml')
        t = soup.select('.sense')
        for i in t:
            t1 += i.text
        t1 = t1.split(".")
        return(t1[0] + '\n\n')
    else:
        print("Error")