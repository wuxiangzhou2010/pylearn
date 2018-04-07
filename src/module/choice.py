# https://www.youtube.com/watch?v=CqvZ3vGoGs0&t=1065s
# demo on some of the modules
import my_module
# import my_module as mm 
# from my_module import *
# from my_module import find_index as fi, Test

import random
import datetime
import calendar
import math

import os

list = ["Math", "History", "Geo", "Bio"]
choice = my_module.find_index(list, "Geo")
print('my_module: ' + str(choice))
choice = random.choice(list)
print('random: ' + choice)

rads  = math.radians(90)
print(math.sin(rads))

today = datetime.date.today()
print(today)

print(calendar.isleap(2000))


print(os.getcwd())
print(os.__file__)