# Stage 1
After casual browsing, we can start writing some code to test.

The following part is **pseudocode** of the initial idea of how we're going to crawl the website.
```py
url_base = http://www.p3spectrum.ca/project/info/?id=
total_active = 291  # from the site it says there's 291 active
count_active = 0
idx = 1
while(count_active < total_active):
    url = url_base+str(idx)
    result = parse_url(url)
    if check_active(result):
        count_active += 1
        save(result)
    idx += 1
```
## HTTP request
The first thing we want to find out is: 
Can we get everything after the first HTTP request? Or it's more complicated?

We need some extra package to start sending HTTP request in `python`.
```
pip install requests
```

Take a look at [`stage1/main.py`](./main.py), and try to execute it. It tries to send an HTTP GET request to `http://www.p3spectrum.ca/project/info/?id=1`. And the result is being written to `test.html`.

## From the HTTP GET result
After open `test.html`, you'll see there are lots of placeholders. And there's no number in it.
<kbd><img src=../imgs/s1_0.png alt="id in url" width="640" /></kbd>

