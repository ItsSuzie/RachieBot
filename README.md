# RachieBot - The Universal Bot!
I'm building a shitposting Bot that can be used in many places!
Telegram - Out there working!
Discord - Ported from Telegram, successfully working!

Too play with RachieBot, search her in telegram. The name is RachieBot.
No discord link avaliable yet.

Telegram Commands she can do, Commands with arguments afterwards:
- /caps ANYTHING YOU TYPE HERE WILL BE IN ALL CAPS
- /WeIrD AnYtHiNg YoU TyPe HeRe WiLl Be SpElT In WeIrD CaSe WhErE EaCh ChArAcTeR AlTeRnAtEs CaSe. LiKe ThE SpOnGeBoB MeMe
- /owoify Huohhhh. anythng uu type hewe wiww become vewy owoifyed ;3
- /echo Anything you type here, i'll repeat!

Commands without arguments:
- /start - recites the starting text when you first launched her
- /rp - Prints the infamous furry owo whats this copypasta
- /tragedy - prints the amazing farth plageus the wise copypasta
- /navyseal - prints the legendary navyseal copypasta

Discord commands are the same, just replace the '/' with '$'

have fun!

Created by @Sindiewen



Setting up locally for yourself:

Now this is for my own telegram and discord bot @rachiebot, but any of the code could be used for your own bot as long as you bring your own bot.
Here's the steps:
- Make sure pip is installed (for something like Ubuntu, apt install python3-pip, idk about other os's)

Telegram:
- Get the Python Telegram bot library here ---> https://github.com/python-telegram-bot/python-telegram-bot (if python 3, use pip3 instal ...)
  - python3 -m pip install -U python-telegram-bot
- Create the file "createTelegramBot.py", import telegram, and create a function 'def createTelegramBot()' that returns the bot with it's token 'return telegram.bot(token='token for your bot goes here')

For Discord:
  - Install the python library: python3 -m pip install -U discord.py
  - Create the file 'createDiscordBot.py'
    - In there, import discord, then create a method 'def createDiscordClient()' which has the single line 'return discord.Client()", and another method called 'def runDiscordClient(client)' which has 'client.run('bot token here').
    - save that in the src directory.

- run program as following:

Manual Method:
  - Run as is within terminal, and seeing stuff in the terminal (idk what it's called)
    - For telegram:
      - within the src directory 'python3 rachiebot.py'
    - For Discord:
      - within the src directory 'python3 rbDiscord.py'
  - This runs the program as a single instance as itself.
  - Use ctrl + c to kill the bot


To Run in the background:
  - Telegram and Discord share the same command:
    - Telegram: 'nohup python3 rachibot.py &'
    - Discord: 'nohup python3 rbDiscord.py &'
      - (this prevents some weird issues with it trying to create multiple instandces of the bot? i think) thks https://askubuntu.com/questions/396654/how-to-run-a-python-program-in-the-background-even-after-closing-the-terminal <3
    - Since it's in the background, you'll need to get it's process id and kill is

To kill the bot's background process:
- run:
  - telegram: 'ps -ax | grep rachiebot.py' then kill it's process id
  - Discord: 'ps -ax | grep rbDiscord.py' then kill it's process ID


You can also use this shell script I made rachiebot.sh!
- ./rachiebot.sh <arg>
    - Arguments include:
        - starttg : starts the telegram bot
        - startdiscord: starts the discord bot
        - startbgtg : starts telegram bot, runs in background
        - startbgdiscord: starts discord bot, runs in background
        - getpidtg : gets the pid of the telegram program so you can kill it
        - getpiddiscord: gets the pid of the discord program so you can kill it
- Then to kill the bot, same as above:
  - get the pid and then kill it's process ID


Final step: shitpost
