import os
import logging
import gspread
import configparser

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode

from oauth2client.service_account import ServiceAccountCredentials

JSON_KEY_FILE = r'D:\Games\Python\bots TG\IncomeAndExpenses\TGBOT\settings\incomeandexpenses-413414-053a6101473b.json'

SETTINGS_PATH = r'D:\Games\Python\bots TG\IncomeAndExpenses\TGBOT\settings\settings.ini'
# database_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'IncomeAndExpenses', 'TGBOT', 'settings', 'database.db')

config = configparser.ConfigParser()
config.read(SETTINGS_PATH)

# Configure logging
logging.basicConfig(level=logging.INFO)

PATH_DATABASE = r'D:\Games\Python\bots TG\IncomeAndExpenses\TGBOT\settings\database.db'
API_TOKEN = config.get('settings', 'token')

bot = Bot(API_TOKEN, parse_mode = ParseMode.HTML)
dp = Dispatcher()

# Function to authenticate and get the Google Sheets client
def get_google_sheets_client():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(JSON_KEY_FILE, scope)
    return gspread.authorize(creds)

