from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, CallbackContext

TOKEN = "8063147867:AAFXpDLM70wcX4_4j9VnP8oQlRmUt5RqDIc"

def start(update: Update, context: CallbackContext):
    update.message.reply_text("👋 I'm alive and ready!")

def message_handler(update: Update, context: CallbackContext):
    text = update.message.text.lower()
    if "hey stepsis" in text:
        keyboard = [
            [InlineKeyboardButton("Root App and Modules", callback_data='root_app_modules')],
            [InlineKeyboardButton("Gaming-Script", callback_data='gaming_script')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text("How can I make you happy today, babe?", reply_markup=reply_markup)

def button(update: Update, context: CallbackContext):
    query = update.callback_query
    data = query.data
    chat_id = query.message.chat_id

    if data == 'root_app_modules':
        files = [
            "KernelSU-Next.apk",
            "KsuWebUI.apk",
            "MT-Manager.apk",
            "Zygisk-Next.zip",
            "SUSFS.zip",
            "Shamiko.zip",
            "Tricky-Store.zip",
            "Tricky-Addon.zip",
            "TSupport.zip",
            "Yuri-Keybox.zip",
            "COPG-Spoof.zip",
        ]
        for f in files:
            try:
                context.bot.send_document(chat_id=chat_id, document=open(f, "rb"))
            except FileNotFoundError:
                context.bot.send_message(chat_id=chat_id, text=f"❌ File `{f}` not found.")

    elif data == 'gaming_script':
        files = [
            "Latest-Bing.zip",
            "Kernel-Driver.zip",
        ]
        for f in files:
            try:
                context.bot.send_document(chat_id=chat_id, document=open(f, "rb"))
            except FileNotFoundError:
                context.bot.send_message(chat_id=chat_id, text=f"❌ File `{f}` not found.")

    query.answer()

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, message_handler))

    updater.start_polling()
    print("✅ Bot is running...")
    updater.idle()

if __name__ == "__main__":
    main()
