#here is the code for scrapping all the links from any webpage using python libraries like urllib,BeautifulSoup,requests
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
from fake_useragent import UserAgent
url=input("Enter the url of the website of which the links you want to get:")
user_agent = UserAgent()
page = requests.get(url,headers={'user-agent':user_agent.chrome})
soup=BeautifulSoup(page.content,'html.parser')
#print("Here is the code of the website")
#print(soup.prettify())
print("These are the links present on this website:")
b=[]
for i in soup.find_all('a'):
    b.append(i.get('href'))
for j in b:
    print(j)
