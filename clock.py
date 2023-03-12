from apscheduler.schedulers.blocking import BlockingScheduler
import requests

url = 'https://samtsai-line-bot-python-flask.onrender.com'  # Replace with your service's URL

def keep_alive():
    # Send a GET request to your service's URL
    requests.get(url)
    print(f'Sent request to {url}')

scheduler = BlockingScheduler()
scheduler.add_job(keep_alive, 'interval', minutes=10)  # Send a request every 5 minutes
scheduler.start()
