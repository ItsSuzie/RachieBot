'''
Entry for the main python program.

Sets up the bot for use.
'''
# A very specific python file called createTelegramBot.py in the same directory is needed
# to run the bot, create it, and use the following commented code below with your token
'''
import telegram

token = "bot token goes here"
def createTelegramBot():
   return telegram.Bot(token='token')

def getToken()
   return token
   '''

# Not adding that file for security reasons to my bot
import createTelegramBot

# Get telegram package
# Make sure you pip (or pip3) install telegram-python-bot
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

# Python logger
import logging

# Importing any external programs to not bloat this file
import WeIrD_StRiNg_CaSe
import owoifier
import copypastas


### <Summary>
### Initiates the telegram bot
### </Summary>
def initRachieBotTelegram():
    # Init telegram bot
    print(" ------------------------------ ")
    print(" Setting RachieBot, Telegram... ")
    print(" ------------------------------ ")


    # creates bot, see iport above
    bot = createTelegramBot.createTelegramBot()
    print(bot.get_me())

    #Creates updater object
    teleUpdater = Updater(token=createTelegramBot.getToken(), use_context=True)
    teleDispatcher = teleUpdater.dispatcher

    #Create logging object
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    # Start the command handler
    start_handler = CommandHandler('start', start)
    # echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)

    # commands
    echo_handler = CommandHandler('echo', echo)
    caps_handler = CommandHandler('caps', caps)
    WeIrD_handler = CommandHandler("weird", WeIrD)
    owo_handler = CommandHandler("owoify", owoify)

    # copypastas
    rp_handler = CommandHandler('rp', rp)
    tragedy_handler = CommandHandler('tragedy', tragedy)
    navy_handler = CommandHandler("navyseal", navyseal)

    #memes
    # meme_handler = CommandHandler('meme', meme)

    # Create dispatchers
    teleDispatcher.add_handler(start_handler)
    teleDispatcher.add_handler(echo_handler)
    teleDispatcher.add_handler(caps_handler)  
    teleDispatcher.add_handler(WeIrD_handler) 
    teleDispatcher.add_handler(owo_handler) 
    teleDispatcher.add_handler(rp_handler)
    teleDispatcher.add_handler(tragedy_handler)
    teleDispatcher.add_handler(navy_handler)

    #run the bot
    print("\n\nBot setup successful. Now running!\n\n")
    teleUpdater.start_polling()



# --------------------- #
# Bot functions
# --------------------- #


# --------------------------- #
# commands without arguments
# --------------------------- #

# recites the starting text when you first launched her
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=copypastas.cp_intro)

# Prints owo copypasta
def rp(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=copypastas.cp_rp)

# Prints darth plageus the wise copypasta
def tragedy(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=copypastas.cp_tragedy)

# Print the navy seal copypasta
def navyseal(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=copypastas.cp_nvs)



# ----------------------- #
# commands with arguments
# ----------------------- #

# ANYTHING YOU TYPE HERE WILL BE IN ALL CAPS
def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

# AnYtHiNg YoU TyPe HeRe WiLl Be SpElT In WeIrD CaSe WhErE EaCh ChArAcTeR AlTeRnAtEs CaSe. LiKe ThE SpOnGeBoB MeMe
def WeIrD(update, context):
    # Get the text
    text_WeIrD = ' '.join(context.args)

    #print cancer
    context.bot.send_message(chat_id=update.effective_chat.id, text=WeIrD_StRiNg_CaSe.to_weird_case(text_WeIrD))

# Huohhhh. anythng uu type hewe wiww become vewy owoifyed ;3
def owoify(update, context):
    # get text
    text_owo = " ".join(context.args)

    #print owo
    context.bot.send_message(chat_id=update.effective_chat.id, text=owoifier.to_owo(text_owo))


# just type anything inside the chat box without commands, rachiebot will echo it back
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


# def meme(update, context):



