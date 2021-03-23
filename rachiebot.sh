#!/bin/bash
# An easy program to start and (eventually) stop rachiebot
# if on zsh: https://stackoverflow.com/questions/53229221/terminal-error-zsh-permission-denied-startup-sh
# run this command:
# cd ~/the/script/folder
#
# chmod +x ./startup.sh

function startTG()
{
    printf "Starting Rachiebot Telegram..."
    python3 src/rachiebot.py
}

function startDiscord()
{
    printf "Starting Rachiebot Discord..."
    python3 src/rbDiscord.py
}

function startBGTG()
{
    printf "Starting Rachiebot, running in background..."
    rm nohup.out
    nohup python3 src/rachiebot.py &
    # printf "Rachiebot Process ID = ${$$}"
}

function startBGDiscord()
{
    printf "Starting Rachiebot discord, running in background..."
    rm nohup.out
    nohup python3 src/rbDiscord.py &
}

# For finding and killing the process
# function killBG()
# {
    # Im curious how this can be done. probably try and get the current pid of the program
# }

function getPIDTG()
{
    ps -ax | grep rachiebot.py
}

function getPIDDiscord()
{
    ps -ax | grep rbDiscord.py
}

# If the user entered 1 argument 
if [ "$#" = 1 ]
then
    # if the user types start as it's argument
    if [ "$1" == 'starttelegram' ]
    then 
        startTG
    
    elif [ "$1" == 'startdiscord' ]
    then
        startDiscord

    elif [ "$1" == 'startbgtg' ]
    then
        startBGTG

    elif [ "$1" == 'startbgdiscord' ]
    then
        startBGDiscord

    elif [ "$1" == "getpidtg" ]
    then
        getPIDTG

    elif [ "$1" == "getpiddiscord" ]
    then
        getPIDDiscord
    # elif [ "$1" == 'stop' ]
    # then
    #     # killBG
    fi

else # invalid number of parameters entered
    printf "Invalid number of arguments. You must enter 1 argument"
fi

