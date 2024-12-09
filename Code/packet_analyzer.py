#!/bin/python3

from filter_packets import *
from packet_parser import *
from compute_metrics import *
import os
import csv

def main():
    '''
    filter all four nodes, parse through each filtered node, 
    compute metrics based on returned parsed data
    '''

    # delete to prevent overlap

    for item in range(1,5):
        if os.path.exists(f"Node{item}_filtered.txt"):
            os.remove(f"Node{item}_filtered.txt")
            print(f"cleared Node{item}")
    # if old csv exists clear it
    if os.path.exists("output.csv"):
        os.remove("output.csv")
        print("")
        print("cleared output")
    
    filtered_list = [] # list of filtered packets
    
    # filter nodes
    for i in range(1,5):
        filter(f"Node{i}.txt")
        filtered_list.append(f"Node{i}_filtered.txt")
    
    # call parser for each item of filtered_list
    if os.path.exists("Data_File.txt"):
        os.remove("Data_File.txt")
        print("cleared Data File")

    # print output to csv
    with open("output.csv", 'w', newline="") as outfile:
        for par in range(1,5):
            # get compute metrics and print
            writer = csv.writer(outfile, delimiter=',')
            parse(f"Node{par}_filtered.txt")
            c_list = []
            # inside call compute metrics for each parsed item
            c_list = compute(f"Node{par}_filtered.txt")
            # clear for reset
            os.remove("Data_File.txt")
            print(f"Cleared{par}")
            dat = [ 
                [f'Node {par}'],
                [],
                ['Echo Requests Sent', 'Echo Requests Recieved', 'Echo Replies Sent', 'Echo Replies Recieved'],
                [f'{c_list[0]}',f'{c_list[1]}',f'{c_list[2]}',f'{c_list[3]}'],
                ['Echo Requests Sent (bytes)', 'Echo Requests Data Sent (bytes)'],
                [f'{c_list[4]}',f'{c_list[5]}'],
                ['Echo Requests Recieved (bytes)', 'Echo Requests Data Recieved'],
                [f'{c_list[6]}',f'{c_list[7]}'],
                ['Average RTT', f'{c_list[8]}'],
                ['Echo Request Throughput (kB/sec)',f'{c_list[9]}'],
                ['Echo Request Goodput (kB/sec)', f'{c_list[10]}'],
                ['Average Reply Delay (us)', ''],
                ['Average Echo Request Hop Count',f'{c_list[11]}'],
                []
            ]
            writer.writerows(dat)

    print ("Complete!")

main()
