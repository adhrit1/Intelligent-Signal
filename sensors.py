from traffic import red, green

def sound_sensor(freqeuncy_road1,frequency_road2,volume1,volume2,):
  ambulance_frequency = 900

  if ambulance_frequency>freqeuncy_road1 and volume1>volume2:
    green()
    print("For road 1")
    red()
    print("For road 2")
  elif ambulance_frequency>frequency_road2 and volume2>volume1:
    red()
    print("For road 1")
    green()
    print("For road 2")
  elif ambulance_frequency == freqeuncy_road1 and ambulance_frequency==frequency_road2:
    if volume1>volume1:
      green()
      print("For road 1")
      red()
      print("For road 2") 
    elif volume1>volume1:
      green()
      print("For road 1")
      red()
      print("For road 2")

    
  
road_width1=int(input("Enter the width of road 1 in metres:"))
road_width2=int(input("Enter the width of road 2 in metres:"))

def distance_sensor(Distance1_A, Distance1_B,Distance1_C, Distance1_D, Distance1_E, Distance2_A,Distance2_B,Distance2_C,Distance2_D,Distance2_E):
  road_traffic_lenght1 = 0
  road_traffic_lenght1 = 0
  if Distance1_A < road_width1:
    road_traffic_lenght1 = 10
  if Distance1_B < road_width1:
    road_traffic_lenght1 = 20
  if Distance1_C < road_width1:
    road_traffic_lenght1 = 30
  if Distance1_D < road_width1:
    road_traffic_lenght = 40
  if Distance1_E < road_width1:
    road_traffic_lenght1 = 50
  if Distance2_A < road_width2:
    road_traffic_lenght2 = 10
  if Distance2_B < road_width2:
    road_traffic_lenght2 = 20
  if Distance2_C < road_width2:
    road_traffic_lenght2 = 30
  if Distance2_D < road_width2:
    road_traffic_lenght2 = 40
  if Distance2_E < road_width2:
    road_traffic_lenght2 = 50
  
  