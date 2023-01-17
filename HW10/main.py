import telebot
import const
import control


bot = telebot.TeleBot(const.telergam_token)
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, const.start_mess)
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, control.parse(message.text))
bot.polling(none_stop=True, interval=0)