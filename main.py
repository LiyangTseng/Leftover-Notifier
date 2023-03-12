'''
Flask entry for LineBot
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
    body = request.get_data(as_text=True)                    
    try:
        json_data = json.loads(body)                         
        channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
        channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
        line_bot_api = LineBotApi(channel_access_token)
        handler = WebhookHandler(channel_secret)
        signature = request.headers['X-Line-Signature']
        handler.handle(body, signature)                
        tk = json_data['events'][0]['replyToken']      
        type = json_data['events'][0]['message']['type']
        if type=='text':
            msg = json_data['events'][0]['message']['text']
            print("msg", msg)

            th = TextHandler()
            reply = th.process_requests(msg)
        else:
            reply = '現在只支援自動回覆文字訊息噢～'

        print("reply", reply)        
        if not reply:
            line_bot_api.reply_message(tk,TextSendMessage(reply))
    except Exception as e:
        print("erorr occurs. request body: {}\n, exception: {}", body, e)
    return 'OK'

if __name__ == "__main__":
    app.run()
