import telebot
import time
import threading

TOKEN = '824385321:AAHXimq-mrBo1baiY4StM-OrHzhaDZdpz4w'
Ygy = 'Угу'
partAsk = 'подтверди'
Answer = 'Подтверждаю'
lastTime = time.time()
TimeSleep = 15             #сек

bot = telebot.TeleBot(TOKEN)

chatIDLast = 0


@bot.message_handler(func=lambda message: True)
def send(message):
    global chatIDLast
    chatID = message.chat.id
    if chatID != chatIDLast:
        MesThread = threading.Thread(target=My_thread, args=(chatID,))
        MesThread.setDaemon(True)
        MesThread.start()
    if partAsk in message.text.lower():
        bot.send_message(chatID, Answer)


def My_thread(IDChat):
    while True:
        time.sleep(TimeSleep)
        print(Ygy)
        bot.send_message(IDChat, Ygy)


bot.polling()




