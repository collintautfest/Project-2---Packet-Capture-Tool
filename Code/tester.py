import os
import sys

timeArrRequest = []
timeArrReply = []
hopCount =[]
rep=0
c1=0
throughReqSent = []
c2=0
throughRepSent = []
c3=0
throughReqSent2 = []
c4=0
throughRepSent2 = []

src=""

with open('/Users/ethanmenand/Downloads/Code 2/Project-2---Packet-Capture-Tool/Code/Node1_filtered.txt') as file:
    next(file)
    for line in file:
        l = line.split()
        
        if len(l)>5:
            if src=="":
                src=l[3]
                print(src)
            if len(l)>7 and l[7]!='unreachable': 
                if(l[4]=='ICMP'):
                    
                    
                    if l[8]=="request" and l[2]==src:
                        timeArrRequest.append(float(l[1]))
                        throughReqSent.append(float(l[5]))
                        c1+=1
                    elif l[8]=="reply" and l[2]==src:
                        timeArrReply.append(float(l[1]))
                        hopCount.append(128-int(l[11][4:])+1)
                        throughRepSent.append(float(l[5]))
                        print(l[5])
                        c2+=1
                    elif l[8]=="request" and l[3]==src:
                        timeArrRequest.append(float(l[1]))
                        throughReqSent2.append(float(l[5]))
                        
                        c3+=1
                    elif l[8]=="reply" and l[3]==src:
                        timeArrReply.append(float(l[1]))
                        hopCount.append(128-int(l[11][4:])+1)
                        throughRepSent2.append(float(l[5]))
                        c4+=1
                        
                
print(c1)
print(c2)
print(c3)
print(c4)



avg = 0
throughAvg = 0
adjusted=0
throughAvg2 = 0
adjusted2=0
greg = 0
echoRequests = 0
exraCount=0
hops=0

count1=0
for i in range(len(timeArrReply)):
    temp1 = timeArrReply[i]-timeArrRequest[i]
    temp2 = round(temp1*1000,2)
    
    exraCount+=1
    if temp2>0.08:
        count1+=1
        avg+=temp2
        echoRequests+=1
        hops+=hopCount[i]
    else:
        greg+=temp2
        exraCount+=1
        
for i in range(len(throughReqSent)):
    throughAvg+=throughReqSent[i]
    adjusted+=(throughReqSent[i]-42)

for i in range(len(throughRepSent)):
    throughAvg2+=throughRepSent[i]
    adjusted2+=(throughRepSent[i]-42)



print(throughAvg)
print(adjusted)
print(throughAvg2)
print(adjusted2)

print(avg)
rtt = avg/count1
print(rtt)

throughput=(throughAvg/avg/1000)
goodput=(adjusted/avg/1000)

#target is 55.51
delay=(greg/c2)*1000
print(delay)

#print(round((greg/c4)*1000,2))

hopAVG=hops/count1
print(hopAVG)
vars = [c1,c2,c3,c4,throughAvg,adjusted,throughAvg2,adjusted2,rtt,throughput,goodput,hopAVG]


