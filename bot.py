from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackContext

# 替换为你的 Bot Token
TOKEN = '7913141683:AAHuJXDJ_uyJQKAGnsP0neeVgei1SOMLoNI'

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('你好 請輸入股票代碼')

async def echo(update: Update, context: CallbackContext) -> None:
    # 打印收到的消息到控制台
    print(update.message.text)
    # 回显消息
    await update.message.reply_text(update.message.text)

def main():
    # 创建 Application 对象并传入 Bot Token
    app = ApplicationBuilder().token(TOKEN).build()

    # 注册 /start 命令的处理程序
    app.add_handler(CommandHandler('start', start))

    # 注册文本消息的处理程序
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # 启动 Bot
    app.run_polling()

if __name__ == '__main__':
    main()
