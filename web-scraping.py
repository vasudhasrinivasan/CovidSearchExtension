import requests
from bs4 import BeautifulSoup
import nltk
import re

URL = "https://www.noodles.com/covidupdate/"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')

def find_by_label():
    find = soup.findAll(text="COVID")
    return find

sentences = nltk.sent_tokenize(r.text)
result = [sentence for sentence in sentences if "COVID" in sentence]
print(result)
find_by_label()

if 'covid' in r.text:
    print("This is available")
else:
    print("Not available")
