from pyrogram import Client
from pyrogram import filters
from pyrogram.types import *
from pycoingecko import CoinGeckoAPI
from requests import *
import random



bot = Client(session_name="Bot",
             api_hash='1b852557e771a37f4609749afeeeed78',
             api_id='427059',
             bot_token='2104577084:AAEt7_CldnJMWfmcxLJbc8Rhmhzi8heIr9E')

# Start Function

@bot.on_message(filters.command('start'))
async def Start(client, message):

    chat_id = message.chat.id
    username = message.chat.username

    replymarkup = ReplyKeyboardMarkup(keyboard=[

        ['Music', 'Wallpaper', 'CryptoPrice'],
        ['Help']
    ],
    resize_keyboard=True)

    await bot.send_message(chat_id, f"""

@{username}

Welcome To W.T.F Bot

Please Use Keyboard

""", reply_markup=replymarkup)


@bot.on_message()
async def main(client, message):

    
    text = message.text
    chat_id = message.chat.id
    username = message.chat.username

    if text == 'CryptoPrice':

        InlineKeyboard = InlineKeyboardMarkup(inline_keyboard=[

            [
                InlineKeyboardButton('BTC', callback_data='bitcoin'),
                InlineKeyboardButton('ETH', callback_data='ethereum'),
                InlineKeyboardButton('BNB', callback_data='binancecoin')
            ],

            [
                InlineKeyboardButton('BLOCK', callback_data='blocknet'),
                InlineKeyboardButton('DOT', callback_data='polkadot'),
                InlineKeyboardButton('DOGE', callback_data='dogecoin')
            ],
            [
                InlineKeyboardButton('FTM', callback_data='fantom'),
                InlineKeyboardButton('ZIL', callback_data='zilliqa'),
                InlineKeyboardButton('TRX', callback_data='tron')
            ],
            [
                InlineKeyboardButton('BTT', callback_data='bittorrent'),
                InlineKeyboardButton('AVAX', callback_data='avalanch'),
                InlineKeyboardButton('ADA', callback_data='cardano')
            ],
            [
                InlineKeyboardButton('XRP', callback_data='ripple'),
                InlineKeyboardButton('CHZ', callback_data='chiliz'),
                InlineKeyboardButton('SOL', callback_data='solana')
            ],
            [

                InlineKeyboardButton('KDA', callback_data='kadena'),
                InlineKeyboardButton('NANO', callback_data='nano'),
                InlineKeyboardButton('VET', callback_data='vechain')
            ]
        ])

        await bot.send_message(chat_id, "Please Select Any Coin", reply_markup=InlineKeyboard)


    if text == "Music":

        music = ['1.mp3', '2.mp3', '3.mp3', '4.mp3', '5.mp3', '6.mp3', '7.mp3', '8.mp3', '9.mp3', '10.mp3', '11.mp3', '12.mp3', '13.mp3', '14.mp3']
        selected_music = random.choice(music)
        await bot.send_audio(chat_id, selected_music, '@AsrarSchoolbot')

    if text == "Wallpaper":

        Wallpaper = ['w1.jpg', 'w2.jpg', 'w3.jpg', 'w4.jpg', 'w5.jpg', 'w6.jpg', 'w7.jpg', 'w8.jpg', 'w9.jpg', 'w10.jpg', 'w12.jpg', 'w13.jpg', 'w14.jpg', 'w15.jpg', 'w16.jpg', 'w17.jpg', 'w18.jpg',
                     'w19.jpg', 'w20.png', 'w21.jpg', 'w22.jpg', 'w23.png', 'w24.jpg']
        selected_wallpaper = random.choice(Wallpaper)

        await bot.send_document(chat_id, selected_wallpaper, caption='@AsrarSchoolbot')

    if text == "Help":

        await bot.send_message(chat_id, f"""
@{username} Hi

This Can Send Random Wallpaper, Music and Found a Crypto Prices For you


Author = MSK
""")

@bot.on_callback_query()
async def CryptoPriceQueryController(client, call):

    message_text = call.message.text
    message_id = call.message.message_id
    data = call.data
    chat_id = call.message.from_user.id

    if message_text == 'Please Select Any Coin':
        
        api = CoinGeckoAPI()
        Price = api.get_price(ids=data, vs_currencies='usd')
        Price = Price[data]['usd']
        Price = float(Price)

        await bot.edit_message_text(chat_id, message_id, f"""
        
At This Moment 

{data} Price is ==> {Price}

""")


bot.run()