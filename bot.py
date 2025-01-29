import logging
import openai
import asyncio
from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message
from aiogram.filters import CommandStart
import os  # Добавили для переменных окружения

TOKEN = os.getenv("7740352062:AAHqMEgaJbuhtqApn7WJ5iZDU-Uv8_7PF8I")  # Получаем токен из переменных окружения
OPENAI_API_KEY = os.getenv("ce74f2f3470376355e7e2c46a008a24")  # API-ключ OpenAI

bot = Bot(token=TOKEN)
dp = Dispatcher()
router = Router()

dp.include_router(router)

openai.api_key = ce74f2f3470376355e7e2c46a008a24  # Устанавливаем API-ключ OpenAI


@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Привет! Отправь мне сообщение, и я отвечу.")


@router.message()
async def chat_with_gpt(message: Message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message.text}]
        )

        reply = response["choices"][0]["message"]["content"]
        await message.answer(reply)

    except Exception as e:
        await message.answer(f"Ошибка обработки запроса: {str(e)}")
        logging.error(f"Ошибка OpenAI: {str(e)}")


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
