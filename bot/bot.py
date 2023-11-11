"""
This example shows how to use webhook with SSL certificate.
"""
import logging
import sys
from os import getenv
from aiohttp import web
from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import FSInputFile, Message
from aiogram.utils.markdown import hbold
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp.web_request import Request
from aiomysql import Connection, Cursor, DictCursor, connect
from aiogram.types import User

MYSQL = {
    "host": "192.168.1.40",
    "user": "root",
    "password": "root",
    "db": "support_bot_database",
    "port": "3306",
}

async def create_con(user: User):
    con: Connection = await connect(**MYSQL)
    cur: Cursor = await con.cursor()
    return con, cur

async def new(user: User):
    con, cur = await create_con()
    await cur.execute(
        "insert ignore into tg_user (tg_chat_id, full_name, user_name, locale) "
        "VALUES (%s, %s, %s, %s)",
        (user.id, user.full_name, user.username, None),
    )

    await con.commit()
    await con.ensure_closed()

async def get_all():
    con, cur = await create_con()
    await cur.execute(
        "select * from tg_user",
    )
    users_data = await cur.fetchall()
    await con.ensure_closed()
    return users_data

TOKEN = getenv("BOT_TOKEN")

WEB_SERVER_HOST = "192.168.1.10"
WEB_SERVER_PORT = 2005

WEBHOOK_SECRET = "my-secret"
BASE_WEBHOOK_URL = f"https://{getenv('SERVER_IP_ADDRESS')}/tg-bot"
print("BASE_WEBHOOK_URL", BASE_WEBHOOK_URL)

WEBHOOK_SSL_CERT = "/nginx-certs/nginx-selfsigned.crt"
WEBHOOK_SSL_PRIV = "/nginx-certs/nginx-selfsigned.key"
router = Router()
web_routes = web.RouteTableDef()

@web_routes.get(f"/get_users")
async def get_200(request: Request):
    return web.json_response(
        {"error": "bot get"}, status=200)

@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await new(message.from_user)
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
    app.add_routes(web_routes)
    web.run_app(app, host=WEB_SERVER_HOST, port=WEB_SERVER_PORT)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    main()
