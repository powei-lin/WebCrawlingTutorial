# Stage 3
Now we're able to get all the data from one page. The next thing is to iterate all active `id`.

## Active or not?
We need to find out weather it's an active project or not before start to iterate all `id`.

So on the upper right side of the snapshot part. There are two icons, one is `category` another is probably showing `active` or not.

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
There's no `A` in it. Also, some numbers in the webpage are missing. I guess the javascript rendering in python is not stable.