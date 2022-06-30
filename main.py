## HAKAN KARADENİZ   ##
##   30 JUNE 2022    ##
## THERE IS A CODE WHICH USED FOR ULTRA WIDE BAND INDOOR LOCALIZATION ##

from cmath import sqrt
import math
from matplotlib import pyplot as plt

print("Please Enter Your Actual Distance between the TAGs for Calculation (meter)")
c = input()
i = 0 # i value will use in the While Loops
j = 0 # j value will use in the While Loops
k = 0 # k value will use in the While Loops
l = 0 # l value will use in the While Loops

file = open("filename.txt","r")

#Device Lists are here !
deviceList1 = []
deviceList2 = []

#Calculation Lists are here !
calculationListX = []
calculationListY = []
calculationListD = []

#Coordinate List are here !

#Reading data file line by line .
file.readline()

while True:
    str = file.readline()
    arr = str.split(":")    #Split the data like an array .
    if not str:
        break
    
    if arr[2] == "RR2": #If we have RR2 in the line, Use this line !
        if arr[3] == "ce32143a":
            deviceList1.append(arr[5])
            deviceList1[len(deviceList1)-1] = deviceList1[len(deviceList1)-1][0:len(deviceList1[len(deviceList1)-1])-1]
        if arr[3] == "8e320fab":
            deviceList2.append(arr[5])
            deviceList2[len(deviceList2)-1] = deviceList2[len(deviceList2)-1][0:len(deviceList2[len(deviceList2)-1])-1]
                    #We can add and drop any device if we know the device ID !

#The Device Lists can be seen like this .
print(deviceList1[0:10])
print(deviceList2[0:10])


print(" ")
print("CALCULATIONS")

#Calculation of Y coordinate / Change your i value for calculations
while True:   
    if not i== 1000:
        asqr = float(deviceList1[i])* float(deviceList1[i])
        bsqr = float(deviceList2[i])* float(deviceList2[i])
        csqr = (float (c) * float (c))
        ust1 = float(asqr) - float (bsqr)
        ust2 = ust1 - float(csqr)
        alt = float (c) * -2
        valueOfY = ust2 / alt
      #  valueOfY = (float(asqr) - float(bsqr) - float (csqr)) / (-2*float (c))
        calculationListY.append(round(valueOfY,4))       
        i = i+1
    else:
        print("calculationListY")
        print(calculationListY)
        break

#Calculation of X coordinate / Change your j value for calculations
while True:
    if not j == 1000:
        a = float (deviceList2[j])*float (deviceList2[j])
        Ysqr = float(calculationListY[j])* float(calculationListY[j])
        valueOfX = math.sqrt(abs(a-Ysqr))
        calculationListX.append(valueOfX)       
        j = j+1
    else:
        print("calculationListX")
        print(calculationListX)
        break

while True:   
    if not k==1000:
      coordinateY = (float (c))- (calculationListY[k])
      calculationListD.append(coordinateY)
      k = k + 1
    else:
      print("calculationList D ")
      print(calculationListD)
      break

#Calculation of coordinates
%matplotlib inline


plt.plot((calculationListX),(calculationListD), 'ro')

plt.xlim(-5,10)
plt.ylim(-5,10)

plt.xlabel("X")
plt.ylabel("Y")

plt.show()