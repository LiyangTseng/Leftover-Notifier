'''
Handle user requests/response
'''
from database_manager import GS_DatabaseManager

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
            reply = self.format_reply(info)
            return reply
        
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
            reply += "{}: {}\n".format(row['name'], row['quantity'])
        return reply.strip()

    def fuzzy_matching(self, text):
        '''
        text processing to handle type
        '''
        pass

if __name__ == "__main__":
    th = TextHandler()
    data = th.process_requests("食材")
    print(data)