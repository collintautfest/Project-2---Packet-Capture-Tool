import os
import sys
import argparse

timeArrRequest = []
timeArrReply = []
through = []

with open('/Users/ethanmenand/Downloads/Captures/Node1.txt') as file:
    for line in file:
        l = line.split()
        if len(l)>5:
            if len(l)>7 and l[7]!='unreachable': 
                if(l[4]=='ICMP'):
                    #print(l)
                    if l[8]=="request":
                        timeArrRequest.append(float(l[1]))
                        through.append(float(l[5]))
                    elif l[8]=="reply":
                        timeArrReply.append(float(l[1]))
            

avg = 0
throughAvg = 0
adjusted=0
greg = 0
c4=0
counter = 0
for i in range(len(timeArrReply)):
    temp1 = timeArrReply[i]-timeArrRequest[i]
    temp2 = round(temp1*1000,2)
    
    print(temp2)
    #print(temp1)
    if temp2>0.08:
        throughAvg+=through[i]
        adjusted+=(through[i]-42)
        avg+=temp1
        counter+=1
        
    else:
        greg+=temp2
        c4+=1
    
        

print(avg)
rtt = avg/counter
print(rtt)
print(counter)
print((throughAvg/avg))
print((adjusted/avg))
#target is 55.51

print(greg)
print(c4)
print(round((greg/c4)*1000,2))



