import bs4
import requests
import lxml
import re


# This is the API URL
static = "https://www.yourdictionary.com/"

# function to find a word.
def findWord(word):
    t1=''
    link = str(static) + word
    req = requests.get(link)

    # When SUCCESS
    if(req.status_code == 200):
        soup = bs4.BeautifulSoup(req.text, 'lxml')
        t = soup.select('.sense')
        for i in t:
            t1 += i.text
        t1 = t1.split(".")
        return(t1[0] + '\n\n')
    # When ERROR
    else:
        print("An Error has been encountered.")
