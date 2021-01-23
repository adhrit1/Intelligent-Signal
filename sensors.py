#The road width is assumed and is taken before the program starts

road_width_1=5
road_width_2=6

traffic_1=0
traffic_2=0
def dist_sensors(dist1_A, dist1_B, dist1_C, dist1_D, dist1_E,  dist2_A, dist2_B, dist2_C, dist2_D, dist2_E,):
  road_traffic_length1=0 
  road_traffic_length2=0 
  
  
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

  road1 = 0
  road2 = 1

  if road1==0 and road2==1:
    algo_num = road_width_2/road_width_1
    algo_num = algo_num*100
    road_value_1 = road_traffic_length1*road_width_1
    #time

  elif road1==1 and road2==0:
    algo_num = road_width_1/road_width_2
    algo_num = algo_num*100
    road_value_2 = road_traffic_length2*algo_num

  return road_traffic_length1,road_traffic_length2

#subjcet to change- for testing
        

def sound_sensor(ambulance_frequency,volume1,volume2):  
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
