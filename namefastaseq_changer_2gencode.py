# -*- coding: utf-8 -*-

import argparse

parser = argparse.ArgumentParser(prog='python3')


parser.add_argument("input_fasta", metavar="input.fasta", type= str,
                    help= "Fasta file to replace sequence names/description for a generate code, e.g. S001")
      
                     #input file parser


parser.add_argument("output_fasta", metavar="output.fasta", type= str,
                    help= "Output fasta file where the sequence description/name was changed to a generated code")

                     #output file parser


arguments = parser.parse_args()


def seq_number_gen(count):
  """
  generate the code for the sequence description assume
  """
    seq_number= str(count)
    while len(seq_number) < 3:
        seq_number = "0" + seq_number
    return seq_number


def changer(input_file, output_file):
  #change de sequence description/name to the generated code
  
  
    file_handle = open(input_file, 'r') #open the input file

    output= open(output_file, 'w') #open the output file

    dictio={} #dicionary creation, description | code 

    count= 0 #count variable

    for line in file:

        if line.startswith('>'): #or line[0]=='>' 

            count+= 1

            new_seqname = '>S' + seq_number_gen(count)+'\n' 
     
            output.write(new_seqname) # write on the new output file the trade of description | generated code
            
       
        else:                         # if the line dont start with ">" write the the sequence normaly                   
            output.write(line)
            
            """
            aggregate the sequence description with the correnpondent generated code
            dictio[new_seqname]=line[1:] 
            """

changer(arguments.input_fasta,arguments.output_fasta)

