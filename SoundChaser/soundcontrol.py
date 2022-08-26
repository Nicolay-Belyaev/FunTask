from datetime import datetime
from sound import *
import time


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

def LogWriter():
    f = open(r"C:\Users\123\Desktop\GeekBrains\FunTask\SoundChaser\log.txt", "a+") # хардкод. надо сделать так, что бы лог файл создавался к каталоге скрипта.
    dt_as_string = (str(datetime.now())[5:16])
    current_volume_as_string = str(Sound.current_volume())
    f.write(f'{dt_as_string}, Current volume set to: {current_volume_as_string} \n')
    f.close()

while True:
    SoundChaser()
    LogWriter()
    time.sleep(600)