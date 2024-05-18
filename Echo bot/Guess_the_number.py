import random

from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

# Введите сюда свой токен
BOT_TOKEN = ""

# Создание бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

#Количество попыток, доступных пользователю
ATTEMPTS = 5
user = {"in_game": False,
        "secret_number": None,
        "attempt": None,
        "total_games": 0,
        "wins": 0}

# Функция возвращения рандомного целого числа от 1 до 100
def get_random_numer() -> int:
    return random.randint(1, 100)

# Хендлер, вызываемый при команде /help
@dp.message(CommandStart())
async def procces_start_command(message: Message):
    await message.answer(
        "Привет!"
        "Давайте сыграем в игру 'Угадай число'!"
        "Чтобы узнать правила игры и посмотреть список доступных команд, отправьте команду /help."
    )
# Хендлер, вызываемый при команде /help
async def procces_help_command(message: Message):
    await message.answer(
        f'Правила игры:\n\nЯ загадываю число от 1 до 100, '
        f'а вам нужно его угадать\nУ вас есть {ATTEMPTS} '
        f'попыток\n\nДоступные команды:\n/help - правила '
        f'игры и список команд\n/cancel - выйти из игры\n'
        f'/stat - посмотреть статистику\n\nДавай сыграем?'
    )