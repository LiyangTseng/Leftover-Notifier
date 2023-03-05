'''
modified from https://steam.oxxostudio.tw/category/python/example/line-webhook.html
'''
import os
from flask import Flask, request

import json

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from text_handler import TextHandler

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def linebot():
    body = request.get_data(as_text=True)                    # 取得收到的訊息內容
    try:
        json_data = json.loads(body)                         # json 格式化訊息內容
        channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
        channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
        line_bot_api = LineBotApi(channel_access_token)              # 確認 token 是否正確
        handler = WebhookHandler(channel_secret)                     # 確認 secret 是否正確
        signature = request.headers['X-Line-Signature']      # 加入回傳的 headers
        handler.handle(body, signature)                      # 綁定訊息回傳的相關資訊
        tk = json_data['events'][0]['replyToken']            # 取得回傳訊息的 Token
        type = json_data['events'][0]['message']['type']     # 取得 LINE 收到的訊息類型
        if type=='text':
            msg = json_data['events'][0]['message']['text']  # 取得 LINE 收到的文字訊息
            print("msg", msg)                                       # 印出內容
            th = TextHandler()
            reply = th.process_requests(msg)
            print("reply", reply)
        else:
            reply = '現在只支援自動回覆文字訊息噢～'
        line_bot_api.reply_message(tk,TextSendMessage(reply))# 回傳訊息
    except:
        print("erorr occurs", body)                                          # 如果發生錯誤，印出收到的內容
    return 'OK'                                              # 驗證 Webhook 使用，不能省略

if __name__ == "__main__":
    app.run()
