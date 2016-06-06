#! /usr/bin/env python
# python is on different parts in different computers. env is used to open it no matter where it is

# DNASeq = raw_input ('enter DNA sequence:')
# use variables with descriptive names. This variable is a string.
# raw_input for whatever is typed after will be considered as the input
DNASeq = 'AGAGAGAGAGAGAACTCTCTCCTCTCTCTAGAGAGAAGAGAG'
DNASeq = 'AGAAGA'
DNASeq = DNASeq.upper()
#strings cannot be edited. You can only create a new string that will replace another.

print ( 'Sequence ' + DNASeq )

SeqLength = float (len ( DNASeq ) )

#print ( 'Length is ' + SeqLength ) can't be concatenated because the 1st element is a string and the 2nd, a floating point

print ( 'Length is ' + str ( SeqLength ) )


NumberA = DNASeq.count ( 'A' )
NumberT = DNASeq.count ( 'T' )
NumberC = DNASeq.count ( 'C' )
NumberG = DNASeq.count ( 'G' )

print ( 'A: ' + str ( NumberA / SeqLength ) )

print ('A:{:.2f}'.format(NumberA / SeqLength))

TotalStrong = NumberG + NumberC
TotalWeak = NumberA + NumberT

if SeqLength <= 14:
	MeltTemp = ( 4 * TotalStrong ) + ( 2 * TotalWeak )

else:
	MeltTemp = 64.9 + 41 * (TotalStrong - 16.4) / SeqLength
	
print ( 'Melting Temp:{}'.format(MeltTemp) )



