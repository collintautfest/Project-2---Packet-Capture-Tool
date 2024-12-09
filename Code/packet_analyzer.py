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

    
    filtered_list = [] # list of filtered packets
    
    # filter nodes
    for i in range(1,5):
        filter(f"Node{i}.txt")
        filtered_list.append(f"Node{i}_filtered.txt")
    
    # call parser for each item of filtered_list
    if os.path.exists("Data_File.txt"):
        os.remove("Data_File.txt")
        print("cleared Data File")

    for par in range(1,5):
        parse(f"Node{par}_filtered.txt")

        # inside call compute metrics for each parsed item

        # clear for reset
        os.remove("Data_File.txt")
        print(f"Cleared{par}")


    # if old csv exists clear it
    if os.path.exists("output.csv"):
        os.remove("output.csv")
        print("")
        print("cleared output")
    # print output to csv
    '''
    with open("output.csv", 'w') as outfile:
        # get compute metrics and print
        writer = csv.writer(outfile)

    '''
    print ("Complete!")

main()
