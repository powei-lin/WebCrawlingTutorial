# import module
import requests

# first, we want to test on one url
url = 'http://www.p3spectrum.ca/project/info/?id=1'

# send http get
result = requests.get(url)

# write to a file to see what's inside
with open('test.html', 'w') as ofile:
    ofile.write(result.text)