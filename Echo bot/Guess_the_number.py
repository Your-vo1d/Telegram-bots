from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

#Введите сюда свой токен
BOT_TOKEN = ""

#Создание бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()