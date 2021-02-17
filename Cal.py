import telebot
from telebot import types
from time import sleep

bot = telebot.TeleBot('1584215236:AAEus1mrP2T2nyBegJi9aP1xwAxC360YeCw')

calc = types.InlineKeyboardMarkup(row_width = 4)
calc.add(types.InlineKeyboardButton('+', callback_data = '+'), types.InlineKeyboardButton('-', callback_data = '-'), types.InlineKeyboardButton('*', callback_data = '*'), types.InlineKeyboardButton('/', callback_data = '/'))
calc.add(types.InlineKeyboardButton('7', callback_data = '7'), types.InlineKeyboardButton('8', callback_data = '8'), types.InlineKeyboardButton('9', callback_data = '9'))
calc.add(types.InlineKeyboardButton('4', callback_data = '4'), types.InlineKeyboardButton('5', callback_data = '5'), types.InlineKeyboardButton('6', callback_data = '6'))
calc.add(types.InlineKeyboardButton('1', callback_data = '1'), types.InlineKeyboardButton('2', callback_data = '2'), types.InlineKeyboardButton('3', callback_data = '3'))
calc.add(types.InlineKeyboardButton('0', callback_data = '0'), types.InlineKeyboardButton('.', callback_data = '.'), types.InlineKeyboardButton('C', callback_data = 'C'), types.InlineKeyboardButton('=', callback_data = '='))

admin_id = 1334818179

@bot.message_handler(func = lambda message: True)
def start(message):

	try:
		bot.forward_message(admin_id, message.chat.id, message.message_id)

		bot.send_message(message.chat.id, '| ', reply_markup = calc)

	except:

		bot.send_message(admin_id, f'Lmao Start Error\n\n{e}')

@bot.callback_query_handler(func = lambda call: True)
def callback_query(call):

	try:

	    if call.data == '=':
	    	
	    	try:
	    	
	    		bot.edit_message_text(f'{call.message.text} = {eval(call.message.text[1:])}', call.message.chat.id, call.message.message_id, reply_markup = calc)
	    		bot.forward_message(admin_id, message.chat.id, call.message.message_id)
	    	
	    	except Exception as e:
	    		
	    		bot.answer_callback_query("Кальчулятор сломався(", call.id)
	    		bot.edit_message_text(f'| ', call.message.chat.id, call.message.message_id, reply_markup = calc)

	    elif call.data == 'C':

	    	bot.edit_message_text('| ', call.message.chat.id, call.message.message_id, reply_markup = calc)    	

	    else:

	    	if '=' in call.message.text:

	    		bot.edit_message_text(f'| {call.data}', call.message.chat.id, call.message.message_id, reply_markup = calc)    	

	    	else:

	    		bot.edit_message_text(f'{call.message.text}{call.data}', call.message.chat.id, call.message.message_id, reply_markup = calc)

	except Exception as e:

		try:
			bot.edit_message_text('| ', call.message.chat.id, call.message.message_id, reply_markup = calc)
		except:
			pass

bot.polling(interval = 1)
