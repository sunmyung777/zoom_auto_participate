import webbrowser
import threading
from datetime import datetime
from pynput.keyboard import Key, Controller
import time
import json

with open('subjects.json', encoding='utf-8') as subjects_json: # open subject json file
    subjects = json.load(subjects_json)

with open('timetable.json', encoding='utf-8') as timetable_json: # open timetable json file
    timetable = json.load(timetable_json)

weekday = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'] # define weekday
today = weekday[datetime.today().weekday()] # day of week
keyboard = Controller()

def printTodaySubjects(): # print today't time table
    print(f'『{today}day time table』')
    for classtime in range(1,timetable[today]["cnt"]+1):
        print(str(classtime) + "교시 : " + timetable[today][str(classtime)])

def meetingURL(meetingID, password): # return meeting link
    url = f'zoommtg://zoom.us/join?action=join&pwd={password}&confno={str(meetingID)}'
    return url

def openMeeting(subject):
    meetingID = subjects[subject]["meetingID"]
    password = subjects[subject]["password"]
    url = meetingURL(meetingID, password)
    webbrowser.open(url)

printTodaySubjects()

while(True):
    currnet_time = datetime.now().strftime('%H:%M') # HH:MM
    if(currnet_time == timetable["start-time"]["morning-assembly"]):
        openMeeting("조례/종례")
    elif((currnet_time == timetable["start-time"]["afterschool-assembly"]["6th"]) and (today=='wed')):
        openMeeting("조례/종례")
        time.sleep(5)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
    elif(currnet_time == timetable["start-time"]["afterschool-assembly"]["6th"] and today=='wed'):
        openMeeting("조례/종례")
        time.sleep(5)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

    for classtime in range(1, timetable[today]["cnt"]+1):
        if(currnet_time == timetable["start-time"][str(classtime)]):
            subject = timetable[today][str(classtime)]
            openMeeting(subject)
            time.sleep(3)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
    # print(f'현재시각 : {currnet_time}')
    time.sleep(60) # 60초(= 1분)마다 검사

