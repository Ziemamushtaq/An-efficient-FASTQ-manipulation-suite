'''
Module      : Find the sequence length of multiple fastq files
Description : .
Copyright   : (c) Zaima Mustaq, 29 july 2022 
License     : MIT 
Maintainer  : drzaimamushtq@gmail.com 
'''


import gzip
import glob

file_ls=glob.glob('*.fastq.gz') #identify all fastq.gz files and make them a list
number_of_file=len(file_ls) #count number of files

if number_of_file == 0:
    print("No FASTQ files were found.")
else:
    for files in file_ls:
        with gzip.open(files,'rb') as f:
            count=0
            for line in f:
                count=count+1
                if count==1: continue
                if count==2:
                    line=line.rstrip()
                    seq_length=len(line)
                    print(files,line,seq_length)
                else: break
