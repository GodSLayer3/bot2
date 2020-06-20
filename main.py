import telebot
from telebot import types

bot = telebot.TeleBot('1229183954:AAGS4_Ro8X36bEKsWGKsnSZk4EiXiVh6GEE')

name = '';
gender = '';
age = 0;


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, "Привет.Как тебя зовут?");
        bot.register_next_step_handler(message, get_name);  # следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, 'Напиши /start');


def get_name(message):  # получаем фамилию
    global name;
    name = message.text;
    bot.send_message(message.from_user.id, "Какой твой пол?")
    bot.register_next_step_handler(message, get_gender);


def get_gender(message):
    global gender
    if message.text == "Мужской":
        gender = message.text
        bot.send_message(message.from_user.id, 'Сколько тебе лет?');
        bot.register_next_step_handler(message, get_age);
    elif message.text == "Женский":
        pol = message.text
        bot.send_message(message.from_user.id, 'Сколько тебе лет?');
        bot.register_next_step_handler(message, get_age);
    else:
        bot.send_message(message.from_user.id, 'Попробуй ещё раз');
        bot.register_next_step_handler(message, get_gender);


def get_age(message):
    global age;
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста');
        keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard.row('Настройки', 'Информация о вас')
        bot.send_message(message.chat.id, "Выбери что дальше", reply_markup=keyboard)
        bot.register_next_step_handler(message, settings);


def settings(message):
    global gender
    global age
    global name
    if message.text == "Информация о вас":
        text = 'Тебе ' + str(age) + ' лет, тебя зовут ' + name + '. Твой пол: ' + gender;
        keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard2.row('Назад')
        bot.send_message(message.from_user.id, text, reply_markup=keyboard2)
        bot.register_next_step_handler(message, back);
    elif message.text == "Настройки":
        settings_markup = telebot.types.ReplyKeyboardMarkup(True, True)
        settings_markup.row('Изменить имя', 'Изменить возраст', 'Изменить пол', 'Назад')
        bot.send_message(message.chat.id, "Что хочешь поменять:", reply_markup=settings_markup)
        bot.register_next_step_handler(message, changesettings);
    bot.register_next_step_handler(message, back);


def back(message):
    if message.text == "Назад":
        keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard.row('Настройки', 'Информация о вас')
        bot.send_message(message.chat.id, "Выбери что дальше", reply_markup=keyboard)
        bot.register_next_step_handler(message, settings2);


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
            bot.register_next_step_handler(message, changesettings);
    elif message.text == "Информация о вас":
        text = 'Тебе ' + str(age) + ' лет, тебя зовут ' + name + '. Твой пол: ' + gender;
        keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard2.row('Назад')
        bot.send_message(message.from_user.id, text, reply_markup=keyboard2)
        bot.register_next_step_handler(message, back);


def changesettings(message):
    if message.text == "Изменить пол":
        bot.send_message(message.chat.id, "Какой твой пол?")
        bot.register_next_step_handler(message, changegender);
    elif message.text == "Изменить возраст":
        bot.send_message(message.chat.id, "Какой твой возраст?")
        bot.register_next_step_handler(message, changeage);
    elif message.text == "Изменить имя":
        bot.send_message(message.chat.id, "Какое новое имя?")
        bot.register_next_step_handler(message, changename);

def changegender(message):
    global gender
    if message.text == "Мужской":
        gender = message.text
    elif message.text == "Женский":
        gender = message.text
    else:
        bot.send_message(message.from_user.id, 'Попробуй ещё раз');
        bot.register_next_step_handler(message, changesettings);
    keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboard2.row('Назад')
    bot.send_message(message.chat.id, "Запомнил", reply_markup=keyboard2)
    bot.register_next_step_handler(message, back);
def changeage(message):
    global age
    while age == 0:
        try:
            age = int(message.text)
            bot.register_next_step_handler(message, back);
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста');
            bot.register_next_step_handler(message, changeage);
    keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboard2.row('Назад')
    bot.send_message(message.chat.id, "Запомнил", reply_markup=keyboard2)
    bot.register_next_step_handler(message, back);

def changename(message):
    global name
    name = message.text;
    keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboard2.row('Назад')
    bot.send_message(message.chat.id, "Запомнил", reply_markup=keyboard2)
    bot.register_next_step_handler(message, back);
bot.polling()
