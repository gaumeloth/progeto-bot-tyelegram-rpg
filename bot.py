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
    await message.reply(message.text)

@dp.message_handler(text='Inverti testo')
async def reverse_text(message: types.Message):
    # Esempio di utilizzo di logging
    logging.info('Ricevuto comando "Inverti testo"')
    reversed_text = message.text[::-1]
    await message.reply(reversed_text)

@dp.message_handler(text='Cerca su Google')
async def google_search(message: types.Message):
    # Esempio di utilizzo di logging
    logging.info('Ricevuto comando "Cerca su Google"')
    query = message.text
    results = search(query, num_results=4)
    response = "Risultati della ricerca:\n"
    for result in results:
        title = result['title']
        link = result['link']
        response += f"\n{title}\n{link}\n"
    await message.reply(response)

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp)
