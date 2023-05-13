# Stage 4
By rendering javascript in python, we're able to get all the information we want. But there's two disadvantages.

1. We render the webpage and then use `bs4` to parse html and find what we want. Which is a bit slow. 

2. The `requests_html` seems not very robust. Sometimes the rendered webpage is missing some information.

## Find the API call
Before rendering javascript, there's must be some API call from the webpage to the database. So let's find out.

Open the project page in a browser and press `F12` to open the developer tool. Every browser has developer tool. I'm using Brave, but I guess all chromium based browser has similar UI. 

Press the `>>` bottom.
<kbd><img src=../imgs/s4_0.png width="640" /></kbd>

Open the `Network` tab.
<kbd><img src=../imgs/s4_1.png width="480" /></kbd>

Refresh the page, you'll see what's all the http requests during loading the page.
<kbd><img src=../imgs/refresh.avif width="640" /></kbd>

<!-- So on the upper right side of the snapshot part. There are two icons, one is `category` another is probably showing `active` or not.

<kbd><img src=../imgs/s3_0.png width="640" /></kbd>

We can use right click on the icon and click inspect to see where is this icon come from.

<kbd><img src=../imgs/s3_1.png width="360" /></kbd>

It shows that it's a `span` with `class="marker marker-prime ng-binding"`.

<kbd><img src=../imgs/s3_2.png width="640" /></kbd>
```py
# import module
from requests_html import HTMLSession
from bs4 import BeautifulSoup

# first, we want to test on one url
url = 'http://www.p3spectrum.ca/project/info/?id=1'

# send http get
session = HTMLSession()
r = session.get(url)

# render javascript
r.html.render()

# process html and try to find span with class
soup = BeautifulSoup(r.html.html, "lxml")
print(soup.find('span', {'class': "marker marker-prime ng-binding"}))
```
## Something's weird
I'm able to get see the following text in the terminal after executing the script.
```
<span class="marker marker-prime ng-binding">A</span>
```
But after executing several times, sometimes I got 
```
<span class="marker marker-prime ng-binding"></span>
``` 
There's no `A` in it. Also, some numbers in the webpage are missing. I guess the javascript rendering in python is not stable. -->