import telebot
bot = telebot.TeleBot('1573966877:AAE1gytAXuQAkjDbDWJfAqDyUvnV-nITOqw')
keyboard1 = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
keyboard1.row('Інструкція')
keyboard1.row('Відділи')
keyboard1.row('Про бот')
keyboard2 = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
keyboard2.row('Виробничо-технічна група')
keyboard2.row('Бухгалтерія ')
keyboard2.row('Охорона праці ')
keyboard2.row('Повернутися на попередню вкладинку ')
keyboard3 = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
keyboard3.row('Електротехнічні установи')
keyboard3.row('Повернутися на попередню вкладку')
keyboard8 = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
keyboard8.row('Поглиблені довідники')
keyboard8.row('Загальні довідники з охорони праці')
keyboard8.row('Повернутися на попередню вкладку')
keyboard4 = telebot.types.InlineKeyboardMarkup()
url_button1 = telebot.types.InlineKeyboardButton(text="Перейти на сайт Флибуста", url="https://flibusta.site")
url_button2 = telebot.types.InlineKeyboardButton(text="Перейти на сайт Альдебаран", url="https://aldebaran.ru")
url_button3 = telebot.types.InlineKeyboardButton(text="Перейти на сайт Рутрекер", url="https://rutracker.org/forum/viewforum.php?f=2054")
keyboard4.add(url_button1)
keyboard4.add(url_button2)
keyboard4.add(url_button3)
keyboard5 = telebot.types.InlineKeyboardMarkup()
url_button4 = telebot.types.InlineKeyboardButton(text="1", url="https://drive.google.com/file/d/1gC7n3IDKQlUwNEkkCFf9wNnWkiQ3XiMU/view?usp=sharing")
url_button5 = telebot.types.InlineKeyboardButton(text="2", url="https://drive.google.com/file/d/1CdIulSRMWNQrHHlK42HirIF2_N5YRIyM/view?usp=sharing")
keyboard5.add(url_button4)
keyboard5.add(url_button5)
keyboard6 = telebot.types.InlineKeyboardMarkup()
url_button6 = telebot.types.InlineKeyboardButton(text="1", url="https://drive.google.com/file/d/1BEOFiAIXdr9cuAipIxYK0ALihwUNCtJX/view?usp=sharing")
url_button7 = telebot.types.InlineKeyboardButton(text="2", url="https://github.com/LymarN/directory/blob/main/Ктиторов%20А.Ф.%20Основные%20приемы%20и%20способы%20выполнения%20электромонтажных%20работ.djvu")
keyboard6.add(url_button6)
keyboard6.add(url_button7)
keyboard7 = telebot.types.InlineKeyboardMarkup()
url_button7 = telebot.types.InlineKeyboardButton(text="1", url="https://drive.google.com/file/d/1qRUDe3bTz8nyaU2xdVMotO91orXSbLjW/view?usp=sharing")
url_button8 = telebot.types.InlineKeyboardButton(text="2", url="https://drive.google.com/file/d/1LlgPrNyTzryADMudAdpGOzESP_oproRG/view?usp=sharing")
url_button11 = telebot.types.InlineKeyboardButton(text="3", url="https://drive.google.com/file/d/1qOZLkuEGh9lcPSc-yW1k5TWXweW3pJeO/view?usp=sharing")
keyboard7.add(url_button7, url_button8, url_button11)
keyboard9 = telebot.types.InlineKeyboardMarkup()
url_button9 = telebot.types.InlineKeyboardButton(text="1", url="https://drive.google.com/file/d/1Fqh2z-SDELfLepAl9LVyQqI5zsOQQ5MQ/view?usp=sharing")
url_button10 = telebot.types.InlineKeyboardButton(text="2", url="https://drive.google.com/file/d/1m30Iug-3rbH7arSWXEh6XAhgi7_Sm7Hw/view?usp=sharing")
keyboard9.add(url_button9, url_button10)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Вітаю!❤️😉 \n'
                                      'Цей бот створений для зручного використання довідникової літератури📚 в будь-який час⏳ в будь-якому місці. \n'
                                      'Обери відділ, в якому бажаєш знайти потрібний довідник✅', reply_markup=keyboard1)

