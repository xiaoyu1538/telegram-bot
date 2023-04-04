import telegram
from telegram.ext import Updater, MessageHandler, Filters

# 用你的 Bot API token 替换下面的字符串
TOKEN = 'your-bot-token-here'

# 创建一个 Telegram Bot 实例
bot = telegram.Bot(token=TOKEN)

def reply_message(update, context):
    """回复消息的处理函数"""
    message = update.message.text
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text='Hello, I received your message: ' + message)

def main():
    """主函数"""
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    # 添加处理函数，当收到任何消息时都调用 reply_message 函数
    dispatcher.add_handler(MessageHandler(Filters.all, reply_message))
    # 开始运行机器人
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
