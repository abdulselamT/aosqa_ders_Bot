import telebot
from telebot import types
from constders import API_KEY
from dataf import ders_with_link as d
from telegram import ParseMode
bot = telebot.TeleBot(API_KEY,parse_mode=None)
userdic={'aosqa':[]}
@bot.message_handler(commands=['exit'])
def generatestart(msg):
    l = list(d.keys())
    markup = types.ReplyKeyboardMarkup(row_width=1)
    for k in l:
        btn2 = types.KeyboardButton("/" + k)
        markup.add(btn2)
    bot.send_message(chat_id=msg.chat.id, text="please select", reply_markup=markup)
    userdic.pop(msg.from_user.username)
@bot.message_handler(content_types=['text'])
def generatekeyboards(msg):
    userne = msg.from_user.username
    if not userne in userdic:
        userdic[userne]=[]
    if userne in userdic:
        if not msg.text=='/start':
            if len(userdic[userne])==3:
                userdic[userne][-1]=msg.text.replace('/','')
            else:
                userdic[userne].append(msg.text.replace('/',''))
        n=userdic[userne]
        l=d.copy()
        for k in n:
            try:
                l=l[k]
            except:
                generatestart(msg)
                return 0

        try:
            l=list(l.keys())
            markup = types.ReplyKeyboardMarkup(row_width=1)
            for k in l:
                btn2 = types.KeyboardButton("/" + k)
                markup.add(btn2)
            btn3 = types.KeyboardButton("/main menu")
            markup.add(btn3)
            bot.send_message(chat_id=msg.chat.id, text="please select", reply_markup=markup)
        except:
            a=l[0]
            b=l[1]
            c=l[2]
            e=1
            if b>c:
                e=-1
                c+=1
            else:
                c-=1
            for j in range(b,c,e):
                tr=a+str(j)
                bot.send_message(chat_id=msg.chat.id, text=tr)

            bot.send_message(chat_id=msg.chat.id, text="ለ አስተያየት @aosqa")
            pass

def welcomeme(msg):
    bot.send_message(chat_id=msg.chat.id, text="welcome")
bot.polling()
