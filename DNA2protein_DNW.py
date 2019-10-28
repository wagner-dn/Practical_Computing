#! /usr/bin/env python

from nucleic_fxns import *

#Ask user for filename that contains DNA sequence
InFileName = raw_input("Enter DNA sequence filename: ")
#InFileName = "DNAtoProtein_test.txt"

#Open and read DNA sequence file
InFile = open(InFileName, 'r')

for DNASeq in InFile:
	while len(DNASeq) % 3 != 0:
		DNASeq = DNASeq[:-1]

	RNASeq = trans(DNASeq)
	ProteinSeq = translate(RNASeq)
	print ProteinSeq

InFile.close()
