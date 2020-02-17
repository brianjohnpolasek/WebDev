import requests
import re

from bs4 import BeautifulSoup
from datetime import date

def getDate():
    today_date = date.today()
    today_date_formatted = str(today_date).split("-")
    today_date_out = ""
    today_date_out += today_date_formatted[1]
    today_date_out += today_date_formatted[2]
    today_date_out += today_date_formatted[0][2]
    today_date_out += today_date_formatted[0][3]
    return today_date_out

vgm_url = 'http://usccb.org/bible/readings/' + getDate() + '.cfm'

html_text = requests.get(vgm_url).text
soup = BeautifulSoup(html_text, 'html.parser')


match_1 = soup.find('div', class_='CS_Textblock_Text')

lectionary = match_1.h3.text

print lectionary

for match_2 in soup.find_all('div', class_='CS_Textblock_Text'):
    print match_2.p
    if match_2.p != None:
        print match_2.p.text
