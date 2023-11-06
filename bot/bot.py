"""
This example shows how to use webhook with SSL certificate.
"""
import logging
import ssl
import sys
from os import getenv

from aiohttp import web

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import FSInputFile, Message
from aiogram.utils.markdown import hbold
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application


TOKEN = "6764040090:AAFKPxX9iqeQlT9gWy-jFxRSb5IIB_2gWYk"

WEB_SERVER_HOST = "127.0.0.1"
WEB_SERVER_PORT = 2005

WEBHOOK_SECRET = "my-secret"
BASE_WEBHOOK_URL = "https://159.89.104.29"

WEBHOOK_SSL_CERT = "/nginx-certs/nginx-selfsigned.crt"
WEBHOOK_SSL_PRIV = "/nginx-certs/nginx-selfsigned.key"
router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")


@router.message()
async def echo_handler(message: types.Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")


async def on_startup(bot: Bot) -> None:
    result = await bot.set_webhook(
        f"{BASE_WEBHOOK_URL}",
        certificate=FSInputFile(WEBHOOK_SSL_CERT),
        secret_token=WEBHOOK_SECRET,
    )
    print(f"{BASE_WEBHOOK_URL}")
    print(result)

def main() -> None:
    dp = Dispatcher()
    dp.include_router(router)
    dp.startup.register(on_startup)
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    app = web.Application()
    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
        secret_token=WEBHOOK_SECRET,
    )
    webhook_requests_handler.register(app, path="")

    setup_application(app, dp, bot=bot)
    web.run_app(app, host=WEB_SERVER_HOST, port=WEB_SERVER_PORT)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    main()
