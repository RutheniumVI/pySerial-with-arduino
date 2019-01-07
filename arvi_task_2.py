# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 22:22:46 2019

@author: veerash palanihamy
"""
import serial
import math
serialCon = serial.Serial("COM5")
while True:
    user_input = input("Type: \nget' to get current temperature \n'on' to turn on led \n'off' to turn off led \n'exit' to close program\n")
    if user_input=="on":
        serialCon.write(b"on")
    elif user_input=="off":
        serialCon.write(b"off")
    elif user_input=="exit":
        serialCon.close()
        break
    elif user_input=="get":
        serialCon.write(b"get")
        while True:
            if serialCon.in_waiting>0:
                data_in = float(serialCon.readline(serialCon.in_waiting).decode())
                #below is the math to convert thermistor anlog reading to a temperature
                try:
                    resistance = 10000/(1023/data_in - 1.0)
                    temperature = math.log(resistance/10000)/3950
                    temperature += 1.0/(298.15)
                    temperature = 1/temperature
                    temperature -=273.15
                    print(temperature)
                except:
                    print("Error in sensor reading")
                break
    else:
        continue