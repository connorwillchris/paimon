from dotenv import load_dotenv
import os

# load the token
load_dotenv()
TOKEN = os.getenv('TOKEN')
SPREADSHEET_ID = os.getenv('SPREADSHEET_ID')
