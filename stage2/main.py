# import module
from requests_html import HTMLSession

# first, we want to test on one url
url = 'http://www.p3spectrum.ca/project/info/?id=1'

# send http get
session = HTMLSession()
r = session.get(url)
r.html.render()

# write to a file to see what's inside
with open('test.html', 'w') as ofile:
    ofile.write(r.html.html)