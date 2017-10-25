# Python script to split a simulated hic paired-end fastq file into R1 and R2.
# Author: Ning Liu
# version 0.1.0


import sys
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
from Bio.SeqRecord import SeqRecord

def main(fastq):

    R1_out_name = fastq.replace(".fastq", "_R1.fastq")
    R2_out_name = fastq.replace(".fastq", "_R2.fastq")
    R1_out = open(R1_out_name, 'w')
    R2_out = open(R2_out_name, 'w')

    count = 1
    for record in SeqIO.parse(fastq,"fastq"):
        #print count
        seq = str(record.seq)
        Q = record.letter_annotations["phred_quality"]
        R_id = record.description
        if count%2!=0:
            R1 = SeqRecord(seq, id = R_id, description = "")
            R1.letter_annotations["phred_quality"] = Q
            R1_out.write(R1.format("fastq"),)
        else:
            R2 = SeqRecord(seq, id = R_id, description = "")
            R2.letter_annotations["phred_quality"] = Q
            R2_out.write(R2.format("fastq"),)
        count = count + 1


if __name__ == '__main__':
    main(sys.argv[1])