@bot.message_handler()
def send_text(message):
    if message.text.lower() == 'інструкція':
        bot.send_message(message.chat.id, 'Вітаю!😇 '
                                          'Для того, щоб знайти літературу📚, потрібно обрати відділ.\n '
                                          'Наразі в боті є декілька відділів:🗂 \n'
                                          '- Виробничо-технічна група💡,\n'
                                          '- Бухгалтерія💵 \n'
                                          '- Охорона праці⚠️.\n'
                                          'В кожному відділі є декілька тем, за яким відсортовано літературу\n'
                                          'Потрібний довідник ви можете відкрити за посиланням на Google диску🌐\n'
                                          'Оскільки деякі екземпляри є лише в архівах, їх доведеться завантажити📥')
    elif message.text.lower() == 'відділи':
        bot.send_message(message.chat.id, 'Обери потрібний відділ✅', reply_markup=keyboard2)
    elif message.text.lower() == 'виробничо-технічна група':
        bot.send_message(message.chat.id, 'Обери потрібну тему✅', reply_markup=keyboard3)
    elif message.text.lower() == 'електротехнічні установи':
        bot.send_message(message.chat.id, 'Обери потрібний довідник✅ \n'
                                          '1️⃣ - Ктиторов А.Ф. Основные приемы и способы выполнения электромонтажных работ \n'
                                          '2️⃣ - Справочник электрика \n', reply_markup=keyboard5)
    elif message.text.lower() == 'бухгалтерія':
        bot.send_message(message.chat.id, 'Обери потрібний довідник✅ \n'
                                          '1️⃣ - Бухгалтерский учет \n'
                                          '2️⃣ -  \n', reply_markup=keyboard6)
    elif message.text.lower() == 'охорона праці':
        bot.send_message(message.chat.id, 'Обери потрібну тему✅', reply_markup=keyboard8)
    elif message.text.lower() == 'загальні довідники з охорони праці':
        bot.send_message(message.chat.id, 'Обери потрібний довідник✅ \n'
                                          '1️⃣ - Охорона праці. Інструктаж для офісних працівників \n'
                                          '2️⃣ - Управление охраной труда \n'
                                          '3️⃣-- Полный справочник по охраной труда ', reply_markup=keyboard7)
    elif message.text.lower() == 'поглиблені довідники':
        bot.send_message(message.chat.id, 'Обери потрібний довідник✅ \n'
                                          '1️⃣ - ОП. Обеспечение прав работников \n'
                                          '2️⃣ - ОП. Утрата трудоспособности ', reply_markup=keyboard9)
    elif message.text.lower() == 'повернутися на попередню вкладку':
        bot.send_message(message.chat.id, 'Обери потрібний відділ✅', reply_markup=keyboard2)
    elif message.text.lower() == 'повернутися на попередню вкладинку':
        bot.send_message(message.chat.id, 'Обери потрібний відділ✅', reply_markup=keyboard1)
    elif message.text.lower() == 'про бот':
        bot.send_message(message.chat.id, 'directory_bot - це пробний бот, який покликаний надавати довідникову літературу за межами підприємства.\n'
                                          'Кількість довідників наразі невелика, але в майбутньому бібліотека буде розширятися\n'
                                          'Побажання щодо роботи боту можна відправити на електронну пошту aleksandrovahopa15@gmail.com')
    elif not message.text.isdigit():
        # Состояние не меняем, поэтому только выводим сообщение об ошибке и ждём дальше
        # hi jgh
        bot.send_message(message.chat.id, "Якщо у нас немає літератури 😔, яку ви шукаєте,  \n "
                                          "можливо, вам варто пошукати на додаткових ресурсах🔎", reply_markup=keyboard4)
        return

bot.polling()