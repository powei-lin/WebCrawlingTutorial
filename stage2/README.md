# Stage 2
We tried very basic HTTP request, and we got a website template without any data.

Apparently there's some Javascript being executed after http request. So the website looks different on the browser.

## Render Javascript in python
After some googling, I found that there's a package called `requests-html` which can render javascript. So let's install it.
```
pip install requests-html
```

## See what we get after rendering javascript
Take a look at [`stage2/main.py`](./main.py). It's basically the same as stage1 except we use another module and render javascript after the HTTP request.

And this time we get a lot of information. Seems like we're almost done.
<kbd><img src=../imgs/s2_0.png width="640" /></kbd>