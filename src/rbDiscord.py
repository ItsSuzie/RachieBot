# Import the discord module needed
import discord
import discord.ext.commands
import random

from discord.message import Message


# python file, to create the discord bot 
# Not adding the createDiscordBot.py file for security purposes.
# Comment below for reference
'''
import discord

token = 'bot token goes here'

def createDiscordClient():
    return discord.Client()

def runDiscordClient(client):
    client.run(token)
'''
import createDiscordBot



# Import the other telegram plugins needed
import WeIrD_StRiNg_CaSe
import owoifier
import copypastas
import timezoneConverter


# Creates discord client
client = createDiscordBot.createDiscordClient()



# storing specific Channel ID's
iStricerEmotesOnly = 823709164630179860
MinraEmotesOnly = 822856634950221835


# rachiebot start message
startmsg = "Hello world! I'm RachieBot! Rachie's shitposter bot!\n\nI have a variety of commands to play with!\n\nCommands I can do, Commands with arguments afterwards:\n- $caps ANYTHING YOU TYPE HERE WILL BE IN ALL CAPS\n- $WeIrD AnYtHiNg YoU TyPe HeRe WiLl Be SpElT In WeIrD CaSe WhErE EaCh ChArAcTeR AlTeRnAtEs CaSe. LiKe ThE SpOnGeBoB MeMe\n- $owoify Huohhhh. anythng uu type hewe wiww become vewy owoifyed ;3\n- $echo Anything you type here, i'll repeat!\n\nCommands without arguments:\n- $start - recites the starting text when you first launched her\n- $rp - Prints the infamous furry owo whats this copypasta\n- $tragedy - prints the amazing farth plageus the wise copypasta\n- $navyseal - prints the legendary navyseal copypasta\n\nhave fun!\n\nCreated by @Sindiewen on Twitter, Github, Telegram and Sindiewen#8507 on discord\nSource code avaliable here: https://github.com/Sindiewen/RachieBot"


print(" ------------------------------ ")
print(" Starting Rachiebot, Discord... ")
print(" ------------------------------ ")


# --------------------- #
# Bot functions
# --------------------- #

# Runs when the bot is ready
@client.event
async def on_ready():
    print('Logged on as {0.user}!'.format(client))
    print("Bot setup successful, New Running!\n\n")


# Runs when the a message has been posted. waits for speicfic commands
@client.event
async def on_message(message):
    # ensure bot doesnt talk to itself
    if message.author == client.user:
        return

    # await message.channel.send("Mesage from {0.author}: {0.content}".format(message))
    # print(message.content)

    # stores the message
    newMsg = "{0.content}".format(message)

    # RachieBot - start:
    if message.content.startswith('$start'):
        await message.channel.send(startmsg)

    
    # commands
    if message.content.startswith("$echo"):
        await message.channel.send(removeCommand(1, newMsg))
    
    if message.content.startswith("$say"):
        await message.delete()
        await message.channel.send(removeCommand(1, newMsg))

    if message.content.startswith('$caps'):
        await message.channel.send(removeCommand(1, newMsg.upper()))

    if message.content.startswith("$weird"):
        await message.channel.send(WeIrD_StRiNg_CaSe.to_weird_case(removeCommand(1, newMsg)))

    if message.content.startswith('$owoify'):
        await message.channel.send(owoifier.to_owo(removeCommand(1, newMsg)))

    



    # Copypastas
    if message.content.startswith('$rp'):
        await message.channel.send(copypastas.cp_rp)

    if message.content.startswith("$tragedy"):
        await message.channel.send(copypastas.cp_tragedy)

    if message.content.startswith("$navyseal"):
        await message.channel.send(copypastas.cp_nvs)

    if message.content.startswith("$fitness"):
        await message.channel.send(copypastas.cp_fitness)



    # if bot is mentioned
    if client.user.mentioned_in(message):
        randNum = random.randint(1,8)
        if randNum == 1:
            await message.reply(copypastas.cp_rp)
        if randNum == 2:
            await message.reply(copypastas.cp_tragedy)
        if randNum == 3:
            await message.reply(copypastas.cp_nvs)
        if randNum == 4:
            await message.reply(copypastas.cp_fitness)
        if randNum == 5:
            await message.reply("i love you bby")
        if randNum == 6:
            await message.reply("c-can i get a hug pls {0.author}?")
        if randNum == 7:
            await message.reply("may i please get some huggie wuggies? uwu")
        if randNum == 8:
            await message.reply("yay, you're sweet, I love you {0.author} <3")

    


    # notices stuffs
    # if message.content.startswith('sus'):
    # if 'sus' in message.content: 
    #     await message.reply("no u", mention_author = True)

    if message.content.startswith('$rbHello'):
        await message.channel.send('Hello!!!') 


    # CHeck the emotes channel if a valid emote has been printed
    if message.content.startswith('$deleteme'):
        await message.delete()
        await message.channel.send("mesage deleted from {0.author}: {0.content}".format(message))

    # within emotes only channel, if message doesnt have emote, delete messge
    # if client.get_channel(iStricerEmotesOnly).
    #     await client.get_channel(iStricerEmotesOnly).delete()
    #     await client.get_channel(iStricerEmotesOnly).send("message deleted from {0.author}: {0.content}".format(message))
    # if message.channel == iStricerEmotesOnly:
    channel = client.get_channel(iStricerEmotesOnly)
    if message.channel == iStricerEmotesOnly:
        await channel.send("this is a test")

    



    # timezone program
    if message.content.startswith("tz!"):
        await message.reply(timezoneConverter.timezoneConversion("{0.content}".format(message)), mention_author = True)
    


    # print('print from {0.author}: {0.content}'.format(message))



# When called, passes a string and removes the command
def removeCommand(spacing, content):
    finalStr = content.split()
    finalStr = finalStr[spacing:]
    finalStr = ' '.join(finalStr)
    return finalStr


# remove text from emote only channel
# def emoteOnlyRemoveText():
    # a




# Runs the discord client with the token inside createDiscordBot.py
createDiscordBot.runDiscordClient(client)