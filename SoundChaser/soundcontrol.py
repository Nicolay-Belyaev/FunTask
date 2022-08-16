from datetime import datetime
from sound import *
import time
from random import randint

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
        rand_volume = randint(90, 100)
        Sound.volume_set(rand_volume)
        print(f'Volume set to {rand_volume}')
    else:
        Sound.volume_min()
        print('Volume set to min')

while True:
    SoundChaser()
    time.sleep(10)