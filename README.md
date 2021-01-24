# Smart Signal

## The software works in 2 ways:

### Traffic control
By using complex algorithms, the program detects traffic on 2 roads and decides which road should go first.
A distance sensor is plcaed on the traffic signal. This sensor has a range of about 1 Km. We have data points that are marked every 10 metres on each road which are in line with the sensor and send radio signals.
Every 20 seconds, the program compares the amount of traffic on each road and will continue to do so.

As we are unable to work with hardware, we have created a GUI system that gives us random values as the traffic.

### Emergency vehicle detection
Using sound sensors, we detect sounds of high frequency and loudness, similar to that of emergency service vehicles. The program, on detection of the siren, will automatically give the green light to the respective road. We believe this could save thousands of lives.