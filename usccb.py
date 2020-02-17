import requests

from bs4 import BeautifulSoup

vgm_url = 'http://usccb.org/bible/readings/021720.cfm'

html_text = requests.get(vgm_url).text
soup = BeautifulSoup(html_text, 'html.parser')

print(soup.title)
