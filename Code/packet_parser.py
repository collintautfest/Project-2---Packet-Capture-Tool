#!/bin/python3
#takes in arg 1 then writes to Data_File.txt
import sys

fi = open("Data_File.txt", 'w')

def parse(filename):
    print('called parse function in packet_parser.py')
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

def main():
    filename = sys.argv[1]
    parse(filename)

if __name__ == "__main__":
    main()
