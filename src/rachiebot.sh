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
    printf "Rachiebot Process ID = ${$$}"
    rm nohup.out
    nohup python3 src/rachiebot.py &
}

# For finding and killing the process
function killBG()
{

}

# If the user entered 1 argument 
if (( "$#" = "1" ))
then
    # if the user types start as it's argument
    if (( "$1" = "start" ))
    then 
        start $1 $$
    fi

else # invalid number of parameters entered
    printf "Invalid number of arguments. You must enter 1 argument"
fi

