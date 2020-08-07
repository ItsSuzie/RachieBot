'''
Entry for the main python program.

Sets up the bot for use.
'''
# A very specific python file called createTelegramBot.py in the same directory.
# it initiates the telegram bot
# import telegram
# def createTelegramBot():
#    return telegram.Bot(token='bot token goes here')
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


### <Summary
### program entry
### </Summary>
def main():
#    print("Hello world!")
    
    initRachieBot() 

### <Summary>
### Initiates the telegram bot
### </Summary>
def initRachieBot():
    # Init telegram bot
    print("Setting up rachie bot...")

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
    echo_handler = CommandHandler('echo', echo)
    caps_handler = CommandHandler('caps', caps)
    WeIrD_handler = CommandHandler("WeIrD", WeIrD)
    owo_handler = CommandHandler("owoify", owoify)
    rp_handler = CommandHandler('rp', rp)
    tragedy_handler = CommandHandler('tragedy', tragedy)
    navy_handler = CommandHandler("navyseal", navyseal)
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
    print("\n\nBot setup successful. Now running!")
    teleUpdater.start_polling()



# --------------------- #
# Bot functions
# --------------------- #

# commands without arguments

# recites the starting text when you first launched her
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello world! I'm RachieBot! Rachie's shitposter bot!\n\nI have a variety of commands to play with!\n\nCommands she can do, Commands with arguments afterwards:\n- /caps ANYTHING YOU TYPE HERE WILL BE IN ALL CAPS\n- /WeIrD AnYtHiNg YoU TyPe HeRe WiLl Be SpElT In WeIrD CaSe WhErE EaCh ChArAcTeR AlTeRnAtEs CaSe. LiKe ThE SpOnGeBoB MeMe\n- /owoify Huohhhh. anythng uu type hewe wiww become vewy owoifyed ;3\n- /echo Anything you type here, i'll repeat!\n\nCommands without arguments:\n- /start - recites the starting text when you first launched her\n- /rp - Prints the infamous furry owo whats this copypasta\n- /tragedy - prints the amazing farth plageus the wise copypasta\n/navyseal - prints the legendary navyseal copypasta\n\nhave fun!\n\nCreated by @Sindiewen\nSource code avaliable here: https://github.com/Sindiewen/RachieBot-Telegram-Bot")

# Prints owo copypasta
def rp(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Rawr x3 nuzzles how are you pounces on you you're so warm o3o notices you have a bulge o: someone's happy ;) nuzzles your necky wecky~ murr~ hehehe rubbies your bulgy wolgy you're so big :oooo rubbies more on your bulgy wolgy it doesn't stop growing ·///· kisses you and lickies your necky daddy likies (; nuzzles wuzzles I hope daddy really likes $: wiggles butt and squirms I want to see your big daddy meat~ wiggles butt I have a little itch o3o wags tail can you please get my itch~ puts paws on your chest nyea~ its a seven inch itch rubs your chest can you help me pwease squirms pwetty pwease sad face I need to be punished runs paws down your chest and bites lip like I need to be punished really good~ paws on your bulge as I lick my lips I'm getting thirsty. I can go for some milk unbuttons your pants as my eyes glow you smell so musky :v licks shaft mmmm~")

# Prints darth plageus the wise copypasta
def tragedy(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Did you ever hear the Tragedy of Darth Plagueis the wise? I thought not. It's not a story the Jedi would tell you. It's a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life... He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful... the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. It's ironic he could save others from death, but not himself.")

# Print the navy seal copypasta
def navyseal(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="What the fuck did you just fucking say about me, you little bitch? I'll have you know I graduated top of my class in the Navy Seals, and I've been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I'm the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You're fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that's just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little 'clever' comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn't, you didn't, and now you're paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You're fucking dead, kiddo.")


# commands with arguments

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










if __name__ == "__main__":
    main()
