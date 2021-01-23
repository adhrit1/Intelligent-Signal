import time
import random
from tkinter import *
from traffic import signals
from sensors import dist_sensor,sound_sensor

window = Tk()
window.title("Traffic signals")
window.geometry('420x200')

road1 = Label(window,text="Road 1")
road1.grid(column=1,row=0)

road2 = Label(window,text="Road 2")
road2.grid(column=3,row=0)



dist_sensor1_A = Label(window,text = "First Sensor")
dist_sensor1_A.grid(coloumn = 1, row = 1)
data1_A = random.radint(1,10)
data1_A_text = Label(window,text= Data1_A)
data1_A_text.grid(coloumn = 2, row = 1)

dist_sensor2_A = Label(window,text = "First Sensor")
dist_sensor2_A.grid(coloumn = 3, row = 1)
data2_A = random.radint(1,10)
data2_A_text = Label(window,text= Data2_A)
data2_A_text.grid(coloumn = 4, row = 1)

dist_sensor1_B = Label(window,text = "Second Sensor")
dist_sensor1_B.grid(coloumn = 1, row = 2)
data1_B = random.radint(1,10)
data1_B_text = Label(window,text= Data1_B)
data1_B_text.grid(coloumn = 2, row = 2)

dist_sensor2_B = Label(window,text = "Second Sensor")
dist_sensor2_B.grid(coloumn = 3, row = 2)
data2_B = random.radint(1,10)
data2_B_text = Label(window,text= Data2_B)
data2_B_text.grid(coloumn = 4, row = 2)

dist_sensor1_C = Label(window,text = "Second Sensor")
dist_sensor1_C.grid(coloumn = 1, row = 3)
data1_C = random.radint(1,10)
data1_C_text = Label(window,text= Data1_C)
data1_C_text.grid(coloumn = 2, row = 3)

dist_sensor2_C = Label(window,text = "Second Sensor")
dist_sensor2_C.grid(coloumn = 3, row = 3)
data2_C = random.radint(1,10)
data2_C_text = Label(window,text= Data2_C)
data2_C_text.grid(coloumn = 4, row = 3)

dist_sensor1_D = Label(window,text = "Second Sensor")
dist_sensor1_D.grid(coloumn = 1, row = 4)
data1_D = random.radint(1,10)
data1_D_text = Label(window,text= Data1_D)
data1_D_text.grid(coloumn = 2, row = 4)

dist_sensor2_D = Label(window,text = "Second Sensor")
dist_sensor2_D.grid(coloumn = 3, row = 4)
data2_D = random.radint(1,10)
data2_D_text = Label(window,text= Data2_D)
data2_D_text.grid(coloumn = 4, row = 4)

ist_sensor1_E = Label(window,text = "Second Sensor")
dist_sensor1_E.grid(coloumn = 1, row = 5)
data1_E = random.radint(1,10)
data1_E_text = Label(window,text= Data1_E)
data1_E_text.grid(coloumn = 2, row = 5)

dist_sensor2_E = Label(window,text = "Second Sensor")
dist_sensor2_E.grid(coloumn = 3, row = 5)
data2_E = random.radint(1,10)
data2_E_text = Label(window,text= Data2_E)
data2_E_text.grid(coloumn = 4, row = 5)