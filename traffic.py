import time 


def green():
  print("Signal Green ",end="")

def red():
  print("Signal Red ",end="")

def timer(t):
  while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
        if t==0:
          print(f'00:00')

def signals(traffic_road1,traffic_road2,):
  
  
  while (traffic_road1 and traffic_road2) >= 0:
    #checks the amount of traffic on both roads
    if traffic_road1 >= traffic_road2:
      green()
      print("For Road 1")
      red()
      print("For Road 2")
      #traffic in that time gone by
      traffic_road1 = traffic_road1 - 40
      timer(20)
    elif traffic_road2 > traffic_road1:
      green()
      print("For Road 2")
      red()
      print("For Road 1")
      #traffic in that time gone by
      traffic_road2 = traffic_road2 -40
      timer(20)