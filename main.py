# -*- coding: utf-8 -*-

import sqlite3
from models import *
from telebot import TeleBot, types

adm = [1633567239, 1825897067]
bot = TeleBot('5280986352:AAHCt6MAKEEaPUUPHcXKW_O65mel9UtMubk')

menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
button1 = types.KeyboardButton('Купить Dedicate Server')
button2 = types.KeyboardButton('Партнерская программа')
button3 = types.KeyboardButton('F.A.Q')
button4 = types.KeyboardButton('Отзывы')
menu.row(button1)
menu.row(button2, button3)
menu.row(button4)

main1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
button1 = types.KeyboardButton('Дедики с админ правами')
button2 = types.KeyboardButton('Дедики без админ прав')
button3 = types.KeyboardButton('Оплата и гарантии')
button4 = types.KeyboardButton('Go Back')
main1.row(button1)
main1.row(button2)
main1.row(button3)
main1.row(button4)

cancel = types.ReplyKeyboardMarkup(resize_keyboard=True)
button1 = types.KeyboardButton('Отмена')
cancel.row(button1)

admins = types.ReplyKeyboardMarkup(resize_keyboard=True)
button1 = types.KeyboardButton('Ответить на сообщение пользователю')
button2 = types.KeyboardButton('Обнулить кол-во дедиков')
button3 = types.KeyboardButton('Удалить дедик с админ правами')
button4 = types.KeyboardButton('Удалить дедик без админ прав')
button5 = types.KeyboardButton('Добавить дедик с админ правами')
button6 = types.KeyboardButton('Добавить дедик без админ прав')
button7 = types.KeyboardButton('Рассылка')
button8 = types.KeyboardButton('Отмена')
admins.row(button1)
admins.row(button2)
admins.row(button3)
admins.row(button4)
admins.row(button5)
admins.row(button6)
admins.row(button7)
admins.row(button8)

def ddos(message):
    now = datetime.now()
    Users.get_last_msg_time(message.chat.id, 3, now.second)
    Users.get_last_msg_time(message.chat.id, 4, now.minute)
    if int(now.second) - Users.get_last_msg_time(message.chat.id, 1, now.second) < 1 and int(now.minute) == Users.get_last_msg_time(message.chat.id, 2, now.minute):
        return True
    else:
        return False

