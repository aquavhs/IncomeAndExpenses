
from datetime import datetime
from TGBOT.settings.database import add_user_data, is_user_in_table
from TGBOT.settings.config import get_google_sheets_client

from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext


router = Router()

@router.message(CommandStart())
async def bot_start(message: Message):
    user_time = datetime.now().strftime('%d-%m-%Y %H:%M')
    user_id = message.from_user.id
    user_name = message.from_user.username
    user_firstName = message.from_user.first_name


    if not is_user_in_table(user_id):
        add_user_data(user_id,user_firstName,user_name,user_time)
        await message.answer('You have been registered!')
    else:
        await message.answer('You are already registered!')

# Работа с гугл таблицей
@router.message(Command('data'))
async def get_data(message: Message):
    # Get the Google Sheets client
    sheets_client = get_google_sheets_client()

    # Replace with your Google Spreadsheet name
    spreadsheet_name = 'MyCosts'

    try:
        # Open the Google Spreadsheet by name
        spreadsheet = sheets_client.open(spreadsheet_name)

        # Get the first sheet in the spreadsheet
        sheet = spreadsheet.get_worksheet(0)

        # Get data from a specific cell (example: A1)
        cell_data = sheet.acell('E6').value

        # Respond to the user with the retrieved data
        await message.reply(f"Data from A1: {cell_data}")

    except Exception as e:
        print(f"Error: {e}")
        await message.reply("An error occurred while retrieving data.")