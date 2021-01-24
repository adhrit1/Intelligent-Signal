import time
from tkinter import *


def green():
  # Green Light
  print("Signal Green ",end="")

def red():
  # Red Light
  print("Signal Red ",end="")


def yellow():
  # Yellow Light
    print("Yellow Signals For Both Signals")
    time.sleep(5)

#The stopwatch program is below
def timer(t):

    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
        if t == 0:
            print(f'00:00')


# The following program compares the amount of traffic on the two roads based on the sensor inputs to decide which road gets the light.


def signals(traffic_road1, traffic_road2):

    while traffic_road1 > 0 or traffic_road2 > 0:
        
        if traffic_road1 >= traffic_road2:
            green()
            print("For Road 1")
            red()
            print("For Road 2")
            
            traffic_road1 = traffic_road1 - 40
            timer(20)
            if traffic_road1<0:
              traffic_road1=0
            print("The length of traffic in road 1 is", traffic_road1,"metres")
            print("The length of traffic in road 2 is", traffic_road2,"metres")
            if traffic_road2 > 0 or traffic_road1 > 0:
              if traffic_road2 > traffic_road1:
                yellow()
        elif traffic_road2 > traffic_road1:
            green()
            print("For Road 2")
            red()
            print("For Road 1")
            #traffic in that time gone by
            traffic_road2 = traffic_road2 - 40
            timer(20)
            if traffic_road2<0:
              traffic_road2=0
            print("The lenght of traffic in road 1 is", traffic_road1,"metres")
            print("The lenght of traffic in road 2 is", traffic_road2,"metres")
            if traffic_road2 > 0 or traffic_road1 > 0:
              if traffic_road1 >= traffic_road2:
                yellow()
