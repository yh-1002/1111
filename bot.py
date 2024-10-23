from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# 替换为你的 Bot Token
TOKEN = 'YOUR_BOT_TOKEN'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! Send me a message and I will echo it!')

def echo(update: Update, context: CallbackContext) -> None:
    # 打印收到的消息到控制台
    print(update.message.text)
    # 回显消息
    update.message.reply_text(update.message.text)

def main():
    # 创建 Updater 对象并传入 Bot Token
    updater = Updater(TOKEN)

    # 获取调度器来注册处理程序
    dispatcher = updater.dispatcher

    # 注册 /start 命令的处理程序
    dispatcher.add_handler(CommandHandler('start', start))

    # 注册文本消息的处理程序
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # 启动 Bot
    updater.start_polling()

    # 运行直到按下 Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
