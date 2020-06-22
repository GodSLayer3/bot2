import telebot
from bot import bot

name = ''
gender = ''
age = 0


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, "Привет.Как тебя зовут?")
        bot.register_next_step_handler(message, get_name)
    else:
        # bot.send_message(message.from_user.id,
        #                  'Упс. Я не знаю такой команды. Давай зайдем в главное меню? Или если ты хочешь начать все '
        #                  'сначала напиши /start.')
        if message.text == "Информация о вас":
            text = 'Тебе ' + str(age) + ' лет, тебя зовут ' + name + '. Твой пол: ' + gender
            keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
            keyboard2.row('Назад')
            bot.send_message(message.from_user.id, text, reply_markup=keyboard2)
            bot.register_next_step_handler(message, back)
        elif message.text == "Настройки":
            settings_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            settings_markup.row('Изменить имя', 'Изменить возраст', 'Изменить пол', 'Назад')
            bot.send_message(message.chat.id, "Что хочешь поменять:", reply_markup=settings_markup)
            bot.register_next_step_handler(message, changesettings)
        elif message.text == "Назад":
            keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
            keyboard.row('Настройки', 'Информация о вас')
            bot.send_message(message.chat.id, "Выбери что дальше", reply_markup=keyboard)
            bot.register_next_step_handler(message, settings2)


def get_name(message):
    global name
    if len(message.text) > 2 and len(message.text) < 20:
        name = message.text
        keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard.row('Мужской', 'Женский')
        bot.send_message(message.from_user.id, "Какой твой пол?", reply_markup=keyboard)
        bot.register_next_step_handler(message, get_gender)
    else:
        bot.send_message(message.from_user.id, 'От двух до 20')
        bot.register_next_step_handler(message, get_name)


def get_gender(message):
    global gender
    if message.text == "Мужской":
        gender = message.text
        bot.send_message(message.from_user.id, 'Сколько тебе лет?')
        bot.register_next_step_handler(message, get_age)
    elif message.text == "Женский":
        gender = message.text
        bot.send_message(message.from_user.id, 'Сколько тебе лет?')
        bot.register_next_step_handler(message, get_age)
    else:
        bot.send_message(message.from_user.id, 'Попробуй ещё раз')
        bot.register_next_step_handler(message, get_gender)


def get_age(message):
    global age
    if not str(message.text).isdigit():
        bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
        bot.register_next_step_handler(message, get_age)
    else:
        if int(message.text) < 2 or int(message.text) > 120:
            bot.send_message(message.chat.id, "Упс. Напиши пожалуйста реальный возраст.")
            bot.register_next_step_handler(message, get_age)
        else:
            age = int(message.text)
            keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
            keyboard.row('Настройки', 'Информация о вас')
            bot.send_message(message.chat.id, "Выбери что дальше", reply_markup=keyboard)
            bot.register_next_step_handler(message, settings)



def settings(message):
    global gender
    global age
    global name
    if message.text == "Информация о вас":
        text = 'Тебе ' + str(age) + ' лет, тебя зовут ' + name + '. Твой пол: ' + gender
        keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard2.row('Назад')
        bot.send_message(message.from_user.id, text, reply_markup=keyboard2)
        bot.register_next_step_handler(message, back)
    elif message.text == "Настройки":
        settings_markup = telebot.types.ReplyKeyboardMarkup(True, True)
        settings_markup.row('Изменить имя', 'Изменить возраст', 'Изменить пол', 'Назад')
        bot.send_message(message.chat.id, "Что хочешь поменять:", reply_markup=settings_markup)
        if message.text == "Назад":
            keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
            keyboard.row('Настройки', 'Информация о вас')
            bot.send_message(message.chat.id, "Выбери что дальше", reply_markup=keyboard)
            bot.register_next_step_handler(message, settings2)
        bot.register_next_step_handler(message, changesettings)


def back(message):
    if message.text == "Назад":
        keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard.row('Настройки', 'Информация о вас')
        bot.send_message(message.chat.id, "Выбери что дальше", reply_markup=keyboard)
        bot.register_next_step_handler(message, settings2)


def settings2(message):
    if message.text == "Настройки":
        settings_markup = telebot.types.ReplyKeyboardMarkup(True, True)
        settings_markup.row('Изменить имя', 'Изменить возраст', 'Изменить пол', 'Назад')
        bot.send_message(message.chat.id, "Что хочешь поменять:", reply_markup=settings_markup)
        if message.text == "Назад":
            keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
            keyboard.row('Настройки', 'Информация о вас')
            bot.send_message(message.chat.id, "Выбери что дальше", reply_markup=keyboard)
        else:
            bot.register_next_step_handler(message, changesettings)
    elif message.text == "Информация о вас":
        text = 'Тебе ' + str(age) + ' лет, тебя зовут ' + name + '. Твой пол: ' + gender
        keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard2.row('Назад')
        bot.send_message(message.from_user.id, text, reply_markup=keyboard2)
        bot.register_next_step_handler(message, back)


def changesettings(message):
    if message.text == "Изменить пол":
        keyboard3 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard3.row('Мужской', 'Женский')
        bot.send_message(message.from_user.id, "Какой твой пол?", reply_markup=keyboard3)
        bot.register_next_step_handler(message, changegender)
    elif message.text == "Изменить возраст":
        bot.send_message(message.chat.id, "Какой твой возраст?")
        bot.register_next_step_handler(message, changeage)
    elif message.text == "Изменить имя":
        bot.send_message(message.chat.id, "Какое новое имя?")
        bot.register_next_step_handler(message, changename)


def changegender(message):
    global gender
    if message.text == "Мужской":
        gender = message.text
    elif message.text == "Женский":
        gender = message.text
    else:
        bot.send_message(message.from_user.id, 'Попробуй ещё раз')
        bot.register_next_step_handler(message, changegender)
    keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboard2.row('Назад')
    bot.send_message(message.chat.id, "Запомнил", reply_markup=keyboard2)
    bot.register_next_step_handler(message, back)


def changeage(message):
    global age
    if not str(message.text).isdigit():
        bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
        bot.register_next_step_handler(message, changeage)
    else:
        if int(message.text) < 2 or int(message.text) > 120:
            bot.send_message(message.chat.id, "Упс. Напиши пожалуйста реальный возраст.")
            bot.register_next_step_handler(message, changeage)
        else:
            age = int(message.text)
            keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
            keyboard2.row('Назад')
            bot.send_message(message.chat.id, "Запомнил", reply_markup=keyboard2)
            bot.register_next_step_handler(message, back)


def changename(message):
    global name
    if len(message.text) > 2 and len(message.text) < 20:
        name = message.text
        keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard2.row('Назад')
        bot.send_message(message.chat.id, "Запомнил", reply_markup=keyboard2)
    else:
        bot.send_message(message.from_user.id, 'От двух до 20')
        bot.register_next_step_handler(message, changename)
    bot.register_next_step_handler(message, back)
bot.polling()
