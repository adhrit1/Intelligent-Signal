import time
import random
from tkinter import *
from traffic import signals, green
#Gets functions "signals" and "green" from traffic.py
from sensors import dist_sensors, sound_sensor
#Gets functions "dist_sensors" and "sound_sensor" from sensors.py

#Provides the window for the GUI
window = Tk()
window.title("Intelligent Signal")
window.geometry('450x200')

road1 = Label(window, text="Road 1")
road1.grid(column=1, row=0)

road2 = Label(window, text="Road 2")
road2.grid(column=3, row=0)

dist_sensor_A = Label(window, text="First Point(m)")
dist_sensor_A.grid(column=1, row=1)
# Gets a random value
data1_A = random.randint(1, 10)
data1_A_text = Label(window, text=data1_A)
data1_A_text.grid(column=2, row=1)

dist_sensor2_A = Label(window, text="First Point(m)")
dist_sensor2_A.grid(column=3, row=1)
# Gets a random value
data2_A = random.randint(1, 10)
data2_A_text = Label(window, text=data2_A)
data2_A_text.grid(column=4, row=1)

dist_sensor_B = Label(window, text="Second Point(m)")
dist_sensor_B.grid(column=1, row=2)
# Gets a random value
data1_B = random.randint(1, 10)
data1_B_text = Label(window, text=data1_B)
data1_B_text.grid(column=2, row=2)

dist_sensor2_B = Label(window, text="Second Point(m)")
dist_sensor2_B.grid(column=3, row=2)
# Gets a random value
data2_B = random.randint(1, 10)
data2_B_text = Label(window, text=data2_B)
data2_B_text.grid(column=4, row=2)

dist_sensor_C = Label(window, text="Third Point(m)")
dist_sensor_C.grid(column=1, row=3)
# Gets a random value
data1_C = random.randint(1, 10)
data1_C_text = Label(window, text=data1_C)
data1_C_text.grid(column=2, row=3)

dist_sensor2_C = Label(window, text="Third Point(m)")
dist_sensor2_C.grid(column=3, row=3)
# Gets a random value
data2_C = random.randint(1, 10)
data2_C_text = Label(window, text=data2_C)
data2_C_text.grid(column=4, row=3)

dist_sensor_D = Label(window, text="Fourth Point(m)")
dist_sensor_D.grid(column=1, row=4)
# Gets a random value
data1_D = random.randint(1, 10)
data1_D_text = Label(window, text=data1_D)
data1_D_text.grid(column=2, row=4)

dist_sensor2_D = Label(window, text="Fourth Point(m)")
dist_sensor2_D.grid(column=3, row=4)
# Gets a random value
data2_D = random.randint(1, 10)
data2_D_text = Label(window, text=data2_D)
data2_D_text.grid(column=4, row=4)

dist_sensor_E = Label(window, text="Fifth Point(m)")
dist_sensor_E.grid(column=1, row=5)
# Gets a random value
data1_E = random.randint(1, 10)
data1_E_text = Label(window, text=data1_E)
data1_E_text.grid(column=2, row=5)

dist_sensor2_E = Label(window, text="Fifth Point(m)")
dist_sensor2_E.grid(column=3, row=5)
# Gets a random value
data2_E = random.randint(1, 10)
data2_E_text = Label(window, text=data2_E)
data2_E_text.grid(column=4, row=5)

sound_sensor1 = Label(window, text="Frequency Sensor(Hz)")
sound_sensor1.grid(column=1, row=7)
# Gets a random value
sound_sensor1_value = random.randint(600, 1000)
sound_sensor1_text = Label(window, text=sound_sensor1_value)
sound_sensor1_text.grid(column=2, row=7)

sound_sensor2 = Label(window, text="Frequency Sensor(Hz)")
sound_sensor2.grid(column=3, row=7)
# Gets a random value
sound_sensor2_value = random.randint(600, 1000)
sound_sensor2_text = Label(window, text=sound_sensor2_value)
sound_sensor2_text.grid(column=4, row=7)

volume_sensor1 = Label(window, text="Loudness Sensor(Db)")
volume_sensor1.grid(column=1, row=8)
# Gets a random value
volume_sensor1_value = random.randint(80, 140)
volume_sensor1_text = Label(window, text=volume_sensor1_value)
volume_sensor1_text.grid(column=2, row=8)

volume_sensor2 = Label(window, text="Loudness Sensor(Db)")
volume_sensor2.grid(column=3, row=8)
# Gets a random value
volume_sensor2_value = random.randint(80, 140)
volume_sensor2_text = Label(window, text=volume_sensor2_value)
volume_sensor2_text.grid(column=4, row=8)




def click():
    # Calling Distance Sensor
    distance1, distance2 = dist_sensors(data1_A, data1_B, data1_C, data1_D,data1_E, data2_A, data2_B, data2_C,data2_D, data2_E)

    # Calling Sound Sensor
    sound_sensor(sound_sensor1_value, sound_sensor2_value,volume_sensor1_value, volume_sensor2_value, distance1,distance2)


    data1_A_replace = random.randint(1, 10)
    # Automatic Change in values
    data1_A_text.configure(text=data1_A_replace)

    data1_B_replace = random.randint(1, 10)
    # Automatic Change in values
    data1_B_text.configure(text=data1_B_replace)

    data1_C_replace = random.randint(1, 10)
    # Automatic Change in values
    data1_C_text.configure(text=data1_C_replace)

    data1_D_replace = random.randint(1, 10)
    # Automatic Change in values
    data1_D_text.configure(text=data1_D_replace)

    data1_E_replace = random.randint(1, 10)
    # Automatic Change in values
    data1_E_text.configure(text=data1_E_replace)

    data2_A_replace = random.randint(1, 10)
    data2_A_text.configure(text=data2_A_replace)

    data2_B_replace = random.randint(1, 10)
    # Automatic Change in values
    data2_B_text.configure(text=data2_B_replace)

    data2_C_replace = random.randint(1, 10)
    # Automatic Change in values
    data2_C_text.configure(text=data2_C_replace)

    data2_D_replace = random.randint(1, 10)
    # Automatic Change in values
    data2_D_text.configure(text=data2_D_replace)

    data2_E_replace = random.randint(1, 10)
    # Automatic Change in values
    data2_E_text.configure(text=data2_E_replace)

    sound1_sensor = random.randint(600, 1000)
    # Automatic Change in values
    sound_sensor1_text.configure(text=sound1_sensor)

    sound2_sensor = random.randint(600, 1000)
    # Automatic Change in values
    sound_sensor2_text.configure(text=sound2_sensor)

    volume1_replace = random.randint(80, 140)
    # Automatic Change in values
    volume_sensor1_text.configure(text=volume1_replace)

    volume2_replace = random.randint(80, 140)
    # Automatic Change in values
    volume_sensor2_text.configure(text=volume1_replace)

    def check():
      distance1, distance2 = dist_sensors(data1_A_replace,data1_B_replace, data1_C_replace, data1_D_replace,data1_E_replace, data2_A_replace, data2_B_replace, data1_C_replace,data1_D_replace, data1_E_replace)

      sound_sensor(sound1_sensor, sound2_sensor,volume1_replace, volume2_replace, distance1,distance2)
      #Button thats calls function "click"
    submit2 = submit = Button(window, text="Press Me Again", command=check)
    submit2.grid(column=2, row=0)
#Button thats calls function "click"
submit = Button(window, text="Press Me", command=click)
submit.grid(column=2, row=0)

window.mainloop()
