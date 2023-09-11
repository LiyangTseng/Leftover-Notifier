#基本功能測試
import requests
from database_manager import GS_DatabaseManager
from text_handler import TextHandler

def lineNotifyMessage(token, msg):

    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type" : "application/x-www-form-urlencoded"
    }

    payload = {'message': msg }
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code

def format_reply(worksheet_outputs):
    reply = ""
    for row in worksheet_outputs:
        reply += "{}: {}\n".format(row['名稱'], row['數量'])
    return reply.strip()

if __name__ == "__main__":
    token = 'JQeuJEkvorbq7THEtE39wEU0uVTn9OXwOrycBoHGJ57'
    dm = GS_DatabaseManager()
    keywords = ["剩菜", "食材"]
    replies = []
    for k in keywords:
        info = dm.query(k)
        message = format_reply(info)
        # replies.append(reply)
        # print(message)
    # print(replies)

        lineNotifyMessage(token, message)