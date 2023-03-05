'''
Handle user requests/response
'''
import pandas as pd
from database_manager import GS_DatabaseManager

class TextHandler:
    def __init__(self, do_fuzzy_matching=False):
        self.keyword_to_tab = {"剩菜": "Leftovers", "食材": "Ingredients"}
        self.do_fuzzy_matching = do_fuzzy_matching

        # TODO: use hierarchy to use database manager
        gs_credential_path = "gs_credentials.json"
        gs_url = 'https://docs.google.com/spreadsheets/d/1HbBhLKTvTGv54dy-eM8YVKn7FiWU8XbmOHyPWcUM7Oc/edit#gid=0'
        self.dm = GS_DatabaseManager(gs_credential_path, gs_url)


    def process_requests(self, text):
        '''
        Ｃonnect with Database Manager object to process use requests
        '''

        keyword = self.fuzzy_matching(text) if self.do_fuzzy_matching else text

        if keyword not in self.keyword_to_tab.keys():
            raise Exception("not a valid keyword, the valid keywords are {}".format(list(self.keyword_to_tab.keys())))
        
        sheet_name = self.keyword_to_tab[keyword]

        # TODO: use hierarchy to use database manager
        info = self.dm.get_sheet_data(sheet_name)
        return info

    def fuzzy_matching(self, text):
        '''
        text processing to handle type
        '''
        pass

if __name__ == "__main__":
    th = TextHandler()
    data = th.process_requests("食材")
    # data = pd.DㄥataFrame(data)
    print(data)