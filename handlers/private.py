from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""I'am **{bn}**
🇬🇧 Usage : /e Music Name
🇬🇧 Sorry I Only Work in Groups :(
▪️
🇹🇷 Kullanım : /e Müzik Adı
🇹🇷 Üzgünüm Sadece Gruplarda Çalışırım :(
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📣 Channel", url="https://t.me/NetdBots"
                    ),    
                    InlineKeyboardButton(
                        "🇬🇧 Add to Group", url="https://t.me/NetdMusicbot?startgroup=true"
                    ),    
                    InlineKeyboardButton(
                        "🇹🇷 Gruba Ekle", url="https://t.me/NetdMusicbot?startgroup=true"
                    )
                ]
            ]
        )
    )
