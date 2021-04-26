''' this program is meant for the Spring Generation for timezone conversion
This will return a string that will be posted into chat, replying to the one who
created the command, and take the current time in it's time zone, and it will convert to whatever timezone you need.

!7pstest
- 7 is the current time
- pst is the 'from' timezone
- est is the 'to' timezone

Breaking up each character in the string to allow for easy conversion
return in this format: 
7PM pst -> 10pm est : time difference is +3 hours
'''

import pendulum

#timezones
timezoneDict = {
    "akst": "US/Alaska",
    "alaska": "US/Alaska",
    "hst": "HST",
    "Hawaii": "HST",
    "pst": "PST8PDT",
    "pacific": "PST8PDT",
    "mst": "MST",
    "mountain": "MST",
    "cst": "CST6CDT",
    "central": "CST6CDT",
    "est": "EST",
    "eastern": "EST",
    "gb": "GB"
}

def timezoneConversion(timezone):
    '''
    Return: string of converted, formatted timezone
    '''

    # split into list
    timeList = timezone.split()


    # ignore the first element, it's the command

    # if the length of the list is 5 eleemtns,
    # it's comverting a specific time to a new time
    if len(timeList) == 5:
        # 0 = tz! | 1 = from time | 2 = am/pm | 3 = from timezone | 4 = to timezone

        # get 24 hour version of time
        time24 = from12HourTo24Hour(int(timeList[1]), timeList[2])

        myTime = pendulum.datetime(2021, 1, 1, time24, 0, 0, 0, timezoneDict[timeList[3]])
        convert = myTime.in_timezone(timezoneDict[timeList[4]])
        timeDiff = convert.diff(myTime).in_hours()
        # print("printing converted time")
        # print(convert)
        # print(convert.strftime('%I:%M:%S %p'))
        # print(convert.strftime('From ' + timeList[1] + ':00:00 ' + timeList[2] + ' ' + timeList[3] + ' to %I:%M:%S %p ' + timeList[4] + "\n Time difference is " + str(timeDiff) + " hours"))
        return convert.strftime('From ' + timeList[1] + ':00:00 ' + timeList[2] + ' ' + timeList[3] + ' to %I:%M:%S %p ' + timeList[4])

    # elif len(timeList) == 4:
    #     myTime = pendulum

    else:
        return "Illegal command. Please enter a legal timezone command.\nexample: tz! 7 pm pst est"
        


    

    #return time

def from12HourTo24Hour(ampmTime, ampm):
    # if the time is in pm, add 12 to the current time, assuming that the number doesnt exceed 24
    # print("old time")
    # print(ampmTime)
    newTime = 0
    if ampm == "pm":
        if ampmTime == 12:
            newTime = 00
        else:
            newTime = ampmTime + 12

    # print("new time")
    # print(newTime)
    # print("\n\n")
    return newTime
    

input = input("enter command:")
timezoneConversion(input)