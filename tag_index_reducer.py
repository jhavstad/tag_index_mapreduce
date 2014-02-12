#! /usr/bin/env python

import sys # Used for stdin and stdout
import csv # Used for parsing input and output lines

def reducer():
    # The csv reader to input tab delimited lines
    reader = csv.reader(sys.stdin, delimiter='\t')
    # The csv writer to output tab delimited lines
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    
    # This dictionary stores the index for the tags
    tag_index = dict()
    
    # Iterate over each line from the input
    for line in reader:
        # Implement an error handler in case anything goes wrong
        try:
            tag_name = line[0] # The tag name is the 1st token
            node_id  = line[1] # The node ID that references the tag is the 2nd token
            
            # If the tag name has not yet been index then add it
            if tag_name not in tag_index:
                tag_index[tag_name] = [0, list()]
                
            # Only store a node ID that references a tag once
            if node_id not in tag_index[tag_name][1]:
                tag_index[tag_name][1].append(node_id)
                
            # Increment the number of times the tag has been referenced by a node
            tag_index[tag_name][0] += 1
            
        # Catch all errors in one statement.  Just continue on to the next line.
        except:
            continue
        
    # Iterate over the tag index and output the list
    for tag in tag_index:
        output = [tag, tag_index[tag][0], tag_index[tag][1]]
        writer.writerow(output)

def main():
    reducer()
    
if __name__ == '__main__':
    main()