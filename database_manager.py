'''
Handle database I/O
'''

from google.oauth2.service_account import Credentials
import gspread
import pandas as pd
from credential_loader import load_credentials

class DatabaseManager:
    # TODO: add class hierarchy
    '''
    Parent class for Database Manager
    '''
    def __init__(self):
        pass

class GS_DatabaseManager:
    '''
    Database manager for google sheets
    '''
    def __init__(self, gs_credential_path, gs_url):
        scope = ['https://www.googleapis.com/auth/spreadsheets']
        credentials = load_credentials()
        creds = Credentials.from_service_account_info(credentials, scopes=scope)
        gs = gspread.authorize(creds)
        
        self.sheet_names = []
        
        self.sheet = gs.open_by_url(gs_url)
        sheet_num = len(self.sheet.worksheets())
        for i in range(sheet_num):
            self.sheet_names.append(self.sheet.get_worksheet(i).title)
        

    def get_sheet_data(self, sheet_name):
        worksheet = self.sheet.worksheet(sheet_name)
        return worksheet.get_all_records()
 
if __name__ == "__main__":
    gs_credential_path = "gs_credentials.json"
    gs_url = 'https://docs.google.com/spreadsheets/d/1HbBhLKTvTGv54dy-eM8YVKn7FiWU8XbmOHyPWcUM7Oc/edit#gid=0'
    dm = GS_DatabaseManager(gs_credential_path, gs_url)
    
    data = pd.DataFrame(dm.get_sheet_data("Leftovers"))
    print(data)