
# Leftovers Notifier
## Overview
- The Flask-based LineBot is deployed on Render.
- Currently store all the data on Google Sheet.
## Set up the project
1. Install relevent packages
```
pip install -r requirements.txt
```
2. Register Render
- Follow [this page](https://ithelp.ithome.com.tw/articles/10283836) for Render registration and usage.
3. Apply for Google Sheet API
- Follow the [steps](https://www.learncodewithmike.com/2021/06/pandas-and-google-sheets.html) to set up Google Sheet API.
- To use Google Sheet credentials while not leak the API secrets on public Github repo, store all the environment variables on Render manually.
## Refenreces
The LineBot source code is modified from [here](https://steam.oxxostudio.tw/category/python/example/line-webhook.html). While the original project deploy the chatbot on ngrok, I turn to Render for its stability.