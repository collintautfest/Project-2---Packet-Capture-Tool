import os
import sys
import argparse

timeArrRequest = []
timeArrReply = []
through = []
hopCount =[]
timeReq = []
timeRep =[]
src=[]
dst=[]
with open('/Users/ethanmenand/Downloads/Captures/Node1.txt') as file:
    for line in file:
        l = line.split()
        if len(l)>5:
            if len(l)>7 and l[7]!='unreachable': 
                if(l[4]=='ICMP'):
                    #print(l)
                    
                    src.append(l[2])
                    dst.append(l[3])
                    if l[8]=="request":
                        timeArrRequest.append(float(l[1]))
                        through.append(float(l[5]))
                        timeReq.append(float(l[1]))
                    elif l[8]=="reply":
                        timeArrReply.append(float(l[1]))
                        hopCount.append(128-int(l[11][4:])+1)
                        timeRep.append(float(l[1]))


timeArrRequest2 = []
timeArrReply2 = []
through2 = []
hopCount2 =[]
timeReq2 = []
timeRep2 =[]
src2=[]
dst2=[]
with open('/Users/ethanmenand/Downloads/Captures/Node2.txt') as file:
    for line in file:
        l = line.split()
        if len(l)>5:
            if len(l)>7 and l[7]!='unreachable': 
                if(l[4]=='ICMP'):
                    #print(l)
                    
                    src2.append(l[2])
                    dst2.append(l[3])
                    if l[8]=="request":
                        timeArrRequest2.append(float(l[1]))
                        through2.append(float(l[5]))
                        timeReq2.append(float(l[1]))
                        timeRep2.append(float(l[1]))
                    elif l[8]=="reply":
                        timeArrReply2.append(float(l[1]))
                        hopCount2.append(128-int(l[11][4:])+1)

timeArrRequest3 = []
timeArrReply3 = []
through3 = []
hopCount3 =[]
timeReq3 = []
timeRep3 =[]
src3=[]
dst3=[]
with open('/Users/ethanmenand/Downloads/Captures/Node3.txt') as file:
    for line in file:
        l = line.split()
        if len(l)>5:
            if len(l)>7 and l[7]!='unreachable': 
                if(l[4]=='ICMP'):
                    #print(l)
                    
                    src3.append(l[2])
                    dst3.append(l[3])
                    if l[8]=="request":
                        timeArrRequest3.append(float(l[1]))
                        through3.append(float(l[5]))
                        timeReq3.append(float(l[1]))

                    elif l[8]=="reply":
                        timeArrReply3.append(float(l[1]))
                        hopCount3.append(128-int(l[11][4:])+1)
                        timeRep3.append(float(l[1]))

timeArrRequest4 = []
timeArrReply4 = []
through4 = []
hopCount4 =[]
timeReq4 = []
timeRep4=[]
src4=[]
dst4=[]
with open('/Users/ethanmenand/Downloads/Captures/Node4.txt') as file:
    for line in file:
        l = line.split()
        if len(l)>5:
            if len(l)>7 and l[7]!='unreachable': 
                if(l[4]=='ICMP'):
                    #print(l)
                    src4.append(l[2])
                    dst4.append(l[3])
                    if l[8]=="request":
                        timeArrRequest4.append(float(l[1]))
                        through4.append(float(l[5]))
                        timeReq4.append(float(l[1]))

                    elif l[8]=="reply":
                        timeArrReply4.append(float(l[1]))
                        hopCount4.append(128-int(l[11][4:])+1)
                        timeRep4.append(float(l[1]))

avg = 0
throughAvg = 0
adjusted=0
greg = 0
c4=0
counter = 0
temp3=0
exraCount=0

rahh=0
grahh=0
for i in range(len(timeArrReply)):
    temp1 = timeArrReply[i]-timeArrRequest[i]
    temp2 = round(temp1*1000,2)
    exraCount+=1
    #print(temp2)
    #print(temp1)
    ip1 = src[i]
    ip2 = dst[i]
    if temp2>0.08:
        throughAvg+=through[i]
        adjusted+=(through[i]-42)
        avg+=temp2
        counter+=1
        rahh+=hopCount[i]
    else:
        for x in range(len(timeRep2)):
            if timeRep[i]<timeRep2[x] and timeReq[i]>timeReq2[x]:
                if timeRep2[x]-timeReq2[x]<0.1:
                    if src2[x]==ip2 and dst2[x]==ip1:
                        greg+=timeRep2[x]-timeReq2[x]
                        c4+=1
       
print(temp3*-1/exraCount)


print(avg)
rtt = avg/counter
print(rtt)
print(counter)
print((throughAvg/avg/1000))
print((adjusted/avg/1000))
#target is 55.51

print(greg)
print(c4)
#print(round((greg/c4)*1000,2))

print(rahh/counter)



