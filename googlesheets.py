# Eventually this will be replaced by a database manager.
# This is for prototyping!

import settings
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import json

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

SPREADSHEET_ID = settings.SPREADSHEET_ID

def init():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    
    return creds

def get_data():
    '''
    id = sheets.values().get(
        spreadsheetId=SPREADSHEET_ID,
        range=f'char_sheets!A{row}',
    ).execute().get('values')[0][0]
    '''

    pass

def update_data(db, data):
    creds = init()
    # RUN THE SERVICE (finally!)
    try:
        service = build('sheets', 'v4', credentials=creds)
        sheets = service.spreadsheets()

        json_data = json.loads(open('database.json').read())
        row = json_data[db]['row']
        cols = json_data[db]['cols']

        for col in range(ord('A'), ord('A') + len(cols)):

            # UPDATE DATA IN SPREADSHEET
            sheets.values().update(
                spreadsheetId=SPREADSHEET_ID,
                range=f'{db}!{chr(col)}{row}',
                valueInputOption='USER_ENTERED',
                body={ 'values': [[f'a']] },
            ).execute()

    except HttpError as err:
        print(err)

update_data('char_sheets')
