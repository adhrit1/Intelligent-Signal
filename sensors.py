# The road width is assumed and is taken before the program starts
road_width_1 = 5
road_width_2 = 6

# Defining sensors that measure the distance of the closest object. Sensors are on footpath


def dist_sensors(dist1_A, dist1_B, dist1_C, dist1_D, dist1_E,  dist2_A, dist2_B, dist2_C, dist2_D, dist2_E,):
    road_traffic_length1 = 0
    road_traffic_length2 = 0

  # if the distance detected by the sensors is less then that of the road width. The sensors assume that there is a car on the road and adds to lenght of traffic
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


# incomplete , need to connect to main sensor reading
# defining sound sensors which detect sounds of certain frequencies and loudness that would be detected as an ambulance and would turn the road associated green.
def sound_sensor(ambulance_frequency, volume1, volume2):
    sound_road1 = int(input("Frequency reading for road 1: "))
    sound_road2 = int(input("Frequency reading for road 2: "))

    if ambulance_frequency == sound_road1 and volume1 > volume2:
      print("Signal Green For Road 1")
      print("Signal Red For road 2")

    elif ambulance_frequency == sound_road2 and volume2 > volume1:
      print("Signal Green For Road 2")
      print("Signal Red For road 1")

    elif ambulance_frequency == sound_road1 and ambulance_frequency == sound_road2:
      if volume1 > volume2:
       print("Signal Green For Road 1")
       print("Signal Red For road 2")
      else:
        print("Signal Green For Road 2")
        print("Signal Red For Road 1")