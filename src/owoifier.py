'''
# My attempt basing it off of https://owoifier--black-is-back.repl.co/. didnt work lol
import re
import math
from random import randint

def to_owo(owoStr):
    faces = ["(・`ω´・)",";;w;;","owo","UwU",">w<","^w^"]

    owoText = "" #owoStr
    print(owoText)

    owoText = re.sub('(?:r|l)/g', "w", owoStr)
    owoText = re.sub('(?:R|L)/g', "W", owoText)
    owoText = re.sub('n([aeiou])/g', 'ny$1', owoText)
    owoText = re.sub('N([aeiou])/g', 'Ny$1', owoText)
    owoText = re.sub('N([AEIOU])/g', 'Ny$1', owoText)
    owoText = re.sub('ove/g', "uv", owoText)

    print(owoText)
    # for i in owoText:
    #     if i == '!':
    #         owoText = owoText
    owoText.replace("!", " " + faces[math.floor(randint(0, len(faces) - 1))])
    print(owoText)

    return owoText


myStr = input ("Enter text to owoify: ")
print(to_owo(myStr))
'''

# Using the code from the repo https://github.com/Alfredooe/OWOifier modified for a function and readability owo
import random

def to_owo(owo):

    #Substitutions
    substitution = {
        "r":"w",
        "l":"w",
        "R":"W",
        "L":"W",
        "no":"nu",
        "has":"haz",
        "have":"haz",
        "you":"uu",
        "the":"da",
        "R":"W",
        "The":"Da" 
    }

    #Prefixes
    prefix = [
        "<3 ",
        "H-hewwo?? ",
        "HIIII! ",
        "Haiiii! ",
        "Huohhhh. ",
        "OWO ",
        "OwO ",
        "UwU ",
        "88w88",
        "H-h-hi",
    ]

    #Suffixes
    suffix = [
        " :3",
        " UwU",
        " ʕʘ‿ʘʔ",
        " >_>",
        " ^_^",
        "..",
        " Huoh.",
        " ^-^",
        " ;_;",
        " xD",
        " x3",
        " :D",
        " :P",
        " ;3",
        " XDDD",
        ", fwendo",
        " ㅇㅅㅇ",
        " (人◕ω◕)",
        " （＾ｖ＾）",
        " Sigh.",
        " ._.",
        " >_<"
        "xD xD xD",
        ":D :D :D",
    ]

    for word, initial in substitution.items():
        owo = owo.replace(word.lower(), initial)
    output = random.choice(prefix) + owo + random.choice(suffix)

    return output

# myStr = input ("Enter text to owoify: ")
# print(to_owo(myStr))
