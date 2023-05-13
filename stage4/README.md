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

After checking some requests, I found this one seems suspicious. Its size is larger than other responses.

<kbd><img src=../imgs/s4_2.png width="640" /></kbd>

It contains lots of information. Since there is project cost showing on the page. I decided to search in this response whether it has the number of `project cost`. And I found it!

<kbd><img src=../imgs/s4_3.png width="640" /></kbd>

## Try to save the response to json file
We've already hit the jackpot. Let's try to save the response to json file and see what else do we get.

By clicking the header tab, you can see what url did we send. Let's copy that url and use python to send that.
<kbd><img src=../imgs/s4_4.png width="640" /></kbd>

Take a look at [`stage4/main.py`](./main.py).