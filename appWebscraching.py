""" import requests
from bs4 import BeautifulSoup

response=requests.get("https://www.niet.co.in/")
html=response.content
soup=BeautifulSoup(html,'html.parser')
print(soup.prettify()) """

#Adding an title in the code
import requests
from bs4 import BeautifulSoup

response=requests.get("https://www.niet.co.in/")
html=response.content
soup=BeautifulSoup(html,'html.parser')
print(soup.title)
print(soup.title.string)
