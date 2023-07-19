import datetime
import time
from playsound import playsound

# using deffunction set the alarm-time
def set_alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("It's an alarm time")
            print("Play the alarm")
            playsound(r"C:\Users\madhu\Downloads\Alarm.mp3.mp3")
            break
            time.sleep(1)


time_formats = ["%H:%M:%S", "%H:%M"]
print("Assigned time formats:")
for i, time_format in enumerate(time_formats, start=1):
    print(str(i) + " " + time_format)
choice = int(input("Enter your choice:"))

selected_format = time_formats[choice - 1]
alarm_time = input("Enter the alarm time(" + selected_format + "):")
if selected_format == "%H:%M:%S":
    alarm_time = datetime.datetime.strptime(alarm_time, "%H:%M:%S").strftime("%H:%M:%S")
if selected_format == "%H:%M":
    alarm_time = datetime.datetime.strptime(alarm_time, "%H:%M").strftime("%H:%M:%S")
# function call
set_alarm(alarm_time)