@bot.message_handler(commands=['Start', 'start'])
def start(message):
    user_id = message.chat.id
    splited = message.text.split()
    if not Users.user_exists(user_id):
        Users.create_user(user_id)
        # Users.increase_join_date(user_id)
        if len(splited) == 2:
            Users.increase_ref_count(splited[1], message.chat.id)
            bot.send_message(message.chat.id, 'Вы перешли сюда по реферальной ссылке')
    bot.send_message(message.chat.id, 'Хотите создать своего бота?\nТогда вам сюда: @ilnurKhalikov', reply_markup=menu)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Купить Dedicate Server':
            bot.send_message(message.chat.id, 'Выберите какой Dedicate Server вас интересует👇', reply_markup=main1)
        elif message.text == 'Партнерская программа':
            bot.send_message(message.chat.id, '''✅Принимаются любые дедики (с админ правами, амазон и прочий микс).
✅Принимается от 15 дедиков за одно обращение. 
✅Обработка дедиков на валидность занимает до 24 часов.
✅Работоспособность дедика должна сохраняться не менее 3х дней.
✅Минимальная оплата за дедик - 1.8$ и выше (зависит от качества).
✅Выплаты производятся на Qiwi, Яндекс Деньги, Банковскую карту.
✅Принимается до 500 дедиков в месяц и до 50 шт в день.''')
            if Users.get_dedicate(message.chat.id, '', 1) < 500:
                bot.send_message(message.chat.id, 'Какое количество дедиков вы желаете внести?', reply_markup=cancel)
                bot.register_next_step_handler(message, dedicate)
            else:
                bot.send_message(message.chat.id, 'Вы дали более 500 дедиков в месяц')
        elif message.text == 'F.A.Q':
            bot.send_message(message.chat.id, '''1. Как подключаться к дедику?
Все очень просто: жмем "пуск" "выполнить", вводим команду mstsc. В появившемся окне вводится имя компьютера - т.е. выданный вам ай пи адрес, далее жмем дополнительно (или параметры), вводим имя юзера, после чего жмем коннект. Откроется вход на удаленный рабочий стол, где нужно будет ввести пароль и жмем "ок". Собственно перед вами и будет рабочий стол сервера, где вы и будете творить.

2. Как залить софт на дедик?
Тоже нет ничего сложного. Если он (софт) находится в интернете - то все делаете как на своем компе - открываете браузер и скачиваете, если он находится у вас в компьютере - то сначала необходимо выложить его на любой файлообменник (dump.ru, sendspace.com и т.д.), а потом по полученной ссылке из браузера деда - опять таки скачать его.
Также можно к дискам дедика подключить ваш локальный диск через опции mstsc.

3. После покупки рекомендуем вам сменить пароль
После покупки рекомендуем вам сменить пароль на любой свой (это касается серверов из таблички, где уже есть отдельно созданная учетка; на ХР менять выданный доступ нельзя, следует создать себе для работы учетку и поставить патч на мультиюзерность со странички с ХР). Как сменить пароль? На деде жмете "start" "run" cmd. Вводите: net user пользователь пароль и enter, например: net user sql KJur665ed, в результате будет назначен пароль KJur665ed для пользователя sql.

4. Как создать нового пользователя на деде?
(При покупке админского дедика из таблички на сайте - это делать никчему, так как вам выдается уже готовая для работы учетка, можете лишь сменить пароль. Если же куплен дедик XP/Win7 - тогда учетка должна быть вами сделана). Например:
Жмем: "start" "run" пишем cmd и вводим:
net user sql 1234567 /add
net localgroup Administrators sql /add
В данном случае будет создана учетка sql с паролем 1234567
•Не забываем о том, что группа администраторов только на англоязычных дедиках называется Administrators, на прочих языковых разновидностях Windows - группа админов называется по другому (например русские дедики: Администраторы, испанские Administradores и т.д.). Как называется группа админов можно посмотреть в compmgmt.msc или (если на дедике домен) - dsa.msc
•Следует учитывать, что на новых версиях Windows Server (например 2008), при создании новой учетки или смене пароля вы можете получить ответ системы о недостаточности прав на выполненение этих операций. Не надо спешить возмущаться, что вам продали дедик без админ прав. Это специфика настроек безопасности и все прекрасно решается - всего навсего нужно запускать командную строку из пуска - через правую кнопоку мыши - "run as administrator", после чего все будет работать. Аналогично, возможно, понадобиться запускать ваш софт таким же образом, через правую кнопку мыши.

5. Что означает надпись "вход в локальный компьютер"?
В этом случае при входе на дедик, после ввода пароля вам необходимо в поле которое находится ПОД паролем выбрать другую строчку, ту, где написано "......(this computer)" и после этого уже входим на сервер.

6. Иногда бывает что после ввода логина и пароля не показывается рабочий стол.
Иногда бывает что после ввода логина и пароля не показывается рабочий стол сервера, т.к. автостартует какая либо программа (типа 1С и прочее). Данный вопрос легко решается следующим способом - логинимся в дедик, после чего жмем сочетание клавиш Ctrl+Alt+End, что вызовет диспетчер задач (дедика! а не ваш), после чего идем в меню File, new task, и набираем explorer, после чего жмем ОК и пойдет дальнейшая загрузка интерфейса дедика.

7. Как быть если в купленном дедике я вижу других "левых" пользователей?
Не надо в этом случае паниковать и спешить обвинять сервис в продаже "не в одни руки" - этого никогда не было и не будет. Во первых, следует точно быть уверенным что это НЕ локальные пользователи деда (так сказать хозяева).''')
            bot.send_message(message.chat.id, '''Во вторых избавиться от нежелательных соседей довольно таки несложно и с данной просьбой вам следует обратиться к консультанту @DedicateOperator_bot и вам обязательно помогут.

8. При попытке логина на дед видим сообщение “Нет доступных лицензий”.
При попытке логина на дед видим сообщение Нет доступных лицензий, для сервера терминалов (Remote session was disconnected because there are no Remote Desktop client access licenses). Лечение: жмем на своем компе "пуск", "выполнить" и туда вставляем команду reg delete "HKLM\SOFTWARE\Microsoft\MSLicensing" /f После этого конектимся к дедику.''')
        elif message.text == 'Отзывы':
            pass
        elif message.text == 'Go Back' or message.text == 'Отмена':
            bot.send_message(message.chat.id, 'Главное меню', reply_markup=menu)
        elif message.text == 'Оплата и гарантии':
            bot.send_message(message.chat.id, '''Схема работы - после согласования всех вопросов относительно покупки - покупатель оплачивает стоимость дедика, после чего получает доступ в виде ай пи адреса, логина и пароля на вход.

💳Оплата возможна через Webmoney, Яндекс деньги, Perfect Money, Qiwi. Оплату принимает ТОЛЬКО наш оператор, который прописан в описании бота.

✔️Для работы вам будет выдана уже готовая учетная запись с полными админскими правами. Админка доступ - выдается как правило после истечения срока гарантии или по настоятельному требованию клиента (в последнем случае уже будет невозможным обмен деда на иной, ввиду того что там не работает ваш софт и т.п.).
✔️Покупателю предоставляется помощь в настройке антивируса, если таковой будет мешать работе, настройке браузера для беспроблемного скачивания файлов, если были предприняты все меры, описанные в FAQ-е, но безрезультатно.
✔️При необходимости возможно рассматривать обмен ранее купленных (б/у) дедиков на другие. В этом случае "старые" дедики принимаются за 1/3 стоимости.

✅Что касается гарантии - она составляет 3 дня для серверов на базе ОС Server 2003/2008 и 1 день - для машин ХР, Win7, Win10 ("домашки"),  для русифицированных машин (нашими силами) - гарантия устанавливается равной 1 день, для дедиков, на которых настраивался VPN нашими силами - 2 дня, если клиент сам настраивает VPN сервер - гарантия НЕ дается.
✅Под гарантию попадают серверы к которым отсутствует подключение (т.е. оффлайн), сопровождающееся соответветствующим сообщением Windows, о том что данный рабочий стол отключен (наличие или отсутстствие пинга не влияет).
❌Случаи отсутствия доступа по поводу блокировки (смены пароля) учетной записи кем либо, отсутствии права на вход на сервер терминалов и прочее подобное - гарантийными НЕ являются.
❌Также, НЕ являются гарантийными случаи "смерти" дедиков в результате манипуляций клиента с ними как, например - русификация, перезагрузка, реконфигурирование сети/файерволла и т.п.
❌Аналогично, НЕ производятся замены в ситуации, когда не открывается какой-либо нужный вам конкретный сайт или не запускается ваша программа, которая по вашему мнению должна была запускаться. Максимум, вы можете вежливо (!) попросить продавца, при наличии свободного времени - попытаться помочь устранить эти проблемы, ну и в совсем исключительных случаях просить о замене. Пойти вам на встречу в этих случаях - это право продавца, но не обязанность, т.к. подобные моменты обсуждаются/чекаются до покупки, если вам это важно.
❗️Важно! В сервисе производятся ТОЛЬКО гарантийные замены серверов, возврат средств НЕ осуществляется, просьба это осознавать ДО покупки.

❌Клиенты, обращающиеся для решения какой либо проблемы, употребляющие в своей речи нецензурные обороты (а тем более в адрес работника поддержки)  -  не обслуживаются.''')
        elif message.text == 'admin' or message.text == 'админ' or message.text == 'Admin' or message.text == 'Админ':
            if message.chat.id in adm:
                bot.send_message(message.chat.id, 'Админ панель', reply_markup=admins)
                bot.register_next_step_handler(message, admin)
        elif message.text == 'Дедики с админ правами':
            s = ''
            i = 1
            db = sqlite3.connect('dedicate.db')
            sql = db.cursor()
            sql.execute("SELECT text FROM dedicate")
            id = sql.fetchall()
            for id in id:
                for id in id:
                    s += f'{i}. `{id}`\n'
                    i += 1
            db.commit()
            if len(s) != 0:
                bot.send_message(message.chat.id, f'{s}', parse_mode='Markdown')
                bot.send_message(message.chat.id, 'Выберете номер дедика указаный рядом с ним')
                bot.register_next_step_handler(message, dedicate_server)
            else:
                bot.send_message(message.chat.id, 'На данный момент доступных дедиков с админ правами нет')
        elif message.text == 'Дедики без админ прав':
            s = ''
            i = 1
            db = sqlite3.connect('dedicate.db')
            sql = db.cursor()
            sql.execute("SELECT text FROM dedicates")
            id = sql.fetchall()
            for id in id:
                for id in id:
                    s += f'{i}. `{id}`\n'
                    i += 1
            db.commit()
            if len(s) != 0:
                bot.send_message(message.chat.id, f'{s}', parse_mode='Markdown')
                bot.send_message(message.chat.id, 'Выберете номер дедика указаный рядом с ним')
                bot.register_next_step_handler(message, dedicates_server)
            else:
                bot.send_message(message.chat.id, 'На данный момент доступных дедиков без админ прав нет')

