from traffic import *
# Defining sensors that measure the distance of the closest object. Sensors are on footpath facing the road.

def dist_sensors(dist1_A, dist1_B, dist1_C, dist1_D, dist1_E, dist2_A ,dist2_B, dist2_C,dist2_D, dist2_E,):
    road_traffic_length1 = 0
    road_traffic_length2 = 0
    # The road width is assumed and is taken before the program starts.
    road_width_1 = 5
    road_width_2 = 6

    #If the distance detected by the sensors is less then that of the road width, then sensors assume that there is a car on the road and adds to length of traffic.
    if dist1_A <= road_width_1:
        road_traffic_length1 = 10

    if dist1_B <= road_width_1:
        road_traffic_length1 = 20

    if dist1_C <= road_width_1:
        road_traffic_length1 = 30

    if dist1_D <= road_width_1:
        road_traffic_length1 = 40

    if dist1_E <= road_width_1:
        road_traffic_length1 = 50

    if dist2_A <= road_width_2:
        road_traffic_length2 = 10

    if dist2_B <= road_width_2:
        road_traffic_length2 = 20

    if dist2_C <= road_width_2:
        road_traffic_length2 = 30

    if dist2_D <= road_width_2:
        road_traffic_length2 = 40

    if dist2_E <= road_width_2:
        road_traffic_length2 = 50

    return road_traffic_length1, road_traffic_length2

 
# This part of the program records the frequency and loudness of the sounds using sound sensors. These values are compared with the other road and the ambulance to decide which road gets the light.
def sound_sensor(frequency1, frequency2, volume1, volume2, traffic_road1,traffic_road2):
    print("The length of traffic in road 1 is", traffic_road1,"metres")
    print("The length of traffic in road 2 is", traffic_road2,"metres")
    
    
    if frequency1>=850 and frequency1<=950:
        print("Ambulance incoming on road 1!")
        green()
        print("For Road 1")
        red()
        print("For Road 2")
        timer(20)
        yellow()
        traffic_road1 = traffic_road1 - 40
        if traffic_road1<0:
              traffic_road1=0
        print("The length of traffic on road 1 is", traffic_road1,"metres")
        print("The length of traffic on road 2 is", traffic_road2,"metres")
        signals(traffic_road1, traffic_road2)
    elif frequency2>=850 and frequency2<=950:
        print("Ambulance Incoming in road 2!")
        green()
        print("For Road 2")
        red()
        print("For Road 1")
        timer(20)
        yellow()
        traffic_road2 = traffic_road2 - 40
        if traffic_road1<0:
          raffic_road1=0
        print("The length of traffic on road 1 is",traffic_road1,"metres")
        print("The length of traffic on road 2 is", traffic_road2,"metres")
        signals(traffic_road1, traffic_road2)

    elif frequency1 >=850 and frequency1<=950 and frequency2>=850 and frequency2<=950:
      # If there are 2 ambulances on both roads, the louder siren turns green
        print(traffic_road1,traffic_road2)
        if volume1 >= volume2:
            print("Ambulance Incoming on road 1!")
            green()
            print("For Road 1")
            red()
            print("For Road 2")
            timer(20)
            yellow()
            traffic_road1 = traffic_road1 - 40
            if traffic_road1<0:
              traffic_road1=0
            print("The length of traffic on road 1 is", traffic_road1,"metres")
            print("The length of traffic on road 2 is", traffic_road2,"metres")
            signals(traffic_road1, traffic_road2)
            
        elif volume1 < volume2:
            print("Ambulance incoming on road 2!")
            green()
            print("For Road 2")
            red()
            print("For Road 1")
            timer(20)
            yellow()
            traffic_road2 = traffic_road1 - 40
            if traffic_road2<0:
              traffic_road1=0
            print("The length of traffic on road 1 is", traffic_road1,"metres")
            print("The length of traffic on road 2 is", traffic_road2,"metres")
            signals(traffic_road1, traffic_road2)
        else:
            pass
    else:
        signals(traffic_road1, traffic_road2)