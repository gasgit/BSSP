import pandas as pd
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import webbrowser

res = requests.get("https://en.wikipedia.org/wiki/List_of_colors:_A-F")
soup = BeautifulSoup(res.content,'lxml')
table = soup.find_all('table',{'class':'wikitable sortable'})[0] 
df = pd.read_html(str(table))
print( tabulate(df[0], headers='keys', tablefmt='sql') )

webbrowser.open('https://en.wikipedia.org/wiki/List_of_colors:_A-F')




