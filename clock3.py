import datetime

current_time = datetime.datetime.now()
print("Current time is:", current_time)

from playsound import playsound
alarmHour = int(input("Enter Hour: "))
alarmMin = int(input("Enter minutes: "))
alarmAm = input("am / pm:")

if alarmAm=="pm":
    alarmHour+=12

while True:
  if alarmHour==datetime.datetime.now().hour and alarmMin==datetime.datetime.now().minute:
        print("Playing..")
        playsound("Alarm.mp3")
        break

