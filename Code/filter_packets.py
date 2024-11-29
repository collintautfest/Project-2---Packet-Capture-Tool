#!/bin/python3
def filter(file_name):
    try:
        filename = file_name
        
        base, ext = filename.rsplit('.', 1)
        output_file = f"{base}_filtered.{ext}"

        with open(filename, 'r') as file, open(output_file, 'w') as outfile:
            write_packet = False # determine if start writing lines
            Buffer = [] # buffer to store packets
            for line in file:
                if "No." in line and "ICMP" in line:
                    # start writing
                    if buffer:
                        outfile.write("".join(buffer)) # write previous
                        buffer = [] # reset

                    write_packet = True
                    buffer.append(line)
                elif "No." in line:
                    # end previous packet if not icmp
                    if buffer and write_packet:
                        outfile.write("".join(buffer))
                        buffer = []

                    write_packet = False # reset for non icmp packets

                elif write_packet:
                    buffer.append(line)

            # edge case for last being icmp
            if buffer and write_packet:
                outfile.write("".join(buffer))

        # Output
    except:
        print(f"Error: The file '{file_name}' does not exist.")


filter('Node1.txt')	