def dedicate(message):
    if message.text == 'Отмена':
        bot.send_message(message.chat.id, 'Главное меню', reply_markup=menu)
    else:
        bot.send_message(message.chat.id, 'Введите данные от дедиков в формате айпи:пароль и каждый с новой строки', reply_markup=cancel)
        bot.register_next_step_handler(message, server)

def server(message):
    if message.text == 'Отмена':
        bot.send_message(message.chat.id, 'Главное меню', reply_markup=menu)
    else:
        if len(message.text.split('\n')) == Users.get_dedicate(message.chat.id, '', 1):
            pass
        else:
            Users.get_dedicate(message.chat.id, len(message.text.split('\n')), 2)
        bot.send_message(adm[0], f'{message.chat.id}\n{message.text}')
        if message.chat.id == adm[0]:
            Users.get_dedicate(adm[0], -Users.get_dedicate(adm[0], '', 1), 2)
        bot.send_message(message.chat.id, 'Мы проверим ваши дедики и ответим вам в течении 48 часов', reply_markup=menu)

def admin(message):
    if message.text == 'Отмена':
        bot.send_message(message.chat.id, 'Главное меню', reply_markup=menu)
    elif message.text == 'Ответить на сообщение пользователю':
        bot.send_message(message.chat.id, 'Введите id пользователя и само сообщение, каждое с новой строки')
        bot.register_next_step_handler(message, answer)
    elif message.text == 'Обнулить кол-во дедиков':
        db = sqlite3.connect('user.db')
        sql = db.cursor()
        sql.execute("SELECT user_id FROM users")
        id = sql.fetchall()
        for id in id:
            for id in id:
                Users.get_dedicate(id, -Users.get_dedicate(id, '', 1), 2)
        bot.send_message(message.chat.id, "Обнуление завершено", reply_markup=menu)
        db.commit()
    elif message.text == 'Удалить дедик с админ правами':
        bot.send_message(message.chat.id, 'Укажите название дедика')
        bot.register_next_step_handler(message, del_dedicate)
    elif message.text == 'Удалить дедик без админ прав':
        bot.send_message(message.chat.id, 'Укажите название дедика')
        bot.register_next_step_handler(message, del_dedicates)
    elif message.text == 'Добавить дедик с админ правами':
        bot.send_message(message.chat.id, 'Введите название дедика')
        bot.register_next_step_handler(message, add_dedicate)
    elif message.text == 'Добавить дедик без админ прав':
        bot.send_message(message.chat.id, 'Введите название дедика')
        bot.register_next_step_handler(message, add_dedicates)
    elif message.text == 'Рассылка':
        bot.send_message(message.chat.id, 'Введите текст')
        bot.register_next_step_handler(message, rasslka)

