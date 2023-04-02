from model import *
from telebot import types, TeleBot

token = input()
bot = TeleBot(token)

menu = types.RepyKeyboardMarkup(resize_keyboard=True)
button1 = types.KeyboardButton("Заработать")
button2 = types.KeyboardButton("Баланс")
button3 = types.KeyboardButton("FAQ")
menu.row(button1)
menu.row(button2, button3)

earn = ReplyKeyboardMarkup(resize=True)
btn1=KeyboardButton('10 человек - 10%')
btn2=KeyboardButton('5 человек - 20%')
btn3=KeyboardButton('4 человека - 25%')
btn4=KeyboardButton('Пополам убыток и доход')
earn.row(btn1, btn2)
earn.row(btn3, btn4)

@bot.message_handler(commands=['Start', 'start'])
def start(message):
    if not(Users.user_exists(message.chat.id)):
        Users.create_user(message.chat.id)
    bot.send_message(message.chat.id, 'Приветсвую Вас в боте для онлайн заработка', reply_markup=menu)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.type == 'private':
        if message.text == 'Заработать':
            bot.send_message(message.chat.id, 'Выберете один вариант:', reply_markup=earn)
            bot.register_next_step_handler(message, earn)
        elif message.text == 'Баланс':
            bot.send_message(message.chat.id, 'Вы заработали с нами: {Users.get_balance(message.chat.id)}\nВы провели с нами {Users.get_n(message.chat.id)} сделок\nУровень вашей доверенности: {Users.get_n(message.chat.id)//10+1}')
        elif message.text == 'FAQ':
            bot.send_message(message.chat.id, '.')
        elif message.text == '10 человек - 10%':
            bot.send_message(message.chat.id, 'Переведите 85 рублей на карту 2200 19.. .... .... в комментарии к платежу укажите свой юзернейм/имя в тг, после чего напишите админу @ilnurKhalikov')
        elif message.text == '5 человек - 20%':
            if Users.get_n(message.chat.id)//10+1 >= 2:
                bot.send_message(message.chat.id, 'Переведите 138 рублей на карту 2200 19.. .... .... в комментарии к платежу укажите свой юзернейм/имя в тг, после чего напишите админу @ilnurKhalikov')
            else:
                bot.send_message(message.chat.id, 'У вас недостаточный уровень доверенности для этого варианта заработка'
        elif message.text == '4 человек - 25%':
            if Users.get_n(message.chat.id)//10+1 >= 3:
                bot.send_message(message.chat.id, 'Переведите 158 рублей на карту 2200 19.. .... .... в комментарии к платежу укажите свой юзернейм/имя в тг, после чего напишите админу @ilnurKhalikov')
           else:
                bot.send_message(message.chat.id, 'У вас недостаточный уровень доверенности для этого варианта заработка'
        elif message.text == 'Пополам убыток и доход':
            if Users.get_n(message.chat.id)//10+1 >= 4:
            bot.send_message(message.chat.id, 'Переведите 275 рублей на карту 2200 19.. .... .... в комментарии к платежу укажите свой юзернейм/имя в тг, после чего напишите админу @ilnurKhalikov , если хотите заработать ещё больше денег, то отправьте ещё 275 рублей на карту выше, и напишите админу "Повышенный доход"')
           else:
                bot.send_message(message.chat.id, 'У вас недостаточный уровень доверенности для этого варианта заработка'

while True:
    try:
        bot.polling()
    except Exception as e:
        print(e)
