import time
import random
from tkinter import *
from traffic import signals
from sensors import dist_sensors, sound_sensor

window = Tk()
window.title("Intelligent Signal")
window.geometry('420x200')

road1 = Label(window,text="Road 1")
road1.grid(column=1,row=0)

road2 = Label(window,text="Road 2")
road2.grid(column=3, row=0)

dist_sensor_A = Label(window,text="First Sensor")
dist_sensor_A.grid(column=1,row=1)
data1_A = random.randint(1,10)
data1_A_text = Label(window,text = data1_A)
data1_A_text.grid(column=2,row=1)

dist_sensor2_A = Label(window,text="First Sensor")
dist_sensor2_A.grid(column=3,row=1)
data2_A = random.randint(1,10)
data2_A_text = Label(window,text=data2_A)
data2_A_text.grid(column=4,row=1)

dist_sensor_B = Label(window,text="Second Sensor")
dist_sensor_B.grid(column=1,row=2)
data1_B = random.randint(1,10)
data1_B_text = Label(window,text = data1_B)
data1_B_text.grid(column=2,row=2)

dist_sensor2_B = Label(window,text="Second Sensor")
dist_sensor2_B.grid(column=3,row=2)
data2_B = random.randint(1,10)
data2_B_text = Label(window,text=data2_B)
data2_B_text.grid(column=4,row=2)

dist_sensor_C = Label(window,text="Third Sensor")
dist_sensor_C.grid(column=1,row=3)
data1_C = random.randint(1,10)
data1_C_text = Label(window,text = data1_C)
data1_C_text.grid(column=2,row=3)

dist_sensor2_C = Label(window,text="Third Sensor")
dist_sensor2_C.grid(column=3,row=3)
data2_C = random.randint(1,10)
data2_C_text = Label(window,text=data2_C)
data2_C_text.grid(column=4,row=3)

dist_sensor_D = Label(window,text="Fourth Sensor")
dist_sensor_D.grid(column=1,row=4)
data1_D = random.randint(1,10)
data1_D_text = Label(window,text = data1_D)
data1_D_text.grid(column=2,row=4)

dist_sensor2_D = Label(window,text="Fourth Sensor")
dist_sensor2_D.grid(column=3,row=4)
data2_D = random.randint(1,10)
data2_D_text = Label(window,text=data2_D)
data2_D_text.grid(column=4,row=4)

dist_sensor_E = Label(window,text="Fifth Sensor")
dist_sensor_E.grid(column=1,row=5)
data1_E = random.randint(1,10)
data1_E_text = Label(window,text = data1_D)
data1_E_text.grid(column=2,row=5)

dist_sensor2_E = Label(window,text="Fifth Sensor")
dist_sensor2_E.grid(column=3,row=5)
data2_E = random.randint(1,10)
data2_E_text = Label(window,text=data2_E)
data2_E_text.grid(column=4,row=5)


def click():
  distance1, distance2 = dist_sensors(data1_A,data1_B,data1_C,data1_D,data1_E,data2_A,data2_B,data2_C,data2_D,data2_E)

  data1_A_replace = random.randint(1,10)
  data1_A_text.configure(text = data1_A_replace)
  data1_B_replce = random.randint(1,10)
  data1_B_text.configure(text = data1_B_replce)
  data1_C_replace = random.randint(1,10)
  data1_C_text.configure(text = data1_C_replace)
  data1_D_replace = random.randint(1,10)
  data1_D_text.configure(text = data1_D_replace)
  data1_E_replace = random.randint(1,10)
  data1_E_text.configure(text = data1_E_replace)

  data2_A_replace = random.randint(1,10)
  data2_A_text.configure(text = data2_A_replace)
  data2_B_replce = random.randint(1,10)
  data2_B_text.configure(text = data2_B_replce)
  data2_C_replace = random.randint(1,10)
  data2_C_text.configure(text = data2_C_replace)
  data2_D_replace = random.randint(1,10)
  data2_D_text.configure(text = data2_D_replace)
  data2_E_replace = random.randint(1,10)
  data2_E_text.configure(text = data2_E_replace)


  sensors(distance1,distance2)
submit = Button(window,text="Enter",command=click)
submit.grid(column=2, row=6)


window.mainloop()