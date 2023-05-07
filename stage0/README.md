# Stage 0
First, we want to find some patterns on the website.

The first thing I noticed was that there's a `id` in the URL.

<img src=../imgs/s0_0.png alt="id in url" width="640" /></a>

On the front page. It says there are **291** active projects.
<img src=../imgs/s0_1.png alt="id in url" width="640" /></a>

So there are few things we need to find out.

1. Does the `id` start from 0 or 1?
2. Are the first 291 projects active projects? Or the `id` is randomly assigned.
3. If first 291 `id` are not all active projects, is there a way to distinguish active and non-active ones?

## 1. Does the `id` start from 0 or 1?
Manually change the `id` in URL to 0.
And it looks like it's just an empty page.
**So the `id` starts from 1**.
<img src=../imgs/s0_2.png alt="id in url" width="640" />

## 2. Are the first 291 projects active projects? Or the `id` is kind of randomly assigned.
After open a few projects from [project page](http://www.p3spectrum.ca/project/).
I found that an active project has `id=418`. So clearly the first 291 projects are not all active.
<img src=../imgs/s0_3.png alt="id in url" width="640" />

## 3. If first 291 `id` are not all active projects, is there a way to distinguish active and non-active ones?
It seems like that there's a `A` indicate whether this project is active or not.