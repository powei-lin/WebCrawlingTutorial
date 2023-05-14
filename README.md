# Web Crawling Tutorial
This repository records the thought process involved in web crawling.

The target website is http://www.p3spectrum.ca/project/info/?id=1

<a href="http://www.p3spectrum.ca/project/info/?id=1" target="_blank"><img src=imgs/website_screenshot.png
alt="website screenshot" width="640" /></a>

## Required basic knowledge
* Python
* Git
* HTTP

## Thought process
* [Stage 0 Try to find common patterns.](/stage0/README.md) 
* [Stage 1 Start coding and send HTTP request.](/stage1/README.md) 
* [Stage 2 Try Javascript rendering.](/stage2/README.md) 
* [Stage 3 Check active and found new problem](/stage3/README.md)
* [Stage 4 Can we do better?](/stage4/README.md) 
* [Stage 5 Loop to get all active projects](/stage5/README.md) 

### Additional part
This part needs login credentials.
* [Additional 0 Get missing data with login](/additional0/README.md) 

## How to use
```sh
# Clone the repo and change directory
git clone https://github.com/powei-lin/WebCrawlingTutorial.git && cd WebCrawlingTutorial
# You should be able to run every stage's python script
python3 stage5/main.py
```