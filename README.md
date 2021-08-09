# Health-And-Safety-Dashboard
This code present in this repository acts as the **frontend** and **webserver** for the project **IoT BasedHealth and Safety For Construction Workers**. 

# Overview
***IoT Based Health and Safety for Construction workers*** is comprised of two parts: **Sensor Nodes** and **WebServer**.

## Sensor Nodes
The workers will be required to wear sensor nodes that exist in the form of helmets, which will be used to monitor the vitals of the workers (Temparature and Pulse) and to detetect falls. Since the **accelerometer** is responsible for detecting falls, the chances of false positives is high. This is because the acceleration a fall is \(g=9.8m/s^2\) regardless of the height of the platform the worker was standing on. We hence use a barometer to calculate the height of the platform above round level, after which we calculate the expected duration of fall using kinematics.

Let the height of the platform be \(H\), acceleration due to gravity be \(g=9.8m/s^2\) and the expected duration of fall be \(t\). We can assume the initial velocity to be \(u=0\). 

For equations of motion, we get
\[
	H = ut + \frac{1}{2}gt^2
\]
Since \(u=0\), we can rewrite the above expression as
\[
	t = \sqrt{\frac{2H}{g}}	
\]

We can hence conclude that a fall has occurred if the duration of fall detected using the accelerometer (say \(t_{obs}\)) is greater than the expression of expected duration of fall (say \(t_{exp}\)) obtained above after correcting for margin of error (say \(E\)), i.e.,
\[t_{obs}>t_{expected} \pm E\]


All the data is sent to both **ThingSpeak** and a local **Django WebServer**. 

## WebServer
***Note*: This is not the same as ESP8266 Web Server.**

The Django WebServer is used to send recieve, process and store the data recieved from the sensor nodes, and to display it on any device present on the same network as the webserver. 

The webserver is explained in more detail in the upcoming sections of this README.

# Features
# Gallery
# Building