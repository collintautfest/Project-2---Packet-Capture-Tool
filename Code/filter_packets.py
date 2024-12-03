#!/bin/python3
def filter(file_name):
    """
    Extracts packets containing the ICMP protocol from a text file and returns it as a filtered text file
    """
    input_filename = file_name
    try:
        # Generate the output filename manually
        if '.' in input_filename:
            base, ext = input_filename.rsplit('.', 1)
            output_filename = f"{base}_filtered.{ext}"
        else:
            output_filename = f"{input_filename}_filtered"

        with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
            buffer = []  # Buffer to store packet lines
            write_packet = False  # Flag to determine if the packet is ICMP
            
            for line in infile:
                if "No." in line:  # Start of a new packet
                # Write previous packet if it contained ICMP
                    if write_packet and buffer:
                        outfile.write("".join(buffer))
                        
                    # Reset for the new packet
                    buffer = [line]
                    write_packet = False  # Reset flag
                else:
                    buffer.append(line)
                    if "ICMP" in line:  # Detect ICMP in the packet
                        write_packet = True

            # edge case for last packet as ICMP
            if write_packet and buffer:
                outfile.write("".join(buffer))

        print(f"ICMP packets extracted successfully to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
filter('Node1.txt')
