#!/bin/python3
def filter(file_name):
    try:
        filename = file_name
        
        base, ext = filename.rsplit('.', 1)
        output_file = f"{base}_filtered.{ext}"

        with open(filename, 'r') as file, open(output_file, 'w') as outfile:
            for line in file:
                # search for lines containing the icmp echo request or reply marker
                split_line = line.strip().split()

                if split_line[] == "ICMP"
                # send to filtered file


        # Output
    except:
        print(f"Error: The file '{file_name}' does not exist.")


filter()	
