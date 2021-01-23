import time
import random
from sensors import proximity_sensors

def green():
  print("Signal Green" , end="")

def red():
  print("Signal Red" , end="")

def timer(t):
  while t:
    mins, secs = divmod(t,60)
    timer = "{:02d}:{:02d}".format(mins,secs)
    print(timer,end="")
    time.sleep(1)
    t -= 1
    if t == 0:
      print(f'00:00')

def signals(traffic_road1,traffic_road2):
  if traffic_road1 >= traffic_road2:
    green()
    print("For Road 1")
    red()
    print("For Road 2")
    traffic_road1 = traffic_road1 -50
    timer(20)
  elif traffic_road2 < traffic_road1:
    green()
    print("For road 2")
    red()
    print("For road 1")
    traffic_road2 = traffic_road2 - 50
    timer(20)