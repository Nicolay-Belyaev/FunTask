from curses.ascii import SO
from datetime import datetime
from sound import *
from time import *
import schedule

def DayTimeChecker():
    dt = datetime.now()
    weekdays = [1, 2, 3, 4, 5]
    hours_for_weekdays = [8, 9, 10, 11, 12, 15, 16, 17, 18, 19, 20, 21, 22]
    
    weekends = [6, 7]
    hours_for_weekends = [12, 15, 16, 17, 18, 19, 20]

    current_day = dt.isoweekday()
    current_hour = dt.time().hour

    return (current_day in weekdays and current_hour in hours_for_weekdays) or (current_day in weekends and current_hour in hours_for_weekends)

def SoundChaser():
    if DayTimeChecker() == True:
        Sound.volume_max()
    else:
        Sound.volume_min()

schedule.every(30).minutes.do(SoundChaser)