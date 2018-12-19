import pandas as pd
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import webbrowser


# fetch web page content using the requests module
res = requests.get("https://en.wikipedia.org/wiki/List_of_colors:_A-F")
# parse and create bs object
soup = BeautifulSoup(res.content,'lxml')
# find first table by class name
table = soup.find_all('table',{'class':'wikitable sortable'})[0] 
# create  list 
df = pd.read_html(str(table))
# tabulate and display
print( tabulate(df[0], headers='keys', tablefmt='sql') )
# open wiki page with default webbrowser
webbrowser.open('https://en.wikipedia.org/wiki/List_of_colors:_A-F')




