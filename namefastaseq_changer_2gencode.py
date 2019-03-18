# -*- coding: utf-8 -*-

import argparse

parser = argparse.ArgumentParser(prog='python3')

# input file parser
parser.add_argument("input_fasta", metavar="input.fasta", type= str,
                    help= "Fasta file to replace sequence names/description for a generate code, e.g. S001")

#output file parser
parser.add_argument("output_fasta", metavar="output.fasta", type= str,
                    help= "Output fasta file where the sequence description/name was changed to a generated code")

arguments = parser.parse_args()

#generate the code for the sequence description assume
def seq_number_gen(count):
    seq_number= str(count)
    while len(seq_number) < 3:
        seq_number = "0" + seq_number
    return seq_number

#change de sequence description/name to the generated code
def function(input_file,output_file):

    input = open(input_file, 'r') #open the input file

    output= open(output_file, 'w') #open the output file

    dictio={} #dicionary creation, description | code 

    count= 0 #count variable

    for line in file:

        if line.startswith('>'): #or line[0]=='>' 

            count+= 1

            new_seqname = '>S' + seq_number_gen(count)+'\n' 
            # write on the new output file the trade of description | generated code
            output.write(new_seqname)
            
        # if the line dont start with ">" write the the sequence normaly
        else:                      
            output.write(line)
            
            # aggregate the sequence description with the correnpondent generated code
            #dictio[new_seqname]=line[1:] 

function(arguments.input_fasta,arguments.output_fasta)

