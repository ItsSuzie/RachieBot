#!/bin/bash
# An easy program to start and (eventually) stop rachiebot

function start()
{
    printf "Starting Rachiebot..."
    python3 src/rachiebot.py
}

function startBG()
{
    printf "Starting Rachiebot in background..."
    rm nohup.out
    nohup python3 src/rachiebot.py &
    # printf "Rachiebot Process ID = ${$$}"
}

# For finding and killing the process
# function killBG()
# {
    # Im curious how this can be done. probably try and get the current pid of the program
# }

function getPID()
{
    ps -ax | grep rachiebot.py
}

# If the user entered 1 argument 
if [ "$#" = 1 ]
then
    # if the user types start as it's argument
    if [ "$1" == 'start' ]
    then 
        start
    
    elif [ "$1" == 'startbg' ]
    then
        startBG

    elif [ "$1" == "getPID" ]
    then
        getPID
    # elif [ "$1" == 'stop' ]
    # then
    #     # killBG
    fi

else # invalid number of parameters entered
    printf "Invalid number of arguments. You must enter 1 argument"
fi

