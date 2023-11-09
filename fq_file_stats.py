#! /usr/bin/env python
#  -*- coding: utf-8 -*-
# By Zaima Mushtaq

from CheckIsCompressed import isCompressed
from Bio import SeqIO
import gzip
from Bio.SeqUtils import GC
#count=0


def statistics(filename):
    count=1
    rlength=0
    gc=0
    if isCompressed(filename):
        with gzip.open(filename, "rt") as handle:
            for read in SeqIO.parse(handle,"fastq"):
                count=count+1
                gc=gc+GC(read.seq)
                rlength=rlength+len(read.seq)
            count=count-1
            average=round(rlength/count)
            gcper=round(gc/count)
            return [count,average,"Compressed",gcper]
    else:
        with open(filename, "rt") as handle:
            for read in SeqIO.parse(handle,"fastq"):
                count=count+1
                gc=gc+GC(read.seq)
                rlength=rlength+len(read.seq)
            count=count-1
            average=round(rlength/count)
            gcper=round(gc/count)
            return [count,average,"Simple Text",gcper]
            #return [count,rlength]
            #print("im here")

#filename="test.fastq"
#c=statistics(filename)
#print(c)

def statisticsSequenceLength(filename):
    count=1
    rlength=0
    for read in SeqIO.parse(filename,"fastq"):
        count=count+1
        rlength=rlength+len(read.seq)

    count=count-1
    average=rlength/count
