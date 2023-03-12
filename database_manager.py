'''
Handle database I/O
'''

from google.oauth2.service_account import Credentials
import gspread

from utils import load_credentials

class DatabaseManager:
    '''
    Parent class for Database Manager
    '''
    def __init__(self):
        pass

    def query(keyword):
        pass

class GS_DatabaseManager(DatabaseManager):
    '''
    Database manager for google sheets
    '''
    def __init__(self):
        super().__init__()

        scope = ['https://www.googleapis.com/auth/spreadsheets']
        credentials = load_credentials()
        creds = Credentials.from_service_account_info(credentials, scopes=scope)
        gs = gspread.authorize(creds)
        gs_url = 'https://docs.google.com/spreadsheets/d/1HbBhLKTvTGv54dy-eM8YVKn7FiWU8XbmOHyPWcUM7Oc/edit#gid=0'
        self.sheet = gs.open_by_url(gs_url)
    
        self.keyword_to_sheet = {"剩菜": "Leftovers", "食材": "Ingredients"}
        self.sheet_names = []
        sheet_num = len(self.sheet.worksheets())
        for i in range(sheet_num):
            self.sheet_names.append(self.sheet.get_worksheet(i).title)     

    def query(self, keyword):
        sheet_name = self.keyword_to_sheet[keyword]
        worksheet = self.sheet.worksheet(sheet_name)
        return worksheet.get_all_records()
 
if __name__ == "__main__":
    dm = GS_DatabaseManager()
    # leftovers = dm.query("剩菜")
    ingredients = dm.query("食材")
    # print(leftovers)
    # print(ingredients)
