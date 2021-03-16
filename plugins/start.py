from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Kanal", url="https://t.me/virtual_coders")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/virtual_coder")]
    ])
    welcomed = f"salom qalesanHey <b>{message.from_user.first_name}</b>\n/help for More info"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
