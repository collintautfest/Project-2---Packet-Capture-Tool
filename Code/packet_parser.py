#!/bin/python3
def parse(filename):
    print('called parse function in packet_parser.py')
    fi = open("Data_File.txt", 'w')

    with open(filename, 'r') as file:
        for line in file:
            if '192' in line:
                fields = line.split()
                if len(fields) >= 2:
                    # time
                    fi.write(fields[1])
                    # source
                    fi.write("\t" + fields[2] + "\t")
                    # Destination
                    fi.write("\t" + fields[3] + "\t")
                    # Protocol
                    fi.write("\t" + fields[4] + "\t")
                    # Length
                    fi.write("\t" + fields[5] + "\t")
                    # Info
                    if 'Destination' in line:
                        fi.write("\t" + fields[6] + " " + fields[7] + " " + fields[8] + " " + fields[9] + "\t" + "\n")
                    else:
                        fi.write("\t" + fields[6] + " " + fields[7] + " " + fields[8] + "\t" + "\n")

