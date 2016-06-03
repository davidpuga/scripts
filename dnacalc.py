#! /usr/bin/env python
# python is on different parts in different computers. env is used to open it no matter where it is

DNASeq = 'ATGAAC'
# use variables with descriptive names. This variable is a string.

print ( 'Sequence ' + DNASeq )

SeqLength = float (len ( DNASeq ) )

#print ( 'Length is ' + SeqLength ) can't be concatenated because the 1st element is a string and the 2nd, a floating point

print ( 'Length is ' + str ( SeqLength ) )


NumberA = DNASeq.count ( 'A' )
#strings have a built-in function .count
NumberT = DNASeq.count ( 'T' )
NumberC = DNASeq.count ( 'C' )
NumberG = DNASeq.count ( 'G' )

print ( 'A: ' + str ( NumberA / SeqLength ) )