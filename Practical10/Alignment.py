# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 10:15:51 2020

@author: skysblues
"""

import numpy as np
humanseq_file = open('SOD2_human.fa')
mouseseq_file = open('SOD2_mouse.fa')
randomseq_file = open('RandomSeq.fa')
seq1={'A':0, 'R':1, 'N':2, 'D':3, 'C':4, 'Q':5, 'E':6, 'G':7, 'H':8, 'I':9, 'L':10, 'K':11, 'M':12, 'F':13, 'P':14, 'S':15, 'T':16, 'W':17, 'Y':18, 'V':19, 'B':20, 'Z':21, 'X':22}
humanseq = ''
mouseseq = ''
randomseq = ''
humanseq_name = ''
mouseseq_name = ''
randomseq_name = ''
blosum = np.loadtxt('BLOSUM62.txt')
for line in humanseq_file:
    if not line.startswith ('>'):    
        humanseq = humanseq + str(line.strip('\n'))
    else:
        humanseq_name = str(line.strip('>'))
#read humanseq_file

for line in mouseseq_file:
    if not line.startswith ('>'):    
        mouseseq = mouseseq + str(line.strip('\n'))
    else:
        mouseseq_name = str(line.strip('>'))
#read mouseseq_file

for line in randomseq_file:
    if not line.startswith ('>'):    
        randomseq = randomseq + str(line.strip('\n'))
    else:
        randomseq_name = str(line.strip('>'))
#read randomseq_file

print('Name:'+ humanseq_name)
print('Sequence:' + humanseq + '\n')
print('Name:'+ mouseseq_name)
print('Sequence:' + mouseseq + '\n')
edit_distance = 0
similarity_of_seq = 0	
for i in range(len(humanseq)):	
      if humanseq[i]!=mouseseq[i]:  	
            edit_distance += 1
similarity_of_seq = (1- edit_distance / len(humanseq)) * 100
print ('Similarity:'+str(similarity_of_seq)+'%')
#print similarity

score = 0
for i in range(len(humanseq)):
    score = score + blosum[seq1[humanseq[i]],seq1[mouseseq[i]]]
print('Score:'+str(score))
print('\n\n\n')
#print score

print('Name:'+ humanseq_name)
print('Sequence:' + humanseq + '\n')
print('Name:'+ randomseq_name)
print('Sequence:' + randomseq + '\n')
edit_distance = 0
similarity_of_seq = 0	
for i in range(len(humanseq)):	
      if humanseq[i]!=randomseq[i]:  	
            edit_distance += 1
similarity_of_seq = (1- edit_distance / len(humanseq)) * 100
print ('Similarity:'+str(similarity_of_seq)+'%')
#print similarity

score = 0
for i in range(len(humanseq)):
    score = score + blosum[seq1[humanseq[i]],seq1[randomseq[i]]]
print('Score:'+str(score))
print('\n\n\n')
#print score

print('Name:'+ mouseseq_name)
print('Sequence:' + mouseseq + '\n')
print('Name:'+ randomseq_name)
print('Sequence:' + randomseq + '\n')
edit_distance = 0
similarity_of_seq = 0	
for i in range(len(mouseseq)):	
      if mouseseq[i]!=randomseq[i]:  	
            edit_distance += 1
similarity_of_seq = (1- edit_distance / len(mouseseq)) * 100
print ('Similarity:'+str(similarity_of_seq)+'%')
#print similarity

score = 0
for i in range(len(mouseseq)):
    score = score + blosum[seq1[mouseseq[i]],seq1[randomseq[i]]]
print('Score:'+str(score))
print('\n\n\n')
#print score