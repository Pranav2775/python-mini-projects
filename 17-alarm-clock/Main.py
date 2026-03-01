import time
import datetime
import pygame

# initialize pygame mixer
pygame.mixer.init()

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Current time: {current_time}", end="\r")

        if current_time == alarm_time:
            print("\nWAKE UP! ⏰")
            pygame.mixer.music.load("alarm.mp3")  # put an mp3 file in same folder
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)
            break

        time.sleep(1)

alarm_time = input("Enter alarm time (HH:MM:SS): ")
set_alarm(alarm_time)
