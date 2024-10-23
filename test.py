from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackContext

from python import requests as res
from python import json
from python import pandas as pd
from python import matplotlib.pyplot as plt

# 替换为你的 Bot Token
TOKEN = '7913141683:AAHuJXDJ_uyJQKAGnsP0neeVgei1SOMLoNI'

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('請輸入股價代碼')

async def echo(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text.lower()

  
    url_oneday='https://openapi.twse.com.tw/v1/exchangeReport/STOCK_DAY_ALL'
    re=res.get(url_oneday)
    data=json.loads(re.text)
    df=pd.DataFrame(data)
    b = df[df['Code'] == user_message]['HighestPrice']
    c = df[df['Code'] == user_message]['LowestPrice']
    d = df[df['Code'] == user_message]['Change']
    e = df[df['Code'] == user_message]['Transaction']
    x = df[df['Code'] == user_message]['Name']
    if b.empty:
      response = f"股票代號 {a} 輸入不存在或沒有資料"
    else:
      response = f"{a} {x.values[0]} 最高價為: {b.values[0]} 最低價為: {c.values[0]} 漲跌差為: {d.values[0]} 成交量為: {e.values[0]}"


  
    
    # 打印收到的消息和回复到控制台
    print(f"Received message: {update.message.text}")
    print(f"Response: {response}")
    # 回显消息
    await update.message.reply_text(response)

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