def answer(message):
    bot.send_message(message.text.split('\n')[0], message.text.split('\n')[1])
    bot.send_message(message.chat.id, 'Сообщение отправлено!')

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

def dedicate_server(message):
    if message.text == 'Go Back' or message.text == 'Отмена':
        bot.send_message(message.chat.id, 'Главное меню', reply_markup=menu)
    elif message.text == 'Дедики без админ прав':
            s = ''
            i = 1
            db = sqlite3.connect('dedicate.db')
            sql = db.cursor()
            sql.execute("SELECT text FROM dedicates")
            id = sql.fetchall()
            for id in id:
                for id in id:
                    s += f'{i}. `{id}`\n'
                    i += 1
            db.commit()
            if len(s) != 0:
                bot.send_message(message.chat.id, f'{s}', parse_mode='Markdown')
                bot.send_message(message.chat.id, 'Выберете номер дедика указаный рядом с ним')
                bot.register_next_step_handler(message, dedicates_server)
            else:
                bot.send_message(message.chat.id, 'На данный момент доступных дедиков без админ прав нет')
    elif message.text == 'Дедики с админ правами':
        s = ''
        i = 1
        db = sqlite3.connect('dedicate.db')
        sql = db.cursor()
        sql.execute("SELECT text FROM dedicate")
        id = sql.fetchall()
        for id in id:
            for id in id:
                s += f'{i}. `{id}`\n'
                i += 1
        db.commit()
        if len(s) != 0:
            bot.send_message(message.chat.id, f'{s}', parse_mode='Markdown')
            bot.send_message(message.chat.id, 'Выберете номер дедика указаный рядом с ним')
            bot.register_next_step_handler(message, dedicate_server)
        else:
            bot.send_message(message.chat.id, 'На данный момент доступных дедиков с админ правами нет')
    else:
        bot.send_message(adm[0], f'Пользователь: `{message.chat.id}`\nЗахотел купить дедик с админ правами под номером {message.text}', parse_mode='Markdown')
        bot.send_message(message.chat.id, 'Запрос на покупку отправлен, ждите ответа в течении 48 часов', reply_markup=menu)

