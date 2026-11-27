import time
from datetime import datetime
import sys
import os, platform

def main():
    study_session = 0
    attempts = 1

    while True:
        try:
            study_session = int(input("Please specify study session in minutes: "))
            if study_session <= 0 or study_session > 720:
                print("Please enter a value between 1 and 720...")
                if attempts == 3:
                    print("You weren´t going to study anyway...")
                    time.sleep(250 / 1000)
                    print("PROGRAM TERMINATED")
                    sys.exit()
                attempts += 1
                continue
            else:
                break
        except ValueError:
            print("Invalid value.\nPROGRAM TERMINATED")
            sys.exit()

    study_session_seconds = study_session * 60

    while True:

        print(f"Your study session is {hh_mm_ss(study_session_seconds)}")
        
        study_session_seconds -= 1
        if study_session_seconds == 0:
            print("Your study session is over!")
            time.sleep(1000/1000)
            sys.exit()
        
        time.sleep(1000/1000)
        clear()

def clear():
    #Temporary function in the pre tk phase...
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def hh_mm_ss(seconds):
    #converts seconds to hh:mm:ss format
    hh = seconds // 3600
    mm = (seconds - (hh * 3600)) // 60
    ss = (seconds - (mm * 60)) % 60
    zero_sec = ""
    zero_min = ""
    if mm < 10:
        zero_min = "0"
    if ss < 10:
        zero_sec = "0"
    return f"{hh}:{zero_min}{mm}:{zero_sec}{ss}"

main()