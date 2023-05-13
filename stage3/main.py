from requests_html import HTMLSession
from bs4 import BeautifulSoup

# first, we want to test on one url
url = 'http://www.p3spectrum.ca/project/info/?id=1'

# send http get
session = HTMLSession()
r = session.get(url)
r.html.render()
soup = BeautifulSoup(r.html.html, "lxml")
print(soup.find('span', {'class': "marker marker-prime ng-binding"}))