from dotenv import load_dotenv
import os

# initialize the DOTENV module
load_dotenv()

# global passwords and tokens
TOKEN = os.getenv('TOKEN')
DB_CONNECTION = os.getenv('DB_CONNECTION')
