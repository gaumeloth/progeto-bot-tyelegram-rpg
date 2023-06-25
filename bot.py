import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from googlesearch import search
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Configura il logger di base
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

bot = Bot(token="5685925571:AAE2AK9kGZSNfEMkpUTOmw0_RT_uMkWgy48")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    # Crea la tastiera personalizzata
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton('Ripeti messaggio'))
    keyboard.add(KeyboardButton('Inverti testo'))
    keyboard.add(KeyboardButton('Cerca su Google'))

    # Invia il messaggio di benvenuto con la tastiera personalizzata
    await message.reply("Ciao! Benvenuto al tuo bot. Utilizza i pulsanti per le azioni disponibili.", reply_markup=keyboard)

@dp.message_handler(text='Ripeti messaggio')
async def repeat_message(message: types.Message):
    # Esempio di utilizzo di logging
    logging.info('Ricevuto comando "Ripeti messaggio"')

    # Chiedi all'utente il messaggio da ripetere
    await message.reply("Inserisci il messaggio da ripetere:")

@dp.message_handler(text='Inverti testo')
async def reverse_text(message: types.Message):
    # Esempio di utilizzo di logging
    logging.info('Ricevuto comando "Inverti testo"')

    # Chiedi all'utente il testo da invertire
    await message.reply("Inserisci il testo da invertire:")

@dp.message_handler(text='Cerca su Google')
async def google_search(message: types.Message):
    # Esempio di utilizzo di logging
    logging.info('Ricevuto comando "Cerca su Google"')

    # Chiedi all'utente il termine di ricerca
    await message.reply("Inserisci il termine di ricerca su Google:")

@dp.message_handler()
async def handle_user_reply(message: types.Message):
    # Gestisci la risposta dell'utente in base al comando selezionato
    if message.text == 'Ripeti messaggio':
        await message.reply(message.text)
    elif message.text == 'Inverti testo':
        await message.reply(message.text[::-1])
    elif message.text == 'Cerca su Google':
        search_term = message.text
        results = search(search_term, num=8, stop=8)

        response = "Risultati della ricerca su Google:\n\n"

        for idx, result in enumerate(results, 1):
            response += f"{idx}. <a href='{result}'>{result}</a>\n"

        await message.reply(response, parse_mode='HTML')

# Aggiungi gli altri gestori dei messaggi come prima

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp)
