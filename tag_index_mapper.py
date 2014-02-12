#! /usr/bin/env python

import sys # Used for stdin and stdout
import csv # Used for parsing input and output lines

def mapper():
    # The csv reader to input tab delimited lines
    reader = csv.reader(sys.stdin, delimiter='\t')
    # The csv writer to output tab delimited lines
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    
    # This is list of the search tags
    search_tags = ['cs101']
    
    # Iterate over each line from the input
    for line in reader:
        # Implement an error handler in case anything goes wrong
        try:
            node_id   = line[0]            # The node ID is the 1st token
            tag_names = line[2].split(' ') # The tag names are space seperated tokens in the 3rd field
            
            # Iterate through all the tag names in the 2nd field and output each one
            # The output is: key = tag_name, value = node_id
            for tag_name in tag_names:
                # If the tag_name is in search tags then send it to the reducer
                if tag_name in search_tags:
                    output = [tag_name, node_id]
                    writer.writerow(output)
            
        # Catch all errors in one statement.  Just continue on to the next line.
        except:
            continue

def main():
    mapper()
    
if __name__ == '__main__':
    main()