'''
Handle user requests/response
'''
import os
import pandas as pd
import dataframe_image as dfi
import pyimgur

from database_manager import GS_DatabaseManager

IMG_DIR = "img"

class TextHandler:
    def __init__(self, database_type="google_sheet", do_fuzzy_matching=False):
        self.keywords = ["剩菜", "食材"]
        self.do_fuzzy_matching = do_fuzzy_matching

        if database_type == "google_sheet":
            self.dm = GS_DatabaseManager()
        elif database_type == "SQL":
            raise Exception("Haven't implment yet")
        else:
            raise Exception("Database not available")


    def process_requests(self, text):
        '''
        Ｃonnect with Database Manager object to process use requests
        '''

        text = self.fuzzy_matching(text) if self.do_fuzzy_matching else text
        keyword = self.spot_keyword(text)

        if not keyword:
            return None
        else:
            info = self.dm.query(keyword)
            # if info:
            #     img_path = self.generate_reply_image(info, keyword)
            #     print(img_path)
            reply = self.format_reply(info)
            return reply

    def get_imgur_link(self, image_local_path):
        client_id = os.getenv('IMGUR_Client_ID', None)
        
        if not client_id:
            raise Exception("Could not load $IMGUR_Client_ID")
        
        im = pyimgur.Imgur(client_id)
        upload_image = im.upload_image(image_local_path, title="Uploaded with PyImgur")
        return upload_image.link


    def generate_reply_image(self, info, filename):
        '''
        transform and return the queried info as image
        '''
        os.makedirs(IMG_DIR, exist_ok=True)

        info = pd.DataFrame(info)
        df_styled = info.style.set_properties(**{'text-align': 'left'}).hide(axis="index")
        image_path = os.path.join(IMG_DIR, filename)
        dfi.export(df_styled, image_path, "matplotlib")
        return image_path
    
        
    def spot_keyword(self, text):
        if self.do_fuzzy_matching:
            # TODO: text processing 
            pass

        for keyword in self.keywords:
            if keyword in text:
                return keyword
        return None

    def format_reply(self, worksheet_outputs):
        reply = ""
        for row in worksheet_outputs:
            reply += "{}: {}\n".format(row['名稱'], row['數量'])
        return reply.strip()

    def fuzzy_matching(self, text):
        '''
        text processing to handle type
        '''
        pass

if __name__ == "__main__":
    th = TextHandler()
    keys = ["剩菜", "食材"]
    for key in keys:
        info = th.process_requests(key)
        print(key, "\n", info)