def dedicates_server(message):
    if message.text == 'Go Back' or message.text == 'Отмена':
        bot.send_message(message.chat.id, 'Главное меню', reply_markup=menu)
    elif message.text == 'Дедики без админ прав':
            s = ''
            i = 1
            db = sqlite3.connect('dedicate.db')
            sql = db.cursor()
            sql.execute("SELECT text FROM dedicates")
            id = sql.fetchall()
            for id in id:
                for id in id:
                    s += f'{i}. `{id}`\n'
                    i += 1
            db.commit()
            if len(s) != 0:
                bot.send_message(message.chat.id, f'{s}', parse_mode='Markdown')
                bot.send_message(message.chat.id, 'Выберете номер дедика указаный рядом с ним')
                bot.register_next_step_handler(message, dedicates_server)
            else:
                bot.send_message(message.chat.id, 'На данный момент доступных дедиков без админ прав нет')
    elif message.text == 'Дедики с админ правами':
        s = ''
        i = 1
        db = sqlite3.connect('dedicate.db')
        sql = db.cursor()
        sql.execute("SELECT text FROM dedicate")
        id = sql.fetchall()
        for id in id:
            for id in id:
                s += f'{i}. `{id}`\n'
                i += 1
        db.commit()
        if len(s) != 0:
            bot.send_message(message.chat.id, f'{s}', parse_mode='Markdown')
            bot.send_message(message.chat.id, 'Выберете номер дедика указаный рядом с ним')
            bot.register_next_step_handler(message, dedicate_server)
        else:
            bot.send_message(message.chat.id, 'На данный момент доступных дедиков с админ правами нет')
    else:
        bot.send_message(adm[0], f'Пользователь: `{message.chat.id}`\nЗахотел купить дедик без админ прав под номером {message.text}', parse_mode='Markdown')
        bot.send_message(message.chat.id, 'Запрос на покупку отправлен, ждите ответа в течении 48 часов', reply_markup=menu)

def del_dedicate(message):
    if message.text == 'Отмена':
        bot.send_message(message.chat.id, 'Главное меню', reply_markup=menu)
    else:
        db = sqlite3.connect('dedicate.db')
        sql = db.cursor()
        sql.execute("SELECT text FROM dedicate")
        id = sql.fetchall()
        for id in id:
            for id in id:
                if id == message.text:
                    sql.execute(f"DELETE FROM dedicate WHERE text = '{message.text}'")
        bot.send_message(message.chat.id, "Удаление завершено", reply_markup=menu)
        db.commit()

def del_dedicates(message):
    if message.text == 'Отмена':
        bot.send_message(message.chat.id, 'Главное меню', reply_markup=menu)
    else:
        db = sqlite3.connect('dedicate.db')
        sql = db.cursor()
        sql.execute("SELECT text FROM dedicates")
        id = sql.fetchall()
        for id in id:
            for id in id:
                if id == message.text:
                    sql.execute(f"DELETE FROM dedicates WHERE text = '{message.text}'")
        bot.send_message(message.chat.id, "Удаление завершено", reply_markup=menu)
        db.commit()

def add_dedicate(message):
    if message.text == 'Отмена':
        bot.send_message(message.chat.id, 'Главное меню', reply_markup=menu)
    else:
        db = sqlite3.connect('dedicate.db')
        sql = db.cursor()
        sql.execute(f"INSERT INTO dedicate (text) VALUES ('{message.text}')")
        bot.send_message(message.chat.id, "Добавление завершено", reply_markup=menu)
        db.commit()

def add_dedicates(message):
    if message.text == 'Отмена':
        bot.send_message(message.chat.id, 'Главное меню', reply_markup=menu)
    else:
        db = sqlite3.connect('dedicate.db')
        sql = db.cursor()
        sql.execute(f"INSERT INTO dedicates (text) VALUES ('{message.text}')")
        bot.send_message(message.chat.id, "Добавление завершено", reply_markup=menu)
        db.commit()

while True:
    try:
        bot.polling()
    except Exception as e:
        print(e)
        bot.send_message(adm[0], f'Error: {e}')