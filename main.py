from time import sleep
from random import randint
from os import system
from config import *

system("title " + prefix)
system("color 2")
print("\033[32m")
progress_gui = "█"

speed_time = size / (time_to_sleep * 100)
for i in range(progress_start, 100):
    sleep(time_to_sleep)

    print(f"{text.format(size=size, progress=progress_start)}|{progress_gui*progress_start}| \tETA {randint(speed_time, speed_time + (speed_time * 0.2))} mb/s")

    progress_start += 1

input()