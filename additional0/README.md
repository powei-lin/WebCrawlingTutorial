# Additional 0
In the previous stage, we send a HTTP request without containing any credentials.
So I assume that the data we get should be missing something.
(Sometimes we could get all data without giving any credentials, thanks to the bad web developer.)

Let's check whether we're missing something or not. After login, there's milestone dates on the page.

<kbd><img src=../imgs/a0_0.png width="640" /></kbd>

Clearly we don't have that part in our json file.

And the received response with login is larger than without.

Without login:

<kbd><img src=../imgs/a0_1.png width="640" /></kbd>


With login:

<kbd><img src=../imgs/a0_2.png width="640" /></kbd>

And after checking what's the difference between with and without login, I found that there's additional column called `SessionGuid` in the http request header.

<kbd><img src=../imgs/a0_3.png width="640" /></kbd>

See [`additional/main.py`](./main.py). We add cookie with http request. And we're able to get the extra data this time.

<kbd><img src=../imgs/a0_4.png width="640" /></kbd>